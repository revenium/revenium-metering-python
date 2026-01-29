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
    # Deprecated fields - kept for backward compatibility (must come before new fields for positional args)
    organization_id: Optional[str] = None  # DEPRECATED: Use organization_name
    product: Optional[str] = None  # DEPRECATED: Use product_name
    # New fields
    organization_name: Optional[str] = None
    product_name: Optional[str] = None
    subscriber_credential: Optional[str] = None
    workflow_id: Optional[str] = None
    trace_id: Optional[str] = None
    transaction_id: Optional[str] = None
    extra: Dict[str, Any] = field(default_factory=lambda: {})

    def merge(self, **kwargs: Any) -> ReveniumContext:
        """Create a new context with overrides (None values don't override)."""
        extra_dict: Dict[str, Any] = kwargs.get("extra", {})

        # Support both new and deprecated field names
        # Check if new field names are explicitly provided (not just present as None)
        has_org_name = "organization_name" in kwargs and kwargs["organization_name"] is not None
        has_org_id = "organization_id" in kwargs and kwargs["organization_id"] is not None
        has_prod_name = "product_name" in kwargs and kwargs["product_name"] is not None
        has_product = "product" in kwargs and kwargs["product"] is not None

        # Determine final values with proper precedence and type coercion
        if has_org_name:
            org_name = str(kwargs["organization_name"])
            org_id = None  # Clear deprecated field when new field is provided
        elif has_org_id:
            org_name = str(kwargs["organization_id"])
            org_id = None  # Clear deprecated field (value is in org_name)
        else:
            # Use existing value, preferring new field over deprecated
            existing_val = self.organization_name or self.organization_id
            org_name = str(existing_val) if existing_val is not None else None
            org_id = None

        if has_prod_name:
            prod_name = str(kwargs["product_name"])
            product_val = None  # Clear deprecated field when new field is provided
        elif has_product:
            prod_name = str(kwargs["product"])
            product_val = None  # Clear deprecated field (value is in prod_name)
        else:
            # Use existing value, preferring new field over deprecated
            existing_val = self.product_name or self.product
            prod_name = str(existing_val) if existing_val is not None else None
            product_val = None

        return ReveniumContext(
            agent=_merge_field(kwargs, "agent", self.agent),
            organization_id=org_id,
            product=product_val,
            organization_name=org_name,
            product_name=prod_name,
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
        # Use new field names, fallback to deprecated fields
        if self.organization_name:
            result["organizationName"] = self.organization_name
        elif self.organization_id:
            result["organizationName"] = self.organization_id
        if self.product_name:
            result["productName"] = self.product_name
        elif self.product:
            result["productName"] = self.product
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
    # Deprecated parameters - kept for backward compatibility
    organization_id: Optional[str] = None,
    product: Optional[str] = None,
    # New parameters
    organization_name: Optional[str] = None,
    product_name: Optional[str] = None,
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
            organization_name="AcmeCorp",
            product_name="customer-chatbot"
        )
    """
    # Use new fields, fallback to deprecated fields
    final_org_name = organization_name if organization_name is not None else organization_id
    final_prod_name = product_name if product_name is not None else product

    # Clear deprecated fields when new fields are provided to prevent inconsistency
    final_org_id = None if organization_name is not None else organization_id
    final_product = None if product_name is not None else product

    new_base = ReveniumContext(
        agent=agent,
        organization_id=final_org_id,
        product=final_product,
        organization_name=final_org_name,
        product_name=final_prod_name,
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
    # Deprecated parameters - kept for backward compatibility
    organization_id: Optional[str] = None,
    product: Optional[str] = None,
    # New parameters
    organization_name: Optional[str] = None,
    product_name: Optional[str] = None,
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
        organization_name=organization_name,
        product_name=product_name,
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
