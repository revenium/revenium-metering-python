# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import event_create_params
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

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/revenium/revenium-metering-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/revenium/revenium-metering-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        payload: Dict[str, object],
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
        ],
        transaction_id: str,
        source_id: str | NotGiven = NOT_GIVEN,
        subscriber_credential: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResponseResource:
        """Meter an event

        Args:
          payload: The rating payload as a JSON object.

        For example, if you are sending key value
              pairs of 'requestTokens' and 'responseTokens' with values of '1' and '2'
              respectively, the payload would be { "requestTokens": "1", "responseTokens":
              "2"}. If these keys do not already exist in Revenium, each key you send will be
              configured as a metering element on the relevant data source.

          source_type: the source type

          transaction_id: The unique identifier of the metering event

          source_id: the sourceId

          subscriber_credential: The unique identifier of the credential

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/events",
            body=maybe_transform(
                {
                    "payload": payload,
                    "source_type": source_type,
                    "transaction_id": transaction_id,
                    "source_id": source_id,
                    "subscriber_credential": subscriber_credential,
                },
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeteringResponseResource,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/revenium/revenium-metering-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/revenium/revenium-metering-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        payload: Dict[str, object],
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
        ],
        transaction_id: str,
        source_id: str | NotGiven = NOT_GIVEN,
        subscriber_credential: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResponseResource:
        """Meter an event

        Args:
          payload: The rating payload as a JSON object.

        For example, if you are sending key value
              pairs of 'requestTokens' and 'responseTokens' with values of '1' and '2'
              respectively, the payload would be { "requestTokens": "1", "responseTokens":
              "2"}. If these keys do not already exist in Revenium, each key you send will be
              configured as a metering element on the relevant data source.

          source_type: the source type

          transaction_id: The unique identifier of the metering event

          source_id: the sourceId

          subscriber_credential: The unique identifier of the credential

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/events",
            body=await async_maybe_transform(
                {
                    "payload": payload,
                    "source_type": source_type,
                    "transaction_id": transaction_id,
                    "source_id": source_id,
                    "subscriber_credential": subscriber_credential,
                },
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeteringResponseResource,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create = to_raw_response_wrapper(
            events.create,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create = async_to_raw_response_wrapper(
            events.create,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create = to_streamed_response_wrapper(
            events.create,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create = async_to_streamed_response_wrapper(
            events.create,
        )
