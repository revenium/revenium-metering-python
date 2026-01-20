"""
Revenium metering decorator for tool calls.

Automatically meters function execution with timing, success/failure, and attribution.

Data flow: Python SDK -> Metering API (/v2/tool/events) -> Kafka -> Clickhouse
"""

from __future__ import annotations

import time
import uuid
import asyncio
import functools
from typing import Any, Dict, List, TypeVar, Callable, Optional, cast
from datetime import datetime, timezone

import httpx

from .context import ReveniumContext, get_context
from ._utils._logs import logger

__all__ = ["meter", "report_tool_call", "configure"]

F = TypeVar("F", bound=Callable[..., Any])

# Global configuration (set via configure())
_metering_url: Optional[str] = None
_api_key: Optional[str] = None


def configure(
    metering_url: str = "http://localhost:8082",
    api_key: str = "demo-key",
) -> None:
    """
    Configure the metering client.

    Example:
        import revenium_metering as revenium
        revenium.configure(
            metering_url="http://localhost:8082",
            api_key="your-api-key",
        )
    """
    global _metering_url, _api_key
    _metering_url = metering_url
    _api_key = api_key


def _build_event_payload(
    tool_id: str,
    operation: Optional[str],
    duration_ms: int,
    success: bool,
    error_message: Optional[str],
    usage_metadata: Optional[Dict[str, Any]],
    context: ReveniumContext,
) -> Dict[str, Any]:
    """Build the event payload for the metering API."""
    transaction_id = context.transaction_id or str(uuid.uuid4())
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    event_payload: Dict[str, Any] = {
        "transactionId": transaction_id,
        "toolId": tool_id,
        "operation": operation or "execute",
        "durationMs": duration_ms,
        "success": success,
        "timestamp": timestamp,
    }

    if error_message:
        event_payload["errorMessage"] = error_message

    if usage_metadata:
        event_payload["usageMetadata"] = usage_metadata

    # Add context fields (agent, product, organizationId, etc.)
    if context.agent:
        event_payload["agent"] = context.agent
    if context.organization_id:
        event_payload["organizationId"] = context.organization_id
    if context.product:
        event_payload["product"] = context.product
    if context.subscriber_credential:
        event_payload["subscriberCredential"] = context.subscriber_credential
    if context.workflow_id:
        event_payload["workflowId"] = context.workflow_id
    if context.trace_id:
        event_payload["traceId"] = context.trace_id

    return event_payload


def _send_tool_event(
    tool_id: str,
    operation: Optional[str],
    duration_ms: int,
    success: bool,
    error_message: Optional[str],
    usage_metadata: Optional[Dict[str, Any]],
    context: ReveniumContext,
) -> None:
    """
    Send tool event to metering API via /v2/tool/events endpoint.

    This goes through the proper pipeline:
    Metering API -> Kafka (hypercurrent.metering.tool-events) -> Clickhouse
    """
    url = _metering_url or "http://localhost:8082"
    key = _api_key or "demo-key"

    event_payload = _build_event_payload(
        tool_id, operation, duration_ms, success, error_message, usage_metadata, context
    )

    try:
        with httpx.Client(timeout=5.0) as client:
            response = client.post(
                f"{url}/v2/tool/events",
                headers={
                    "x-api-key": key,
                    "Content-Type": "application/json",
                },
                json=event_payload,
            )
            response.raise_for_status()
            logger.debug("[metered] %s:%s %dms", tool_id, operation or "execute", duration_ms)
    except Exception as e:
        # Non-blocking - just log and continue
        logger.warning("metering error: %s", e)


async def _send_tool_event_async(
    tool_id: str,
    operation: Optional[str],
    duration_ms: int,
    success: bool,
    error_message: Optional[str],
    usage_metadata: Optional[Dict[str, Any]],
    context: ReveniumContext,
) -> None:
    """
    Async version of _send_tool_event for use in async contexts.

    Uses httpx.AsyncClient to avoid blocking the event loop.
    """
    url = _metering_url or "http://localhost:8082"
    key = _api_key or "demo-key"

    event_payload = _build_event_payload(
        tool_id, operation, duration_ms, success, error_message, usage_metadata, context
    )

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.post(
                f"{url}/v2/tool/events",
                headers={
                    "x-api-key": key,
                    "Content-Type": "application/json",
                },
                json=event_payload,
            )
            response.raise_for_status()
            logger.debug("[metered] %s:%s %dms", tool_id, operation or "execute", duration_ms)
    except Exception as e:
        # Non-blocking - just log and continue
        logger.warning("metering error: %s", e)


def report_tool_call(
    tool_id: str,
    operation: Optional[str] = None,
    duration_ms: int = 0,
    success: bool = True,
    error_message: Optional[str] = None,
    usage_metadata: Optional[Dict[str, Any]] = None,
    agent: Optional[str] = None,
    organization_id: Optional[str] = None,
    product: Optional[str] = None,
    subscriber_credential: Optional[str] = None,
    workflow_id: Optional[str] = None,
    trace_id: Optional[str] = None,
    transaction_id: Optional[str] = None,
) -> None:
    """
    Manually report a tool call.

    Example:
        revenium.report_tool_call(
            tool_id="firecrawl",
            operation="scrape",
            duration_ms=1234,
            success=True,
            usage_metadata={"pages": 5, "data_mb": 2.3},
            agent="my-agent"
        )
    """
    ctx = get_context().merge(
        agent=agent,
        organization_id=organization_id,
        product=product,
        subscriber_credential=subscriber_credential,
        workflow_id=workflow_id,
        trace_id=trace_id,
        transaction_id=transaction_id,
    )
    _send_tool_event(
        tool_id=tool_id,
        operation=operation,
        duration_ms=duration_ms,
        success=success,
        error_message=error_message,
        usage_metadata=usage_metadata,
        context=ctx,
    )


def _extract_output_fields(result: Any, output_fields: Optional[List[str]]) -> Optional[Dict[str, Any]]:
    """Extract specified fields from the result for usage metadata.

    Wrapped in try/except to avoid overriding the wrapped function's exception
    if a property accessor throws.
    """
    if not output_fields or result is None:
        return None

    try:
        usage_metadata: Dict[str, Any] = {}
        for field_name in output_fields:
            if isinstance(result, dict):
                if field_name in result:
                    usage_metadata[field_name] = result[field_name]
            elif hasattr(result, field_name):
                usage_metadata[field_name] = getattr(result, field_name)

        return usage_metadata if usage_metadata else None
    except Exception:
        # Don't let output field extraction errors override the wrapped function's result
        return None


def meter(
    tool_id: str,
    operation: Optional[str] = None,
    output_fields: Optional[List[str]] = None,
    agent: Optional[str] = None,
    organization_id: Optional[str] = None,
    product: Optional[str] = None,
    subscriber_credential: Optional[str] = None,
    workflow_id: Optional[str] = None,
    trace_id: Optional[str] = None,
) -> Callable[[F], F]:
    """
    Decorator to automatically meter tool function calls.

    Captures timing, success/failure, and reports to Revenium metering.

    Example:
        @revenium.meter("firecrawl")
        def scrape(url):
            return firecrawl.scrape(url)

        @revenium.meter("fal_flux", operation="generate_image", agent="image-bot")
        async def generate_image(prompt):
            return await fal.run("fal-ai/flux", {"prompt": prompt})

        @revenium.meter("runway", output_fields=["duration_seconds", "resolution"])
        def generate_video(prompt):
            return runway.generate(prompt)
    """

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
            ctx = get_context().merge(
                agent=agent,
                organization_id=organization_id,
                product=product,
                subscriber_credential=subscriber_credential,
                workflow_id=workflow_id,
                trace_id=trace_id,
            )
            # Only generate transaction_id if not provided by context
            if not ctx.transaction_id:
                ctx = ctx.merge(transaction_id=str(uuid.uuid4()))

            start_time = time.perf_counter()
            call_success = True
            call_error_message: Optional[str] = None
            result: Any = None

            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                call_success = False
                call_error_message = str(e)
                raise
            finally:
                duration_ms = int((time.perf_counter() - start_time) * 1000)
                usage_metadata = _extract_output_fields(result, output_fields)

                _send_tool_event(
                    tool_id=tool_id,
                    operation=operation,
                    duration_ms=duration_ms,
                    success=call_success,
                    error_message=call_error_message,
                    usage_metadata=usage_metadata,
                    context=ctx,
                )

        @functools.wraps(func)
        async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
            ctx = get_context().merge(
                agent=agent,
                organization_id=organization_id,
                product=product,
                subscriber_credential=subscriber_credential,
                workflow_id=workflow_id,
                trace_id=trace_id,
            )
            # Only generate transaction_id if not provided by context
            if not ctx.transaction_id:
                ctx = ctx.merge(transaction_id=str(uuid.uuid4()))

            start_time = time.perf_counter()
            call_success = True
            call_error_message: Optional[str] = None
            result: Any = None

            try:
                result = await func(*args, **kwargs)
                return result
            except Exception as e:
                call_success = False
                call_error_message = str(e)
                raise
            finally:
                duration_ms = int((time.perf_counter() - start_time) * 1000)
                usage_metadata = _extract_output_fields(result, output_fields)

                await _send_tool_event_async(
                    tool_id=tool_id,
                    operation=operation,
                    duration_ms=duration_ms,
                    success=call_success,
                    error_message=call_error_message,
                    usage_metadata=usage_metadata,
                    context=ctx,
                )

        # Auto-detect sync vs async
        if asyncio.iscoroutinefunction(func):
            return cast(F, async_wrapper)
        return cast(F, sync_wrapper)

    return decorator
