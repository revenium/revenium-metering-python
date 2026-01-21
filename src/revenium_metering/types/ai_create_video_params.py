# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AICreateVideoParams", "Subscriber", "SubscriberCredential"]


class AICreateVideoParams(TypedDict, total=False):
    model: Required[str]
    """The AI model identifier used for this video operation"""

    provider: Required[str]
    """The underlying AI provider/vendor whose model is processing the request"""

    request_duration: Required[Annotated[int, PropertyInfo(alias="requestDuration")]]
    """The total duration of the AI video request in milliseconds"""

    request_time: Required[Annotated[str, PropertyInfo(alias="requestTime")]]
    """The timestamp when your application sent the request to the AI provider (ISO 8601 format)"""

    response_time: Required[Annotated[str, PropertyInfo(alias="responseTime")]]
    """The timestamp when the AI video operation finished (ISO 8601 format)"""

    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]
    """The unique identifier of the video transaction"""

    # Video-specific billing fields
    duration_seconds: Required[Annotated[float, PropertyInfo(alias="durationSeconds")]]
    """Duration of the generated video in seconds"""

    credits_consumed: Annotated[float, PropertyInfo(alias="creditsConsumed")]
    """Number of credits consumed for this video generation"""

    requested_duration_seconds: Annotated[float, PropertyInfo(alias="requestedDurationSeconds")]
    """The duration requested by the user (may differ from actual duration)"""

    credit_rate: Annotated[float, PropertyInfo(alias="creditRate")]
    """The rate at which credits are consumed per second"""

    # Video metadata fields
    fps: int
    """Frames per second of the generated video"""

    resolution: str
    """Video resolution (e.g., '1080p', '720p', '4K')"""

    video_job_id: Annotated[str, PropertyInfo(alias="videoJobId")]
    """Unique identifier for the video generation job"""

    async_operation: Annotated[bool, PropertyInfo(alias="asyncOperation")]
    """Whether this was an asynchronous video generation operation"""

    operation_subtype: Annotated[str, PropertyInfo(alias="operationSubtype")]
    """Technical classification of the video operation (e.g., 'generation', 'editing')"""

    # Cost and error fields
    total_cost: Annotated[float, PropertyInfo(alias="totalCost")]
    """The total cost in USD for this video operation (overrides automatic calculation)"""

    error_reason: Annotated[str, PropertyInfo(alias="errorReason")]
    """Error message or reason if the video operation failed"""

    error_code: Annotated[int, PropertyInfo(alias="errorCode")]
    """HTTP error code if the operation failed"""

    billing_skipped: Annotated[bool, PropertyInfo(alias="billingSkipped")]
    """If true, backend returns $0 cost"""

    skip_reason: Annotated[
        Literal["FREE_TIER", "RATE_LIMITED", "ERROR_RESPONSE", "INTERNAL_TEST"],
        PropertyInfo(alias="skipReason")
    ]
    """Reason why billing was skipped"""

    # Subscriber information
    subscriber: Subscriber
    """The subscriber metadata"""

    subscriber_email: Annotated[str, PropertyInfo(alias="subscriberEmail")]
    """The email address of the subscriber"""

    subscriber_id: Annotated[str, PropertyInfo(alias="subscriberId")]
    """Unique identifier for the subscriber"""

    subscription_id: Annotated[str, PropertyInfo(alias="subscriptionId")]
    """Unique identifier of the subscription"""

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """ID of the subscriber's organization"""

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """Identifier of the product"""

    # Tracing and context fields
    trace_id: Annotated[str, PropertyInfo(alias="traceId")]
    """Trace multiple video calls belonging to same overall request"""

    trace_type: Annotated[str, PropertyInfo(alias="traceType")]
    """Categorical identifier for grouping workflows"""

    trace_name: Annotated[str, PropertyInfo(alias="traceName")]
    """Human-readable label for this trace instance"""

    parent_transaction_id: Annotated[str, PropertyInfo(alias="parentTransactionId")]
    """Link to parent transaction for distributed tracing"""

    transaction_name: Annotated[str, PropertyInfo(alias="transactionName")]
    """Human-friendly name for this operation"""

    task_type: Annotated[str, PropertyInfo(alias="taskType")]
    """Task type for tracking costs or performance"""

    agent: str
    """The AI agent that is making the request"""

    environment: str
    """Deployment environment identifier (e.g., 'production', 'staging', 'development')"""

    region: str
    """Cloud region or data center (e.g., 'us-east-1', 'ap-southeast-2')"""

    retry_number: Annotated[int, PropertyInfo(alias="retryNumber")]
    """Retry attempt counter (0 for first attempt, 1 for first retry, etc.)"""

    middleware_source: Annotated[str, PropertyInfo(alias="middlewareSource")]
    """The source middleware or SDK that generated this request"""

    model_source: Annotated[str, PropertyInfo(alias="modelSource")]
    """The source of the AI model used"""

    credential_alias: Annotated[str, PropertyInfo(alias="credentialAlias")]
    """Human-readable name for the API key being used"""


class SubscriberCredential(TypedDict, total=False):
    name: str
    """An alias for an API key used by one or more users"""

    value: str
    """The key value associated with the subscriber"""


class Subscriber(TypedDict, total=False):
    id: str
    """Track cost & performance by individual users"""

    credential: SubscriberCredential
    """The credential used by the subscriber"""

    email: str
    """The email address of the subscriber"""

