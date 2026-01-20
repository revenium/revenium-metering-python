"""
Context management for Revenium metering.

Provides global and scoped context for attribution fields.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Generator
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import field, dataclass

__all__ = ["ReveniumContext", "set_context", "get_context", "context", "clear_context"]


def _merge_field(kwargs: Dict[str, Any], key: str, default: Optional[str]) -> Optional[str]:
    """Merge a field, only using default if key is not in kwargs or value is None."""
    if key in kwargs and kwargs[key] is not None:
        return str(kwargs[key])
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
    extra: Dict[str, Any] = field(default_factory=lambda: {})

    def merge(self, **kwargs: Any) -> ReveniumContext:
        """Create a new context with overrides (None values don't override)."""
        extra_dict: Dict[str, Any] = kwargs.get("extra", {})
        return ReveniumContext(
            agent=_merge_field(kwargs, "agent", self.agent),
            organization_id=_merge_field(kwargs, "organization_id", self.organization_id),
            product=_merge_field(kwargs, "product", self.product),
            subscriber_credential=_merge_field(kwargs, "subscriber_credential", self.subscriber_credential),
            workflow_id=_merge_field(kwargs, "workflow_id", self.workflow_id),
            trace_id=_merge_field(kwargs, "trace_id", self.trace_id),
            transaction_id=_merge_field(kwargs, "transaction_id", self.transaction_id),
            extra={**self.extra, **extra_dict},
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for API calls."""
        result: Dict[str, Any] = {}
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
_context_stack: ContextVar[Optional[List[ReveniumContext]]] = ContextVar(
    "revenium_context_stack",
    default=None,
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
    **extra: Any,
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
    new_base = ReveniumContext(
        agent=agent,
        organization_id=organization_id,
        product=product,
        subscriber_credential=subscriber_credential,
        workflow_id=workflow_id,
        trace_id=trace_id,
        transaction_id=transaction_id,
        extra=extra,
    )
    # Replace the base context, keeping any scoped contexts on top
    current_stack = _context_stack.get()
    if current_stack is None or len(current_stack) <= 1:
        _context_stack.set([new_base])
    else:
        # Preserve scoped contexts, replace base
        _context_stack.set([new_base, *current_stack[1:]])


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
    **extra: Any,
) -> Generator[ReveniumContext, None, None]:
    """
    Context manager for scoped context overrides.

    Example:
        with revenium.context(agent="sub-agent", workflow_id="sub-workflow"):
            # Calls here use the scoped context
            scrape(url)
    """
    current_stack = _get_context_stack()
    current = current_stack[-1] if current_stack else ReveniumContext()
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
    # Use copy-on-write to avoid mutating shared list across async Tasks
    new_stack = [*current_stack, new_context]
    token = _context_stack.set(new_stack)
    try:
        yield new_context
    finally:
        _context_stack.reset(token)
