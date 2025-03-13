# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AICreateCompletionParams"]


class AICreateCompletionParams(TypedDict, total=False):
    audio_token_count: Required[Annotated[int, PropertyInfo(alias="audioTokenCount")]]
    """The number of audio tokens in the completion"""

    cached_token_count: Required[Annotated[int, PropertyInfo(alias="cachedTokenCount")]]
    """The number of cached tokens in the completion"""

    completion_start_time: Required[Annotated[str, PropertyInfo(alias="completionStartTime")]]
    """Time to first token for streaming requests"""

    completion_token_count: Required[Annotated[int, PropertyInfo(alias="completionTokenCount")]]
    """The number of tokens in the completion"""

    cost_type: Required[Annotated[Literal["AI"], PropertyInfo(alias="costType")]]
    """Cost type for the completion"""

    model: Required[str]
    """The model used for generating the LLM completion"""

    prompt_token_count: Required[Annotated[int, PropertyInfo(alias="promptTokenCount")]]
    """The number of tokens in the prompt"""

    provider: Required[str]
    """Vendor providing the LLM completion service"""

    reasoning_token_count: Required[Annotated[int, PropertyInfo(alias="reasoningTokenCount")]]
    """The number of reasoning tokens in the completion"""

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

    transaction_cost: Required[Annotated[float, PropertyInfo(alias="transactionCost")]]
    """The cost associated with the LLM completion"""

    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]
    """The unique identifier of the LLM completion transaction"""

    agent: str
    """The AI agent that is making the request"""

    ai_provider_key_name: Annotated[str, PropertyInfo(alias="aiProviderKeyName")]
    """The name (not the value!) of the API key used to access the AI provider"""

    api_key: Annotated[str, PropertyInfo(alias="apiKey")]

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """
    Populate the ID of the subscriber’s organization from your system to allow
    Revenium to track usage & costs by company. i.e. AcmeCorp. If several
    subscriberIds have the same organizationId, Revenium’s reporting will show usage
    for the entire organization broken down by user.
    """

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """
    Identifier of the product from your own system that you wish to use to correlate
    usage between Revenium & your application.
    """

    source_id: Annotated[str, PropertyInfo(alias="sourceId")]
    """
    Identifier of the source to correlate usage between Revenium & your application.
    """

    subscriber_identity: Annotated[str, PropertyInfo(alias="subscriberIdentity")]
    """
    Populate the ID of the subscriber from your system to allow Revenium to track
    usage & costs for individual users. Oftentimes a subscriberId is an email
    address.
    """

    subscription_id: Annotated[str, PropertyInfo(alias="subscriptionId")]
    """
    Unique identifier of the subscription from your own system that you wish to use
    to correlate usage between Revenium & your application.
    """

    task_id: Annotated[str, PropertyInfo(alias="taskId")]
    """Identifier of the associated task.

    If you wish to track the costs and performance for a task that occurs over
    several prompts, use a consistent task ID for all prompts included in that task.
    """

    task_type: Annotated[str, PropertyInfo(alias="taskType")]
    """
    If you wish to track the costs or performance of a specific task and compare the
    values over time or compare the performance across AI models or vendors, use a
    consistent taskType for all related tasks.
    """

    trace_id: Annotated[str, PropertyInfo(alias="traceId")]
    """Trace multiple LLM calls belonging to same overall request"""
