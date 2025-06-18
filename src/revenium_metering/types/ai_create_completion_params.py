# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AICreateCompletionParams"]


class AICreateCompletionParams(TypedDict, total=False):
    completion_start_time: Required[Annotated[str, PropertyInfo(alias="completionStartTime")]]
    """Time to first token for streaming requests"""

    cost_type: Required[Annotated[Literal["AI"], PropertyInfo(alias="costType")]]
    """Cost type for the completion"""

    input_token_count: Required[Annotated[int, PropertyInfo(alias="inputTokenCount")]]
    """The count of consumed input tokens"""

    is_streamed: Required[Annotated[bool, PropertyInfo(alias="isStreamed")]]
    """Indicates if the completion was streamed"""

    model: Required[str]
    """The model used for generating the LLM completion"""

    output_token_count: Required[Annotated[int, PropertyInfo(alias="outputTokenCount")]]
    """The count of consumed output tokens"""

    provider: Required[str]
    """Vendor providing the LLM completion service"""

    request_duration: Required[Annotated[int, PropertyInfo(alias="requestDuration")]]
    """The duration of the request in milliseconds"""

    request_time: Required[Annotated[str, PropertyInfo(alias="requestTime")]]
    """The timestamp when the request was made"""

    response_time: Required[Annotated[str, PropertyInfo(alias="responseTime")]]
    """The timestamp when the response was generated.

    If streaming, this is the time to first token
    """

    stop_reason: Required[
        Annotated[
            Literal["END", "END_SEQUENCE", "TIMEOUT", "TOKEN_LIMIT", "COST_LIMIT", "COMPLETION_LIMIT", "ERROR"],
            PropertyInfo(alias="stopReason"),
        ]
    ]
    """The reason for stopping the completion"""

    total_token_count: Required[Annotated[int, PropertyInfo(alias="totalTokenCount")]]
    """The total number of tokens"""

    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]
    """The unique identifier of the LLM completion transaction"""

    agent: str
    """The AI agent that is making the request"""

    cache_creation_token_count: Annotated[int, PropertyInfo(alias="cacheCreationTokenCount")]
    """The number of cached creation tokens in the completion"""

    cache_read_token_count: Annotated[int, PropertyInfo(alias="cacheReadTokenCount")]
    """The number of cached read tokens in the completion"""

    error_reason: Annotated[str, PropertyInfo(alias="errorReason")]
    """The details of the error that occurred during the LLM completion"""

    input_token_cost: Annotated[float, PropertyInfo(alias="inputTokenCost")]
    """The input token cost associated with the LLM completion"""

    mediation_latency: Annotated[int, PropertyInfo(alias="mediationLatency")]
    """The latency, in milliseconds, of latency by an AI or API gateway"""

    model_source: Annotated[str, PropertyInfo(alias="modelSource")]
    """The source of the AI model used for the completion"""

    operation_type: Annotated[
        Literal["CHAT", "GENERATE", "EMBED", "CLASSIFY", "SUMMARIZE", "TRANSLATE", "TOOL_CALL", "RERANK", "SEARCH", "MODERATION", "VISION", "TRANSFORM", "GUARDRAIL", "OTHER"],
        PropertyInfo(alias="operationType"),
    ]
    """The type of operation performed"""

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """
    Populate the ID of the subscriber’s organization from your system to allow
    Revenium to track usage & costs by company. i.e. AcmeCorp. If several
    subscriberIds have the same organizationId, Revenium’s reporting will show usage
    for the entire organization broken down by user.
    """

    output_token_cost: Annotated[float, PropertyInfo(alias="outputTokenCost")]
    """The output token cost associated with the LLM completion"""

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """
    Identifier of the product from your own system that you wish to use to correlate
    usage between Revenium & your application.
    """

    reasoning_token_count: Annotated[int, PropertyInfo(alias="reasoningTokenCount")]
    """The number of reasoning tokens in the completion"""

    response_quality_score: Annotated[float, PropertyInfo(alias="responseQualityScore")]
    """The quality score of the response"""

    subscriber_credential: Annotated[str, PropertyInfo(alias="subscriberCredential")]
    """
    Populate the ID of the subscriber from your system to allow Revenium to track
    usage & costs for individual users.
    """

    subscriber_credential_name: Annotated[str, PropertyInfo(alias="subscriberCredentialName")]
    """
    Populate the name of the subscriber credential from your system to allow
    Revenium to track usage & costs for individual users.
    """

    subscriber_email: Annotated[str, PropertyInfo(alias="subscriberEmail")]
    """The email address of the subscriber"""

    subscriber_id: Annotated[str, PropertyInfo(alias="subscriberId")]
    """
    Populate the ID of the subscriber from your system to allow Revenium to track
    usage & costs for individual users. i.e. user-123. If several
    subscriberCredentials have the same subscriberId, Revenium’s reporting will show
    usage for the entire organization broken down by user.
    """

    subscription_id: Annotated[str, PropertyInfo(alias="subscriptionId")]
    """
    Unique identifier of the subscription from your own system that you wish to use
    to correlate usage between Revenium & your application.
    """

    system_fingerprint: Annotated[str, PropertyInfo(alias="systemFingerprint")]
    """
    A unique identifier that represents the statistical signature of the language
    model that generated a specific chat completion. This fingerprint can be used
    for model attribution, debugging, and monitoring model behavior across request
    """

    task_type: Annotated[str, PropertyInfo(alias="taskType")]
    """
    If you wish to track the costs or performance of a specific task and compare the
    values over time or compare the performance across AI models or vendors, use a
    consistent taskType for all related tasks.
    """

    temperature: float
    """The temperature setting used for the LLM completion"""

    time_to_first_token: Annotated[int, PropertyInfo(alias="timeToFirstToken")]
    """The time to first token in milliseconds"""

    total_cost: Annotated[float, PropertyInfo(alias="totalCost")]
    """The total cost associated with the LLM completion"""

    trace_id: Annotated[str, PropertyInfo(alias="traceId")]
    """Trace multiple LLM calls belonging to same overall request"""

    credential_alias: Annotated[str, PropertyInfo(alias="credentialAlias")]
    """Human-readable name for the API key being used"""

    environment: str
    """Deployment environment identifier (e.g., 'production', 'staging', 'development')"""

    operation_subtype: Annotated[str, PropertyInfo(alias="operationSubtype")]
    """Additional operation detail (e.g., 'function_call', 'sql_query')"""

    parent_transaction_id: Annotated[str, PropertyInfo(alias="parentTransactionId")]
    """Link to parent transaction for distributed tracing"""

    region: str
    """Cloud region or data center (e.g., 'us-east-1', 'ap-southeast-2')"""

    retry_number: Annotated[int, PropertyInfo(alias="retryNumber")]
    """Retry attempt counter (0 for first attempt, 1 for first retry, etc.)"""

    trace_name: Annotated[str, PropertyInfo(alias="traceName")]
    """Human-readable label for this trace instance (max 256 chars)"""

    trace_type: Annotated[str, PropertyInfo(alias="traceType")]
    """Categorical identifier for grouping workflows (alphanumeric, hyphens, underscores; max 128 chars)"""

    transaction_name: Annotated[str, PropertyInfo(alias="transactionName")]
    """Human-friendly name for this operation"""
