# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
# DRAFT v6.6.1 - Image metering endpoint support (REVAI-199)

from __future__ import annotations

from typing import Dict, Any
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AICreateImageParams", "Subscriber", "SubscriberCredential", "Attributes"]


class AICreateImageParams(TypedDict, total=False):
    # Required fields
    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]
    """The unique identifier of the image generation transaction"""

    provider: Required[str]
    """Vendor providing the image generation service (e.g., FAL, OPENAI, STABILITY)"""

    model: Required[str]
    """The model used for generating the image (e.g., flux-pro, dall-e-3)"""

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
    """The reason for stopping the image generation"""

    # Billing fields - at least one required (TOP LEVEL per API spec)
    actual_image_count: Annotated[int, PropertyInfo(alias="actualImageCount")]
    """Number of images actually generated"""

    requested_image_count: Annotated[int, PropertyInfo(alias="requestedImageCount")]
    """Number of images requested"""

    # Image-specific attributes (optional metadata)
    attributes: Attributes
    """Image-specific optional metadata attributes"""

    # Optional fields - common identifiers
    model_source: Annotated[str, PropertyInfo(alias="modelSource")]
    """The source of the AI model used (e.g., FAL, OPENAI)"""

    operation_type: Annotated[
        Literal["IMAGE"],
        PropertyInfo(alias="operationType"),
    ]
    """The type of operation - always IMAGE for this endpoint"""

    operation_subtype: Annotated[str, PropertyInfo(alias="operationSubtype")]
    """Specific image operation (e.g., text_to_image, image_to_image, inpaint)"""

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
    """The quality score of the generated image"""

    error_reason: Annotated[str, PropertyInfo(alias="errorReason")]
    """The details of the error if image generation failed"""

    total_cost: Annotated[float, PropertyInfo(alias="totalCost")]
    """Override automatic cost calculation with explicit total cost"""


class Attributes(TypedDict, total=False):
    """Image-specific billing and metadata attributes"""

    image_count: Annotated[int, PropertyInfo(alias="imageCount")]
    """Number of images generated"""

    billing_unit: Annotated[str, PropertyInfo(alias="billingUnit")]
    """Billing unit type (e.g., 'images', 'megapixels', 'credits')"""

    credits_used: Annotated[int, PropertyInfo(alias="creditsUsed")]
    """Number of provider credits consumed"""

    task_type: Annotated[str, PropertyInfo(alias="taskType")]
    """Task type for analytics (e.g., TEXT_TO_IMAGE, INPAINT)"""

    width: int
    """Image width in pixels"""

    height: int
    """Image height in pixels"""

    aspect_ratio: Annotated[str, PropertyInfo(alias="aspectRatio")]
    """Aspect ratio (e.g., '1:1', '16:9')"""

    megapixels: float
    """Total megapixels generated (width * height * count / 1M)"""

    steps: int
    """Number of inference steps (for diffusion models)"""

    guidance_scale: Annotated[float, PropertyInfo(alias="guidanceScale")]
    """Guidance scale / CFG scale used"""


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
