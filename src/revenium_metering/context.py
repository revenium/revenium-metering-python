"""
Context management for Revenium metering.

Provides global and scoped context for attribution fields.
"""

from contextvars import ContextVar
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List

__all__ = ["ReveniumContext", "set_context", "get_context", "context", "clear_context"]


def _merge_field(kwargs: Dict[str, Any], key: str, default: Any) -> Any:
    """Merge a field, only using default if key is not in kwargs or value is None."""
    if key in kwargs and kwargs[key] is not None:
        return kwargs[key]
    return default


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
            agent=_merge_field(kwargs, "agent", self.agent),
            organization_id=_merge_field(kwargs, "organization_id", self.organization_id),
            product=_merge_field(kwargs, "product", self.product),
            subscriber_credential=_merge_field(kwargs, "subscriber_credential", self.subscriber_credential),
            workflow_id=_merge_field(kwargs, "workflow_id", self.workflow_id),
            trace_id=_merge_field(kwargs, "trace_id", self.trace_id),
            transaction_id=_merge_field(kwargs, "transaction_id", self.transaction_id),
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


# ContextVar for async-safe context (works with both threads and asyncio Tasks)
_context_stack: ContextVar[List[ReveniumContext]] = ContextVar(
    "revenium_context_stack",
    default=None,  # type: ignore
)


def _get_context_stack() -> List[ReveniumContext]:
    """Get the context stack for the current context (thread or asyncio Task)."""
    stack = _context_stack.get()
    if stack is None:
        stack = [ReveniumContext()]
        _context_stack.set(stack)
    return stack


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
    _context_stack.set([ReveniumContext()])


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
