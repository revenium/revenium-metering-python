# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AICreateAudioParams", "Subscriber", "SubscriberCredential"]


class AICreateAudioParams(TypedDict, total=False):
    model: Required[str]
    """The AI model identifier used for this audio operation"""

    provider: Required[str]
    """The underlying AI provider/vendor whose model is processing the request"""

    request_duration: Required[Annotated[int, PropertyInfo(alias="requestDuration")]]
    """The total duration of the AI audio request in milliseconds"""

    request_time: Required[Annotated[str, PropertyInfo(alias="requestTime")]]
    """The timestamp when your application sent the request to the AI provider (ISO 8601 format)"""

    response_time: Required[Annotated[str, PropertyInfo(alias="responseTime")]]
    """The timestamp when the AI audio operation finished (ISO 8601 format)"""

    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]
    """The unique identifier of the audio transaction"""

    # Audio-specific billing fields
    duration_seconds: Annotated[float, PropertyInfo(alias="durationSeconds")]
    """Duration of the audio in seconds (required for transcription/translation operations)"""

    character_count: Annotated[int, PropertyInfo(alias="characterCount")]
    """Number of characters in the text (required for TTS/speech operations)"""

    input_audio_token_count: Annotated[int, PropertyInfo(alias="inputAudioTokenCount")]
    """Number of input audio tokens (for realtime audio operations)"""

    output_audio_token_count: Annotated[int, PropertyInfo(alias="outputAudioTokenCount")]
    """Number of output audio tokens (for realtime audio operations)"""

    input_token_count: Annotated[int, PropertyInfo(alias="inputTokenCount")]
    """Number of input text tokens (for realtime audio operations)"""

    output_token_count: Annotated[int, PropertyInfo(alias="outputTokenCount")]
    """Number of output text tokens (for realtime audio operations)"""

    # Audio metadata fields
    operation_subtype: Annotated[str, PropertyInfo(alias="operationSubtype")]
    """Technical classification of the audio operation (transcription, translation, speech, tts, synthesis, realtime)"""

    billing_unit: Annotated[Literal["PER_MINUTE", "PER_CHARACTER", "PER_TOKEN"], PropertyInfo(alias="billingUnit")]
    """How this operation should be billed"""

    language: str
    """Language code for the audio (e.g., 'en', 'es', 'fr')"""

    voice: str
    """Voice identifier for TTS operations (e.g., 'alloy', 'echo', 'fable')"""

    audio_format: Annotated[str, PropertyInfo(alias="audioFormat")]
    """Audio file format (e.g., 'mp3', 'wav', 'opus')"""

    quality: str
    """Audio quality setting (e.g., 'standard', 'hd')"""

    speed: float
    """Playback speed for TTS (typically 0.25 to 4.0)"""

    sample_rate: Annotated[int, PropertyInfo(alias="sampleRate")]
    """Audio sample rate in Hz (e.g., 16000, 44100)"""

    response_format: Annotated[str, PropertyInfo(alias="responseFormat")]
    """Response format for transcription (e.g., 'json', 'verbose_json', 'text', 'srt', 'vtt')"""

    source_language: Annotated[str, PropertyInfo(alias="sourceLanguage")]
    """Source language for translation operations"""

    target_language: Annotated[str, PropertyInfo(alias="targetLanguage")]
    """Target language for translation operations"""

    is_realtime: Annotated[bool, PropertyInfo(alias="isRealtime")]
    """Whether this is a real-time/streaming audio operation"""

    # Cost and error fields
    total_cost: Annotated[float, PropertyInfo(alias="totalCost")]
    """The total cost in USD for this audio operation (overrides automatic calculation)"""

    error_reason: Annotated[str, PropertyInfo(alias="errorReason")]
    """Error message or reason if the audio operation failed"""

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
    """Trace multiple audio calls belonging to same overall request"""

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

