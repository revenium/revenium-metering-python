# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import event_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
        transaction_id: str,
        source_id: str | Omit = omit,
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
        | Omit = omit,
        subscriber_credential: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeteringResponseResource:
        """Submit a generic metering event with a flexible payload structure.

        Use this
        endpoint to meter custom events that you wish to track in Revenium. The payload
        should contain any key-value pairs representing metrics to track or rate for
        usage-based revenue calculation. The key values sent here will be created as
        'metering elements' if they do not already exist, and rated according to pricing
        definitions for the relevant metering element on a product if they do.

        Args:
          payload: The rating payload as a JSON object containing key-value pairs representing
              usage metrics to track. For example, a SaaS application might send: {
              "storageGB": 15.5, "apiCalls": 1250, "computeMinutes": 480 }. If these keys do
              not already exist in Revenium, each key you send will be automatically
              configured as a metering element on the relevant data source.

          transaction_id: The unique identifier of the metering event

          source_id: Optional identifier for the source that represents the feature under which usage
              charges should be tracked. In the events endpoint, sources typically represent
              categories for billable units such as features, services, or resources (e.g.,
              'storageCharges' or 'CpuCharges'). If you wish for the key value pairs you send
              to be automatically applied to a source that is used in a product to calculate
              usage-based revenue, you should specify the relevant sourceId here. Sources must
              be pre-configured in the Revenium platform. The ID can be found on the sources
              page or retrieved via the list sources endpoint.

          source_type: Specifies the originating SDK or gateway of the metered event traffic. This is
              used for Revenium analytics only, and does not affect how Revenium processes and
              categorizes incoming metrics. Optional - defaults to 'UNKNOWN' if not specified.

          subscriber_credential: Optional unique identifier for the subscriber/customer associated with this
              usage event. This credential maps the metered usage to a specific subscription
              and its associated product pricing rules. Can be any unique identifier from your
              system (customer ID, subscription ID, API key, etc.) that you've configured as a
              subscriber credential in the Revenium platform. Visible on the subscriber
              credentials page in Revenium.

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
                    "transaction_id": transaction_id,
                    "source_id": source_id,
                    "source_type": source_type,
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
        transaction_id: str,
        source_id: str | Omit = omit,
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
        | Omit = omit,
        subscriber_credential: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeteringResponseResource:
        """Submit a generic metering event with a flexible payload structure.

        Use this
        endpoint to meter custom events that you wish to track in Revenium. The payload
        should contain any key-value pairs representing metrics to track or rate for
        usage-based revenue calculation. The key values sent here will be created as
        'metering elements' if they do not already exist, and rated according to pricing
        definitions for the relevant metering element on a product if they do.

        Args:
          payload: The rating payload as a JSON object containing key-value pairs representing
              usage metrics to track. For example, a SaaS application might send: {
              "storageGB": 15.5, "apiCalls": 1250, "computeMinutes": 480 }. If these keys do
              not already exist in Revenium, each key you send will be automatically
              configured as a metering element on the relevant data source.

          transaction_id: The unique identifier of the metering event

          source_id: Optional identifier for the source that represents the feature under which usage
              charges should be tracked. In the events endpoint, sources typically represent
              categories for billable units such as features, services, or resources (e.g.,
              'storageCharges' or 'CpuCharges'). If you wish for the key value pairs you send
              to be automatically applied to a source that is used in a product to calculate
              usage-based revenue, you should specify the relevant sourceId here. Sources must
              be pre-configured in the Revenium platform. The ID can be found on the sources
              page or retrieved via the list sources endpoint.

          source_type: Specifies the originating SDK or gateway of the metered event traffic. This is
              used for Revenium analytics only, and does not affect how Revenium processes and
              categorizes incoming metrics. Optional - defaults to 'UNKNOWN' if not specified.

          subscriber_credential: Optional unique identifier for the subscriber/customer associated with this
              usage event. This credential maps the metered usage to a specific subscription
              and its associated product pricing rules. Can be any unique identifier from your
              system (customer ID, subscription ID, API key, etc.) that you've configured as a
              subscriber credential in the Revenium platform. Visible on the subscriber
              credentials page in Revenium.

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
                    "transaction_id": transaction_id,
                    "source_id": source_id,
                    "source_type": source_type,
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
