# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import api_meter_request_params, api_meter_response_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.metering_response_resource import MeteringResponseResource

__all__ = ["APIsResource", "AsyncAPIsResource"]


class APIsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/revenium/revenium-metering-python#accessing-raw-response-data-eg-headers
        """
        return APIsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/revenium/revenium-metering-python#with_streaming_response
        """
        return APIsResourceWithStreamingResponse(self)

    def meter_request(
        self,
        *,
        transaction_id: str,
        content_type: str | NotGiven = NOT_GIVEN,
        credential: str | NotGiven = NOT_GIVEN,
        method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"] | NotGiven = NOT_GIVEN,
        remote_host: str | NotGiven = NOT_GIVEN,
        request_message_size: int | NotGiven = NOT_GIVEN,
        resource: str | NotGiven = NOT_GIVEN,
        source_id: str | NotGiven = NOT_GIVEN,
        source_type: Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
        user_agent: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResponseResource:
        """
        Meter an API request

        Args:
          transaction_id: A client-supplied unique identifier used to correlate request and response pairs
              across /meter/v2/apis/requests and /meter/v2/apis/response endpoints. Must be
              consistent between related API calls to ensure proper usage tracking and
              analytics.

          content_type: The content type of the request

          credential: The unique identifier of the credential

          method: The HTTP method of the request

          remote_host: The IP address for the origin of the request. Used by Revenium to report API
              usage by geography.

          request_message_size: The size of the request message in bytes

          resource: Visible in the ‘resource’ field when viewing sources in the revenium application.
                          The resource field (often a full URL or relative URI) can be used to auto-match
                          transactions to existing sources based on the URL/URI accessed in the API call.

          source_id: Sources are typically individual API endpoints. For existing sources, the ID can
              be found in the Revenium platform on the sources page or retrieved
              programmatically via the list sources endpoint. A sourceId is created
              automatically for new sources.

          source_type: Specifies the originating platform or gateway of the metered API traffic. This
              helps Revenium properly process and categorize incoming metrics according to
              their source system architecture. If not specified, defaults to 'UNKNOWN'.

          user_agent: The user agent of the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/apis/requests",
            body=maybe_transform(
                {
                    "transaction_id": transaction_id,
                    "content_type": content_type,
                    "credential": credential,
                    "method": method,
                    "remote_host": remote_host,
                    "request_message_size": request_message_size,
                    "resource": resource,
                    "source_id": source_id,
                    "source_type": source_type,
                    "user_agent": user_agent,
                },
                api_meter_request_params.APIMeterRequestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeteringResponseResource,
        )

    def meter_response(
        self,
        *,
        response_code: int,
        transaction_id: str,
        backend_latency: float | NotGiven = NOT_GIVEN,
        content_type: str | NotGiven = NOT_GIVEN,
        gateway_latency: float | NotGiven = NOT_GIVEN,
        response_message_size: int | NotGiven = NOT_GIVEN,
        total_duration: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResponseResource:
        """
        Meter an API response

        Args:
          response_code: The HTTP status code of the response

          transaction_id: A client-supplied unique identifier used to correlate request and response pairs
              across /meter/v2/apis/requests and /meter/v2/apis/response endpoints. Must be
              consistent between related API calls to ensure proper usage tracking and
              analytics.

          backend_latency: The latency introduced by backend services in milliseconds

          content_type: The content type of the request

          gateway_latency: The latency introduced by the gateway in milliseconds

          response_message_size: The size of the response message in bytes

          total_duration: The total duration of the request processing in milliseconds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/apis/responses",
            body=maybe_transform(
                {
                    "response_code": response_code,
                    "transaction_id": transaction_id,
                    "backend_latency": backend_latency,
                    "content_type": content_type,
                    "gateway_latency": gateway_latency,
                    "response_message_size": response_message_size,
                    "total_duration": total_duration,
                },
                api_meter_response_params.APIMeterResponseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeteringResponseResource,
        )


class AsyncAPIsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/revenium/revenium-metering-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/revenium/revenium-metering-python#with_streaming_response
        """
        return AsyncAPIsResourceWithStreamingResponse(self)

    async def meter_request(
        self,
        *,
        transaction_id: str,
        content_type: str | NotGiven = NOT_GIVEN,
        credential: str | NotGiven = NOT_GIVEN,
        method: Literal["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"] | NotGiven = NOT_GIVEN,
        remote_host: str | NotGiven = NOT_GIVEN,
        request_message_size: int | NotGiven = NOT_GIVEN,
        resource: str | NotGiven = NOT_GIVEN,
        source_id: str | NotGiven = NOT_GIVEN,
        source_type: Literal[
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
        ]
        | NotGiven = NOT_GIVEN,
        user_agent: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResponseResource:
        """
        Meter an API request

        Args:
          transaction_id: A client-supplied unique identifier used to correlate request and response pairs
              across /meter/v2/apis/requests and /meter/v2/apis/response endpoints. Must be
              consistent between related API calls to ensure proper usage tracking and
              analytics.

          content_type: The content type of the request

          credential: The unique identifier of the credential

          method: The HTTP method of the request

          remote_host: The IP address for the origin of the request. Used by Revenium to report API
              usage by geography.

          request_message_size: The size of the request message in bytes

          resource: Visible in the ‘resource’ field when viewing sources in the revenium application.
                          The resource field (often a full URL or relative URI) can be used to auto-match
                          transactions to existing sources based on the URL/URI accessed in the API call.

          source_id: Sources are typically individual API endpoints. For existing sources, the ID can
              be found in the Revenium platform on the sources page or retrieved
              programmatically via the list sources endpoint. A sourceId is created
              automatically for new sources.

          source_type: Specifies the originating platform or gateway of the metered API traffic. This
              helps Revenium properly process and categorize incoming metrics according to
              their source system architecture. If not specified, defaults to 'UNKNOWN'.

          user_agent: The user agent of the request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/apis/requests",
            body=await async_maybe_transform(
                {
                    "transaction_id": transaction_id,
                    "content_type": content_type,
                    "credential": credential,
                    "method": method,
                    "remote_host": remote_host,
                    "request_message_size": request_message_size,
                    "resource": resource,
                    "source_id": source_id,
                    "source_type": source_type,
                    "user_agent": user_agent,
                },
                api_meter_request_params.APIMeterRequestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeteringResponseResource,
        )

    async def meter_response(
        self,
        *,
        response_code: int,
        transaction_id: str,
        backend_latency: float | NotGiven = NOT_GIVEN,
        content_type: str | NotGiven = NOT_GIVEN,
        gateway_latency: float | NotGiven = NOT_GIVEN,
        response_message_size: int | NotGiven = NOT_GIVEN,
        total_duration: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResponseResource:
        """
        Meter an API response

        Args:
          response_code: The HTTP status code of the response

          transaction_id: A client-supplied unique identifier used to correlate request and response pairs
              across /meter/v2/apis/requests and /meter/v2/apis/response endpoints. Must be
              consistent between related API calls to ensure proper usage tracking and
              analytics.

          backend_latency: The latency introduced by backend services in milliseconds

          content_type: The content type of the request

          gateway_latency: The latency introduced by the gateway in milliseconds

          response_message_size: The size of the response message in bytes

          total_duration: The total duration of the request processing in milliseconds

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/apis/responses",
            body=await async_maybe_transform(
                {
                    "response_code": response_code,
                    "transaction_id": transaction_id,
                    "backend_latency": backend_latency,
                    "content_type": content_type,
                    "gateway_latency": gateway_latency,
                    "response_message_size": response_message_size,
                    "total_duration": total_duration,
                },
                api_meter_response_params.APIMeterResponseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeteringResponseResource,
        )


class APIsResourceWithRawResponse:
    def __init__(self, apis: APIsResource) -> None:
        self._apis = apis

        self.meter_request = to_raw_response_wrapper(
            apis.meter_request,
        )
        self.meter_response = to_raw_response_wrapper(
            apis.meter_response,
        )


class AsyncAPIsResourceWithRawResponse:
    def __init__(self, apis: AsyncAPIsResource) -> None:
        self._apis = apis

        self.meter_request = async_to_raw_response_wrapper(
            apis.meter_request,
        )
        self.meter_response = async_to_raw_response_wrapper(
            apis.meter_response,
        )


class APIsResourceWithStreamingResponse:
    def __init__(self, apis: APIsResource) -> None:
        self._apis = apis

        self.meter_request = to_streamed_response_wrapper(
            apis.meter_request,
        )
        self.meter_response = to_streamed_response_wrapper(
            apis.meter_response,
        )


class AsyncAPIsResourceWithStreamingResponse:
    def __init__(self, apis: AsyncAPIsResource) -> None:
        self._apis = apis

        self.meter_request = async_to_streamed_response_wrapper(
            apis.meter_request,
        )
        self.meter_response = async_to_streamed_response_wrapper(
            apis.meter_response,
        )
