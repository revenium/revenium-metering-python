"""
Context management for Revenium metering.

Provides global and scoped context for attribution fields.
"""

import threading
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Optional, Dict, Any

__all__ = ["ReveniumContext", "set_context", "get_context", "context", "clear_context"]


@dataclass
class ReveniumContext:
    """Attribution context for Revenium metering."""
    agent: Optional[str] = None
    organization_id: Optional[str] = None
    product: Optional[str] = None
    subscriber_credential: Optional[str] = None
    workflow_id: Optional[str] = None
    trace_id: Optional[str] = None
    transaction_id: Optional[str] = None
    extra: Dict[str, Any] = field(default_factory=dict)

    def merge(self, **kwargs) -> "ReveniumContext":
        """Create a new context with overrides (None values don't override)."""
        return ReveniumContext(
            agent=kwargs.get("agent") or self.agent,
            organization_id=kwargs.get("organization_id") or self.organization_id,
            product=kwargs.get("product") or self.product,
            subscriber_credential=kwargs.get("subscriber_credential") or self.subscriber_credential,
            workflow_id=kwargs.get("workflow_id") or self.workflow_id,
            trace_id=kwargs.get("trace_id") or self.trace_id,
            transaction_id=kwargs.get("transaction_id") or self.transaction_id,
            extra={**self.extra, **kwargs.get("extra", {})},
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API calls."""
        result = {}
        if self.agent:
            result["agent"] = self.agent
        if self.organization_id:
            result["organizationId"] = self.organization_id
        if self.product:
            result["product"] = self.product
        if self.subscriber_credential:
            result["subscriberCredential"] = self.subscriber_credential
        if self.workflow_id:
            result["workflowId"] = self.workflow_id
        if self.trace_id:
            result["traceId"] = self.trace_id
        if self.transaction_id:
            result["transactionId"] = self.transaction_id
        result.update(self.extra)
        return result


# Thread-local storage for context
_context_local = threading.local()


def _get_context_stack() -> list:
    """Get the context stack for the current thread."""
    if not hasattr(_context_local, "stack"):
        _context_local.stack = [ReveniumContext()]
    return _context_local.stack


def set_context(
    agent: Optional[str] = None,
    organization_id: Optional[str] = None,
    product: Optional[str] = None,
    subscriber_credential: Optional[str] = None,
    workflow_id: Optional[str] = None,
    trace_id: Optional[str] = None,
    transaction_id: Optional[str] = None,
    **extra,
) -> None:
    """
    Set global context for all subsequent metered calls.

    Example:
        revenium.set_context(
            agent="my-agent",
            organization_id="acme-org",
            product="gold-tier"
        )
    """
    stack = _get_context_stack()
    stack[0] = ReveniumContext(
        agent=agent,
        organization_id=organization_id,
        product=product,
        subscriber_credential=subscriber_credential,
        workflow_id=workflow_id,
        trace_id=trace_id,
        transaction_id=transaction_id,
        extra=extra,
    )


def get_context() -> ReveniumContext:
    """Get the current context (top of stack)."""
    stack = _get_context_stack()
    return stack[-1] if stack else ReveniumContext()


def clear_context() -> None:
    """Clear all context."""
    _context_local.stack = [ReveniumContext()]


@contextmanager
def context(
    agent: Optional[str] = None,
    organization_id: Optional[str] = None,
    product: Optional[str] = None,
    subscriber_credential: Optional[str] = None,
    workflow_id: Optional[str] = None,
    trace_id: Optional[str] = None,
    transaction_id: Optional[str] = None,
    **extra,
):
    """
    Context manager for scoped context overrides.

    Example:
        with revenium.context(agent="sub-agent", workflow_id="sub-workflow"):
            # Calls here use the scoped context
            scrape(url)
    """
    stack = _get_context_stack()
    current = get_context()
    new_context = current.merge(
        agent=agent,
        organization_id=organization_id,
        product=product,
        subscriber_credential=subscriber_credential,
        workflow_id=workflow_id,
        trace_id=trace_id,
        transaction_id=transaction_id,
        extra=extra,
    )
    stack.append(new_context)
    try:
        yield new_context
    finally:
        stack.pop()
