# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AICreateCompletionParams", "Subscriber", "SubscriberCredential"]


class AICreateCompletionParams(TypedDict, total=False):
    completion_start_time: Required[Annotated[str, PropertyInfo(alias="completionStartTime")]]
    """
    The timestamp when the AI completion started generating output, in ISO 8601
    format with UTC timezone. For streaming requests, this is when the first token
    was received. For non-streaming requests, this is typically the same as or very
    close to responseTime. Used to calculate time-to-first-token latency for
    streaming completions.
    """

    cost_type: Required[Annotated[Literal["AI"], PropertyInfo(alias="costType")]]
    """The type of cost being tracked.

    Currently always 'AI' for AI completion costs. This field is used internally by
    Revenium to categorize different types of metered usage. You typically do not
    need to set this field as it defaults to 'AI'.
    """

    input_token_count: Required[Annotated[int, PropertyInfo(alias="inputTokenCount")]]
    """The count of consumed input tokens"""

    is_streamed: Required[Annotated[bool, PropertyInfo(alias="isStreamed")]]
    """
    Indicates whether this completion used streaming (true) or non-streaming/batch
    mode (false). Streaming completions receive tokens incrementally as they're
    generated, while non-streaming completions wait for the complete response. This
    affects how timeToFirstToken and responseTime are interpreted.
    """

    model: Required[str]
    """The AI model identifier used for this completion.

    Should match the exact model name from your AI provider (e.g., 'gpt-4',
    'claude-3-opus-20240229', 'gemini-pro'). This is used for cost calculation,
    performance analytics, and model comparison reporting in Revenium. Valid model
    names in Revenium for proper cost estimate can be verified using the
    sources/ai/models endpoint.
    """

    output_token_count: Required[Annotated[int, PropertyInfo(alias="outputTokenCount")]]
    """The count of consumed output tokens"""

    provider: Required[str]
    """The underlying AI provider/vendor whose model is actually processing the
    request.

    This identifies which company's AI model is being used, regardless of how you're
    accessing it (direct API, proxy, or gateway).

    Common values: 'OpenAI' (for GPT models), 'Anthropic' (for Claude models),
    'Google' (for Gemini models), 'Cohere', 'Mistral', 'Meta' (for Llama models),
    'Amazon Bedrock', 'Azure'.

    Custom values are accepted but may affect analytics categorization. Revenium
    looks up model pricing primarily by model name (e.g., 'gpt-4', 'claude-3-opus'),
    so using non-standard provider names will not break cost calculation. However,
    using standard provider names ensures proper categorization in analytics and
    reporting.

    If using an aggregation service like LiteLLM or OpenRouter, this should still be
    the actual provider (e.g., 'Anthropic' not 'LiteLLM'). If using Revenium
    middleware, this is typically auto-populated from the AI provider's API
    response. Supported provider models can be verified using the sources/ai/models
    endpoint which returns both providers and model names.
    """

    request_duration: Required[Annotated[int, PropertyInfo(alias="requestDuration")]]
    """
    The total duration of the AI completion request in milliseconds, from request
    start to completion. Calculated as (responseTime - requestTime). This includes
    network latency, AI processing time, and any mediation/gateway overhead. Used
    for performance analytics and SLA monitoring.
    """

    request_time: Required[Annotated[str, PropertyInfo(alias="requestTime")]]
    """
    The timestamp when your application sent the request to the AI provider, in ISO
    8601 format with UTC timezone (e.g., '2025-03-02T15:04:05Z'). This is used to
    calculate request duration and analyze usage patterns over time. Set this to the
    time immediately before calling the AI provider's API.
    """

    response_time: Required[Annotated[str, PropertyInfo(alias="responseTime")]]
    """
    The timestamp when the AI completion finished, in ISO 8601 format with UTC
    timezone. For streaming requests, this is when the last token was received and
    the stream closed. For non-streaming requests, this is when the complete
    response was received. Used to calculate total request duration.
    """

    stop_reason: Required[
        Annotated[
            Literal[
                "END", "END_SEQUENCE", "TIMEOUT", "TOKEN_LIMIT", "COST_LIMIT", "COMPLETION_LIMIT", "ERROR", "CANCELLED"
            ],
            PropertyInfo(alias="stopReason"),
        ]
    ]
    """The reason for stopping the completion"""

    total_token_count: Required[Annotated[int, PropertyInfo(alias="totalTokenCount")]]
    """The total number of tokens"""

    agent: str
    """The AI agent that is making the request"""

    cache_creation_token_cost: Annotated[float, PropertyInfo(alias="cacheCreationTokenCost")]
    """The cost in USD for cache creation tokens in this completion.

    Typically leave null to let Revenium automatically calculate costs based on the
    model and provider's caching pricing. Only provide a value if you have custom
    pricing agreements or want to override Revenium's cost calculation. If provided,
    this will override Revenium's automatic calculation.
    """

    cache_creation_token_count: Annotated[int, PropertyInfo(alias="cacheCreationTokenCount")]
    """The number of tokens used to create new cache entries (prompt caching).

    When you send a long prompt for the first time, the AI provider may cache it for
    faster subsequent requests. Cache creation tokens are typically billed at a
    higher rate than regular input tokens. Only include if your provider supports
    prompt caching (e.g., Anthropic Claude, OpenAI with cache-enabled models).
    Revenium's middleware will always populate this field automatically. Leave null
    otherwise.
    """

    cache_read_token_cost: Annotated[float, PropertyInfo(alias="cacheReadTokenCost")]
    """The cost in USD for cache read tokens in this completion.

    Typically leave null to let Revenium automatically calculate costs based on the
    model and provider's caching pricing. Only provide a value if you have custom
    pricing agreements or want to override Revenium's cost calculation. If provided,
    this will override Revenium's automatic calculation.
    """

    cache_read_token_count: Annotated[int, PropertyInfo(alias="cacheReadTokenCount")]
    """The number of tokens read from cache (prompt caching).

    When reusing a previously cached prompt, these tokens are read from cache
    instead of being processed as new input tokens. Cache read tokens are typically
    billed at a lower rate than regular input tokens. Only include if your provider
    supports prompt caching and reports cache hits. Revenium's middleware will
    always populate this field automatically. Leave null otherwise.
    """

    environment: str
    """Deployment environment where this AI completion was executed.

    Used for filtering and analyzing usage patterns across different deployment
    stages. Common values: 'production', 'staging', 'development', 'test'. Leave
    null if not tracking by environment.
    """

    error_reason: Annotated[str, PropertyInfo(alias="errorReason")]
    """Error message or reason if the AI completion failed.

    Include this field when the AI provider returns an error (e.g., rate limit
    exceeded, invalid API key, model not found, content policy violation). Used for
    error rate analytics and debugging. Leave null for successful completions.
    """

    input_token_cost: Annotated[float, PropertyInfo(alias="inputTokenCost")]
    """The cost in USD for input tokens in this completion.

    Typically leave null to let Revenium automatically calculate costs based on the
    model and provider's current pricing. Only provide a value if you have custom
    pricing agreements or want to override Revenium's cost calculation. Note: Manual
    cost override may not be available on all Revenium plans.
    """

    mediation_latency: Annotated[int, PropertyInfo(alias="mediationLatency")]
    """
    The latency in milliseconds introduced by intermediate systems between your
    application and the AI provider, such as API gateways, proxies, or AI mediation
    layers. This helps identify performance bottlenecks outside of the AI provider's
    processing time. Leave null if not using intermediate systems or if latency is
    not tracked separately.
    """

    middleware_source: Annotated[str, PropertyInfo(alias="middlewareSource")]
    """
    Identifier of the Revenium middleware package or SDK that captured and submitted
    this AI completion metadata. This field is AUTOMATICALLY SET by Revenium's
    middleware packages (e.g., 'revenium-openai-python', 'revenium-anthropic-node').
    You typically should NOT manually set this field. It is used for analytics to
    track which integration methods are being used and for debugging
    middleware-specific issues.
    """

    model_source: Annotated[str, PropertyInfo(alias="modelSource")]
    """The routing or aggregation layer used to access the AI model.

    This identifies whether you're calling the AI provider directly or through an
    intermediary service.

    Common values: 'DIRECT', 'LITELLM', 'OPENROUTER', 'PORTKEY', 'AZURE_OPENAI', or
    provider names ('OPENAI', 'ANTHROPIC', 'GOOGLE', etc.) when calling directly.

    Custom values are accepted for specialized routing layers or gateways. This
    field is used for integration tracking and analytics.
    """

    operation_subtype: Annotated[str, PropertyInfo(alias="operationSubtype")]
    """
    Technical classification of the specific operation or tool used within the AI
    completion. This provides finer-grained categorization than operationType.
    Examples: 'web_search', 'function_call', 'code_interpreter', 'sql_query',
    'http_request', 'file_read', 'ocr'. Used for analyzing which tools or
    capabilities are being used most frequently. Leave null for standard completions
    without tool usage.
    """

    operation_type: Annotated[
        Literal[
            "CHAT",
            "GENERATE",
            "EMBED",
            "CLASSIFY",
            "SUMMARIZE",
            "TRANSLATE",
            "OTHER",
            "TOOL_CALL",
            "RERANK",
            "SEARCH",
            "MODERATION",
            "VISION",
            "TRANSFORM",
            "GUARDRAIL",
        ],
        PropertyInfo(alias="operationType"),
    ]
    """The type of operation performed"""

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """
    Populate the ID of the subscriber’s organization from your system to allow
    Revenium to track usage & costs by company. i.e. AcmeCorp. If several
    subscriberIds have the same organizationId, Revenium’s reporting will show usage
    for the entire organization broken down by subscriberId.
    """

    output_token_cost: Annotated[float, PropertyInfo(alias="outputTokenCost")]
    """The cost in USD for output tokens in this completion.

    Typically leave null to let Revenium automatically calculate costs based on the
    model and provider's current pricing. Only provide a value if you have custom
    pricing agreements or want to override Revenium's cost calculation. If provided,
    this will override Revenium's automatic calculation. Note: Manual cost override
    may not be available on all Revenium plans.
    """

    parent_transaction_id: Annotated[str, PropertyInfo(alias="parentTransactionId")]
    """Parent transaction ID for hierarchical tracing.

    When an AI completion is part of a larger workflow or spawned by another AI
    call, this field references the parent's spanId/transactionId. Used to build
    transaction trees and understand call hierarchies in complex multi-step AI
    workflows. Leave null for root-level transactions. You can use either
    'parentSpanId' (recommended) or 'parentTransactionId'.
    """

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """
    Identifier of the product from your own system that you wish to use to correlate
    usage between Revenium & your application.
    """

    reasoning_token_count: Annotated[int, PropertyInfo(alias="reasoningTokenCount")]
    """The number of reasoning tokens used in the completion.

    Reasoning tokens are extended thinking tokens used by AI models for complex
    problem-solving. These are sometimes billed separately from regular input/output
    tokens. Only include this field if your AI provider reports reasoning tokens
    Revenium's middleware will always populate this field if reasoning tokens are
    reported by the AI provider. Leave null for models without reasoning
    capabilities.
    """

    region: str
    """Cloud region or geographic location where this AI completion was processed.

    Used for analyzing latency patterns, compliance requirements, and regional cost
    differences. Examples: 'us-east-1', 'eu-west-1', 'ap-southeast-2'. Leave null if
    not tracking by region.
    """

    response_quality_score: Annotated[float, PropertyInfo(alias="responseQualityScore")]
    """Optional quality score for the AI response on a 0.0-1.0 scale.

    Set by your application's evaluation logic (e.g., RAGAS, human feedback, custom
    scoring). Used in Revenium analytics to correlate quality with cost, model
    choice, and other metrics. Leave null if not tracking quality scores.
    """

    retry_number: Annotated[int, PropertyInfo(alias="retryNumber")]
    """Retry attempt number for this AI completion.

    0 indicates the first attempt (no retry), 1 indicates first retry, 2 indicates
    second retry, etc. Used for analyzing failure rates and retry patterns. Each
    retry attempt should be a separate transaction with incrementing retryNumber and
    the same traceId. Leave null or set to 0 for first attempts.
    """

    subscriber: Subscriber
    """Metadata about the subscriber/end-user making this AI request.

    Include this to track usage by individual users within an organization. Contains
    user identifiers and associated credential information. Leave null if not
    tracking individual user-level usage.
    """

    subscription_id: Annotated[str, PropertyInfo(alias="subscriptionId")]
    """
    Unique identifier of the subscription from your own system that you wish to use
    to correlate usage between Revenium & your application.
    """

    system_fingerprint: Annotated[str, PropertyInfo(alias="systemFingerprint")]
    """
    A unique identifier provided by the AI provider that represents the statistical
    signature of the language model that generated this completion. This fingerprint
    can be used for model attribution, debugging, and monitoring model behavior
    across requests. Automatically provided by some AI providers (e.g., OpenAI) in
    their API responses. Leave null if your provider does not supply this value.
    """

    task_type: Annotated[str, PropertyInfo(alias="taskType")]
    """Optional category to group related AI tasks for cost and performance analysis.

    Use consistent values to compare metrics across different models or vendors
    performing the same type of work. Examples: 'chat', 'summarization',
    'code-generation', 'translation', 'image-generation', 'embeddings',
    'classification', 'sentiment-analysis'. This is freeform text - choose values
    that match your use cases.
    """

    temperature: float
    """
    The temperature parameter used for this completion, controlling randomness in
    the AI's output. Typically ranges from 0.0 (deterministic) to 2.0 (very random).
    Track this to correlate temperature settings with response quality, cost, or
    other metrics. Useful for A/B testing different temperature values.
    """

    time_to_first_token: Annotated[int, PropertyInfo(alias="timeToFirstToken")]
    """The latency in milliseconds from request start to first token received.

    Calculated as (completionStartTime - requestTime). This metric is particularly
    important for streaming completions to measure perceived responsiveness. For
    non-streaming completions, this may be null or equal to requestDuration.
    """

    total_cost: Annotated[float, PropertyInfo(alias="totalCost")]
    """The total cost in USD for this completion (sum of all token costs).

    Typically leave null to let Revenium automatically calculate the total based on
    token counts and current pricing. Only provide a value if you have custom
    pricing agreements or want to override Revenium's cost calculation. If provided,
    this will override Revenium's automatic calculation.
    """

    trace_id: Annotated[str, PropertyInfo(alias="traceId")]
    """
    Optional trace identifier to group multiple related AI completion calls that
    belong to the same overall user request or workflow. For example, if a single
    user query triggers multiple LLM calls (e.g., retrieval + generation), use the
    same traceId for all calls to analyze them together in Revenium's analytics.
    Leave null for standalone completions.
    """

    trace_name: Annotated[str, PropertyInfo(alias="traceName")]
    """
    Human-readable label for individual trace instances (e.g., 'Marketing Video Q4
    2025'). Enables finding specific workflow executions. Can contain any UTF-8
    string. Max 256 characters. All transactions in the same trace must have the
    same traceName.
    """

    trace_type: Annotated[str, PropertyInfo(alias="traceType")]
    """
    Categorical identifier for grouping similar workflows (e.g., 'create_video',
    'write_script'). Enables trace-level analytics and anomaly detection within
    workflow cohorts. Must contain only alphanumeric characters, hyphens, and
    underscores. Max 128 characters. Defaults to 'uncategorized' if not provided or
    invalid. All transactions in the same trace must have the same traceType.
    """

    transaction_id: Annotated[str, PropertyInfo(alias="transactionId")]
    """Unique identifier for this specific AI completion transaction.

    Used for deduplication, correlation with request/response pairs, and transaction
    lookup in Revenium analytics. If not provided, a UUID will be auto-generated.
    For best practices, generate a UUID in your application before making the AI
    call and use the same ID when submitting to Revenium. You can use either
    'spanId' (recommended) or 'transactionId'.
    """

    transaction_name: Annotated[str, PropertyInfo(alias="transactionName")]
    """Human-readable name for this transaction.

    Provides context about what this AI completion is doing in business terms.
    Examples: 'Summarize Application', 'Credit Risk Analysis', 'Customer Support
    Response'. Used in trace visualization for better readability. Falls back to
    taskType if not provided.
    """


class SubscriberCredential(TypedDict, total=False):
    name: str
    """An alias for an API key used by one or more users.

    Used to track cost & performance by individual API keys.
    """

    value: str
    """The key value associated with the subscriber (most commonly an API key).

    Used to track cost & performance by API key value (normally used when the only
    identifier for a user is an API key).
    """


class Subscriber(TypedDict, total=False):
    id: str
    """
    Track cost & performance by individual users (if customers are anonymous or
    tracking by emails is not desired). If several subscriberIds are submitted with
    the same organizationId, Revenium’s reporting will show usage for the entire
    organization broken down by subscriberId.
    """

    credential: SubscriberCredential
    """The credential used by the subscriber"""

    email: str
    """The email address of the subscriber.

    Used to track cost & performance by individual users if customer e-mail
    addresses are known.
    """
