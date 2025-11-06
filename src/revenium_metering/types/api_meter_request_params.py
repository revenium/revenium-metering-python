# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["APIMeterRequestParams"]


class APIMeterRequestParams(TypedDict, total=False):
    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]
    """
    A client-supplied unique identifier used to correlate request and response pairs
    across /meter/v2/apis/requests and /meter/v2/apis/response endpoints. Must be
    consistent between related API calls to ensure proper usage tracking and
    analytics.
    """

    content_type: Annotated[str, PropertyInfo(alias="contentType")]
    """The content type of the request"""

    credential: str
    """The unique identifier of the credential"""

    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"]
    """The HTTP method of the request"""

    remote_host: Annotated[str, PropertyInfo(alias="remoteHost")]
    """The IP address for the origin of the request.

    Used by Revenium to report API usage by geography.
    """

    request_message_size: Annotated[int, PropertyInfo(alias="requestMessageSize")]
    """The size of the request message in bytes"""

    resource: str
    """Visible in the ‘resource’ field when viewing sources in the revenium
    application.

    The resource field (often a full URL or relative URI) can be used to auto-match
                transactions to existing sources based on the URL/URI accessed in the API call.
    """

    source_id: Annotated[str, PropertyInfo(alias="sourceId")]
    """Sources are typically individual API endpoints.

    For existing sources, the ID can be found in the Revenium platform on the
    sources page or retrieved programmatically via the list sources endpoint. A
    sourceId is created automatically for new sources.
    """

    source_type: Annotated[
        Literal[
            "UNKNOWN",
            "AI",
            "SDK_PYTHON",
            "SDK_JS",
            "SDK_JVM",
            "SDK_SPRING",
            "SDK_DOTNET",
            "SDK_GOLANG",
            "SDK_RUST",
            "EBPF",
            "AWS",
            "AZURE",
            "SNOWFLAKE",
            "KONG",
            "GRAVITEE",
            "MULESOFT",
            "BOOMI",
            "REVENIUM",
            "INTERNAL",
        ],
        PropertyInfo(alias="sourceType"),
    ]
    """Specifies the originating platform or gateway of the metered API traffic.

    This helps Revenium properly process and categorize incoming metrics according
    to their source system architecture. If not specified, defaults to 'UNKNOWN'.
    """

    user_agent: Annotated[str, PropertyInfo(alias="userAgent")]
    """The user agent of the request"""
