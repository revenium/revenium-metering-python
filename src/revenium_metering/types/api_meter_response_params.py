# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["APIMeterResponseParams"]


class APIMeterResponseParams(TypedDict, total=False):
    response_code: Required[Annotated[int, PropertyInfo(alias="responseCode")]]
    """The HTTP status code of the response"""

    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]
    """
    A client-supplied unique identifier used to correlate request and response pairs
    across /meter/v2/apis/requests and /meter/v2/apis/response endpoints. Must be
    consistent between related API calls to ensure proper usage tracking and
    analytics.
    """

    backend_latency: Annotated[float, PropertyInfo(alias="backendLatency")]
    """The latency introduced by backend services in milliseconds"""

    content_type: Annotated[str, PropertyInfo(alias="contentType")]
    """The content type of the request"""

    gateway_latency: Annotated[float, PropertyInfo(alias="gatewayLatency")]
    """The latency introduced by the gateway in milliseconds"""

    response_message_size: Annotated[int, PropertyInfo(alias="responseMessageSize")]
    """The size of the response message in bytes"""

    total_duration: Annotated[int, PropertyInfo(alias="totalDuration")]
    """The total duration of the request processing in milliseconds"""
