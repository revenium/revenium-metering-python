# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import ai_create_completion_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
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

__all__ = ["AIResource", "AsyncAIResource"]


class AIResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/revenium/revenium-metering-python#accessing-raw-response-data-eg-headers
        """
        return AIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/revenium/revenium-metering-python#with_streaming_response
        """
        return AIResourceWithStreamingResponse(self)

    def create_completion(
        self,
        *,
        audio_token_count: int,
        cached_token_count: int,
        completion_start_time: str,
        completion_token_count: int,
        cost_type: Literal["AI"],
        input_token_cost: float,
        model: str,
        output_token_cost: float,
        prompt_token_count: int,
        provider: str,
        reasoning_token_count: int,
        request_duration: int,
        request_time: str,
        response_time: str,
        stop_reason: Literal[
            "END", "END_SEQUENCE", "TIMEOUT", "TOKEN_LIMIT", "COST_LIMIT", "COMPLETION_LIMIT", "ERROR"
        ],
        total_cost: float,
        total_token_count: int,
        transaction_id: str,
        agent: str | NotGiven = NOT_GIVEN,
        ai_provider_key_name: str | NotGiven = NOT_GIVEN,
        api_key: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        source_id: str | NotGiven = NOT_GIVEN,
        subscriber_identity: str | NotGiven = NOT_GIVEN,
        subscription_id: str | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        task_type: str | NotGiven = NOT_GIVEN,
        trace_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResponseResource:
        """
        Record the details of an LLM completion

        Args:
          audio_token_count: The number of audio tokens in the completion

          cached_token_count: The number of cached tokens in the completion

          completion_start_time: Time to first token for streaming requests

          completion_token_count: The number of tokens in the completion

          cost_type: Cost type for the completion

          input_token_cost: The input token cost associated with the LLM completion

          model: The model used for generating the LLM completion

          output_token_cost: The output token cost associated with the LLM completion

          prompt_token_count: The number of tokens in the prompt

          provider: Vendor providing the LLM completion service

          reasoning_token_count: The number of reasoning tokens in the completion

          request_duration: The duration of the request in milliseconds

          request_time: The timestamp when the request was made

          response_time: The timestamp when the response was generated. If streaming, this is the time to
              first token

          stop_reason: The reason for stopping the completion

          total_cost: The total cost associated with the LLM completion

          total_token_count: The total number of tokens

          transaction_id: The unique identifier of the LLM completion transaction

          agent: The AI agent that is making the request

          ai_provider_key_name: The name (not the value!) of the API key used to access the AI provider

          organization_id: Populate the ID of the subscriber’s organization from your system to allow
              Revenium to track usage & costs by company. i.e. AcmeCorp. If several
              subscriberIds have the same organizationId, Revenium’s reporting will show usage
              for the entire organization broken down by user.

          product_id: Identifier of the product from your own system that you wish to use to correlate
              usage between Revenium & your application.

          source_id: Identifier of the source to correlate usage between Revenium & your application.

          subscriber_identity: Populate the ID of the subscriber from your system to allow Revenium to track
              usage & costs for individual users. Oftentimes a subscriberId is an email
              address.

          subscription_id: Unique identifier of the subscription from your own system that you wish to use
              to correlate usage between Revenium & your application.

          task_id: Identifier of the associated task. If you wish to track the costs and
              performance for a task that occurs over several prompts, use a consistent task
              ID for all prompts included in that task.

          task_type: If you wish to track the costs or performance of a specific task and compare the
              values over time or compare the performance across AI models or vendors, use a
              consistent taskType for all related tasks.

          trace_id: Trace multiple LLM calls belonging to same overall request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/ai/completions",
            body=maybe_transform(
                {
                    "audio_token_count": audio_token_count,
                    "cached_token_count": cached_token_count,
                    "completion_start_time": completion_start_time,
                    "completion_token_count": completion_token_count,
                    "cost_type": cost_type,
                    "input_token_cost": input_token_cost,
                    "model": model,
                    "output_token_cost": output_token_cost,
                    "prompt_token_count": prompt_token_count,
                    "provider": provider,
                    "reasoning_token_count": reasoning_token_count,
                    "request_duration": request_duration,
                    "request_time": request_time,
                    "response_time": response_time,
                    "stop_reason": stop_reason,
                    "total_cost": total_cost,
                    "total_token_count": total_token_count,
                    "transaction_id": transaction_id,
                    "agent": agent,
                    "ai_provider_key_name": ai_provider_key_name,
                    "api_key": api_key,
                    "organization_id": organization_id,
                    "product_id": product_id,
                    "source_id": source_id,
                    "subscriber_identity": subscriber_identity,
                    "subscription_id": subscription_id,
                    "task_id": task_id,
                    "task_type": task_type,
                    "trace_id": trace_id,
                },
                ai_create_completion_params.AICreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeteringResponseResource,
        )


class AsyncAIResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/revenium/revenium-metering-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/revenium/revenium-metering-python#with_streaming_response
        """
        return AsyncAIResourceWithStreamingResponse(self)

    async def create_completion(
        self,
        *,
        audio_token_count: int,
        cached_token_count: int,
        completion_start_time: str,
        completion_token_count: int,
        cost_type: Literal["AI"],
        input_token_cost: float,
        model: str,
        output_token_cost: float,
        prompt_token_count: int,
        provider: str,
        reasoning_token_count: int,
        request_duration: int,
        request_time: str,
        response_time: str,
        stop_reason: Literal[
            "END", "END_SEQUENCE", "TIMEOUT", "TOKEN_LIMIT", "COST_LIMIT", "COMPLETION_LIMIT", "ERROR"
        ],
        total_cost: float,
        total_token_count: int,
        transaction_id: str,
        agent: str | NotGiven = NOT_GIVEN,
        ai_provider_key_name: str | NotGiven = NOT_GIVEN,
        api_key: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        source_id: str | NotGiven = NOT_GIVEN,
        subscriber_identity: str | NotGiven = NOT_GIVEN,
        subscription_id: str | NotGiven = NOT_GIVEN,
        task_id: str | NotGiven = NOT_GIVEN,
        task_type: str | NotGiven = NOT_GIVEN,
        trace_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResponseResource:
        """
        Record the details of an LLM completion

        Args:
          audio_token_count: The number of audio tokens in the completion

          cached_token_count: The number of cached tokens in the completion

          completion_start_time: Time to first token for streaming requests

          completion_token_count: The number of tokens in the completion

          cost_type: Cost type for the completion

          input_token_cost: The input token cost associated with the LLM completion

          model: The model used for generating the LLM completion

          output_token_cost: The output token cost associated with the LLM completion

          prompt_token_count: The number of tokens in the prompt

          provider: Vendor providing the LLM completion service

          reasoning_token_count: The number of reasoning tokens in the completion

          request_duration: The duration of the request in milliseconds

          request_time: The timestamp when the request was made

          response_time: The timestamp when the response was generated. If streaming, this is the time to
              first token

          stop_reason: The reason for stopping the completion

          total_cost: The total cost associated with the LLM completion

          total_token_count: The total number of tokens

          transaction_id: The unique identifier of the LLM completion transaction

          agent: The AI agent that is making the request

          ai_provider_key_name: The name (not the value!) of the API key used to access the AI provider

          organization_id: Populate the ID of the subscriber’s organization from your system to allow
              Revenium to track usage & costs by company. i.e. AcmeCorp. If several
              subscriberIds have the same organizationId, Revenium’s reporting will show usage
              for the entire organization broken down by user.

          product_id: Identifier of the product from your own system that you wish to use to correlate
              usage between Revenium & your application.

          source_id: Identifier of the source to correlate usage between Revenium & your application.

          subscriber_identity: Populate the ID of the subscriber from your system to allow Revenium to track
              usage & costs for individual users. Oftentimes a subscriberId is an email
              address.

          subscription_id: Unique identifier of the subscription from your own system that you wish to use
              to correlate usage between Revenium & your application.

          task_id: Identifier of the associated task. If you wish to track the costs and
              performance for a task that occurs over several prompts, use a consistent task
              ID for all prompts included in that task.

          task_type: If you wish to track the costs or performance of a specific task and compare the
              values over time or compare the performance across AI models or vendors, use a
              consistent taskType for all related tasks.

          trace_id: Trace multiple LLM calls belonging to same overall request

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/ai/completions",
            body=await async_maybe_transform(
                {
                    "audio_token_count": audio_token_count,
                    "cached_token_count": cached_token_count,
                    "completion_start_time": completion_start_time,
                    "completion_token_count": completion_token_count,
                    "cost_type": cost_type,
                    "input_token_cost": input_token_cost,
                    "model": model,
                    "output_token_cost": output_token_cost,
                    "prompt_token_count": prompt_token_count,
                    "provider": provider,
                    "reasoning_token_count": reasoning_token_count,
                    "request_duration": request_duration,
                    "request_time": request_time,
                    "response_time": response_time,
                    "stop_reason": stop_reason,
                    "total_cost": total_cost,
                    "total_token_count": total_token_count,
                    "transaction_id": transaction_id,
                    "agent": agent,
                    "ai_provider_key_name": ai_provider_key_name,
                    "api_key": api_key,
                    "organization_id": organization_id,
                    "product_id": product_id,
                    "source_id": source_id,
                    "subscriber_identity": subscriber_identity,
                    "subscription_id": subscription_id,
                    "task_id": task_id,
                    "task_type": task_type,
                    "trace_id": trace_id,
                },
                ai_create_completion_params.AICreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeteringResponseResource,
        )


class AIResourceWithRawResponse:
    def __init__(self, ai: AIResource) -> None:
        self._ai = ai

        self.create_completion = to_raw_response_wrapper(
            ai.create_completion,
        )


class AsyncAIResourceWithRawResponse:
    def __init__(self, ai: AsyncAIResource) -> None:
        self._ai = ai

        self.create_completion = async_to_raw_response_wrapper(
            ai.create_completion,
        )


class AIResourceWithStreamingResponse:
    def __init__(self, ai: AIResource) -> None:
        self._ai = ai

        self.create_completion = to_streamed_response_wrapper(
            ai.create_completion,
        )


class AsyncAIResourceWithStreamingResponse:
    def __init__(self, ai: AsyncAIResource) -> None:
        self._ai = ai

        self.create_completion = async_to_streamed_response_wrapper(
            ai.create_completion,
        )
