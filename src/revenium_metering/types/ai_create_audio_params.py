# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
# DRAFT v6.6.1 - Audio metering endpoint support (REVAI-199)

from __future__ import annotations

from typing import Dict, Any
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AICreateAudioParams", "Subscriber", "SubscriberCredential", "Attributes"]


class AICreateAudioParams(TypedDict, total=False):
    # Required fields
    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]
    """The unique identifier of the audio transaction"""

    provider: Required[str]
    """Vendor providing the audio service (e.g., OPENAI, ELEVENLABS, GOOGLE)"""

    model: Required[str]
    """The model used for audio processing (e.g., whisper-1, tts-1-hd)"""

    request_time: Required[Annotated[str, PropertyInfo(alias="requestTime")]]
    """The timestamp when the request was made (ISO 8601)"""

    response_time: Required[Annotated[str, PropertyInfo(alias="responseTime")]]
    """The timestamp when the response was generated (ISO 8601)"""

    request_duration: Required[Annotated[int, PropertyInfo(alias="requestDuration")]]
    """The duration of the request in milliseconds"""

    stop_reason: Required[
        Annotated[
            Literal["END", "ERROR", "TIMEOUT", "CANCELLED"],
            PropertyInfo(alias="stopReason"),
        ]
    ]
    """The reason for stopping the audio processing"""

    # Billing fields - at least one required (TOP LEVEL per API spec)
    duration_seconds: Annotated[float, PropertyInfo(alias="durationSeconds")]
    """Audio duration in seconds - for transcription billing"""

    character_count: Annotated[int, PropertyInfo(alias="characterCount")]
    """Number of characters - for TTS billing"""

    input_audio_token_count: Annotated[int, PropertyInfo(alias="inputAudioTokenCount")]
    """Input audio tokens - for realtime API billing"""

    output_audio_token_count: Annotated[int, PropertyInfo(alias="outputAudioTokenCount")]
    """Output audio tokens - for realtime API billing"""

    # Audio-specific attributes (optional metadata)
    attributes: Attributes
    """Audio-specific optional metadata attributes"""

    # Optional fields - common identifiers
    model_source: Annotated[str, PropertyInfo(alias="modelSource")]
    """The source of the AI model used (e.g., OPENAI, GOOGLE)"""

    operation_type: Annotated[
        Literal["AUDIO"],
        PropertyInfo(alias="operationType"),
    ]
    """The type of operation - always AUDIO for this endpoint"""

    operation_subtype: Annotated[str, PropertyInfo(alias="operationSubtype")]
    """Specific audio operation (e.g., transcription, tts, translation)"""

    middleware_source: Annotated[str, PropertyInfo(alias="middlewareSource")]
    """The source middleware or SDK that generated this request"""

    # Billing identity fields
    agent: str
    """The AI agent that is making the request"""

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """The organization ID for billing attribution"""

    product_id: Annotated[str, PropertyInfo(alias="productId")]
    """Product identifier for usage correlation"""

    subscription_id: Annotated[str, PropertyInfo(alias="subscriptionId")]
    """Subscription identifier for usage correlation"""

    subscriber: Subscriber
    """The subscriber metadata"""

    # Trace visualization fields
    trace_id: Annotated[str, PropertyInfo(alias="traceId")]
    """Trace multiple calls belonging to same overall request"""

    environment: str
    """Deployment environment identifier (e.g., 'production', 'staging')"""

    parent_transaction_id: Annotated[str, PropertyInfo(alias="parentTransactionId")]
    """Link to parent transaction for distributed tracing"""

    transaction_name: Annotated[str, PropertyInfo(alias="transactionName")]
    """Human-friendly name for this operation"""

    region: str
    """Cloud region or data center (e.g., 'us-east-1')"""

    credential_alias: Annotated[str, PropertyInfo(alias="credentialAlias")]
    """Human-readable name for the API key being used"""

    trace_type: Annotated[str, PropertyInfo(alias="traceType")]
    """Categorical identifier for grouping workflows"""

    trace_name: Annotated[str, PropertyInfo(alias="traceName")]
    """Human-readable label for this trace instance"""

    retry_number: Annotated[int, PropertyInfo(alias="retryNumber")]
    """Retry attempt counter (0 for first attempt)"""

    # Quality metrics
    response_quality_score: Annotated[float, PropertyInfo(alias="responseQualityScore")]
    """The quality score of the audio output"""

    error_reason: Annotated[str, PropertyInfo(alias="errorReason")]
    """The details of the error if audio processing failed"""

    total_cost: Annotated[float, PropertyInfo(alias="totalCost")]
    """Override automatic cost calculation with explicit total cost"""


class Attributes(TypedDict, total=False):
    """Audio-specific billing and metadata attributes"""

    duration: float
    """Audio duration in seconds - primary billing metric for transcription"""

    duration_unit: Annotated[str, PropertyInfo(alias="durationUnit")]
    """Unit for duration (e.g., 'seconds', 'minutes')"""

    character_count: Annotated[int, PropertyInfo(alias="characterCount")]
    """Number of characters - primary billing metric for TTS"""

    billing_unit: Annotated[str, PropertyInfo(alias="billingUnit")]
    """Billing unit type (e.g., 'seconds', 'characters', 'minutes')"""

    credits_used: Annotated[int, PropertyInfo(alias="creditsUsed")]
    """Number of provider credits consumed"""

    task_type: Annotated[str, PropertyInfo(alias="taskType")]
    """Task type for analytics (e.g., TRANSCRIPTION, TTS, TRANSLATION)"""

    sample_rate: Annotated[int, PropertyInfo(alias="sampleRate")]
    """Audio sample rate in Hz"""

    channels: int
    """Number of audio channels"""

    format: str
    """Audio format (e.g., 'mp3', 'wav', 'opus')"""

    language: str
    """Language code (e.g., 'en', 'es', 'fr')"""

    word_count: Annotated[int, PropertyInfo(alias="wordCount")]
    """Number of words in transcription output"""


class SubscriberCredential(TypedDict, total=False):
    name: str
    """An alias for an API key used by one or more users."""

    value: str
    """The key value associated with the subscriber."""


class Subscriber(TypedDict, total=False):
    id: str
    """Track cost & performance by individual users."""

    credential: SubscriberCredential
    """The credential used by the subscriber"""

    email: str
    """The email address of the subscriber."""
