# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import ai_create_completion_params
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
        completion_start_time: str,
        cost_type: Literal["AI"],
        input_token_count: int,
        is_streamed: bool,
        model: str,
        output_token_count: int,
        provider: str,
        request_duration: int,
        request_time: str,
        response_time: str,
        stop_reason: Literal[
            "END", "END_SEQUENCE", "TIMEOUT", "TOKEN_LIMIT", "COST_LIMIT", "COMPLETION_LIMIT", "ERROR", "CANCELLED"
        ],
        total_token_count: int,
        transaction_id: str,
        agent: str | NotGiven = NOT_GIVEN,
        cache_creation_token_cost: float | NotGiven = NOT_GIVEN,
        cache_creation_token_count: int | NotGiven = NOT_GIVEN,
        cache_read_token_cost: float | NotGiven = NOT_GIVEN,
        cache_read_token_count: int | NotGiven = NOT_GIVEN,
        error_reason: str | NotGiven = NOT_GIVEN,
        input_token_cost: float | NotGiven = NOT_GIVEN,
        mediation_latency: int | NotGiven = NOT_GIVEN,
        middleware_source: str | NotGiven = NOT_GIVEN,
        model_source: str | NotGiven = NOT_GIVEN,
        operation_type: Literal["CHAT", "GENERATE", "EMBED", "CLASSIFY", "SUMMARIZE", "TRANSLATE", "OTHER"]
        | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        output_token_cost: float | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        reasoning_token_count: int | NotGiven = NOT_GIVEN,
        response_quality_score: float | NotGiven = NOT_GIVEN,
        subscriber: ai_create_completion_params.Subscriber | NotGiven = NOT_GIVEN,
        subscription_id: str | NotGiven = NOT_GIVEN,
        system_fingerprint: str | NotGiven = NOT_GIVEN,
        task_type: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        time_to_first_token: int | NotGiven = NOT_GIVEN,
        total_cost: float | NotGiven = NOT_GIVEN,
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
          completion_start_time: Time to first token for streaming requests

          cost_type: Cost type for the completion

          input_token_count: The count of consumed input tokens

          is_streamed: Indicates if the completion was streamed

          model: The model used for generating the LLM completion

          output_token_count: The count of consumed output tokens

          provider: Vendor providing the LLM completion service

          request_duration: The duration of the request in milliseconds

          request_time: The timestamp when the request was made

          response_time: The timestamp when the response was generated. If streaming, this is the time to
              first token

          stop_reason: The reason for stopping the completion

          total_token_count: The total number of tokens

          transaction_id: The unique identifier of the LLM completion transaction

          agent: The AI agent that is making the request

          cache_creation_token_cost: The cache creation token cost associated with the LLM completion. Note that if
              you send a valuefor this parameter in your request, it will override Revenium's
              automatic calculation of tokencost by AI model.

          cache_creation_token_count: The number of cached creation tokens in the completion

          cache_read_token_cost: The cache read token cost associated with the LLM completion. Note that if you
              send a valuefor this parameter in your request, it will override Revenium's
              automatic calculation of tokencost by AI model.

          cache_read_token_count: The number of cached read tokens in the completion

          error_reason: The details of the error that occurred during the LLM completion

          input_token_cost: The input token cost associated with the LLM completion

          mediation_latency: The latency, in milliseconds, of latency by an AI or API gateway

          middleware_source: The source middleware or SDK that generated this AI completion request

          model_source: The source of the AI model used for the completion

          operation_type: The type of operation performed

          organization_id: Populate the ID of the subscriber’s organization from your system to allow
              Revenium to track usage & costs by company. i.e. AcmeCorp. If several
              subscriberIds have the same organizationId, Revenium’s reporting will show usage
              for the entire organization broken down by subscriberId.

          output_token_cost: The output token cost associated with the LLM completion. Note that if you send
              a valuefor this parameter in your request, it will override Revenium's automatic
              calculation of tokencost by AI model. This option may not be available on all
              Revenium plans.

          product_id: Identifier of the product from your own system that you wish to use to correlate
              usage between Revenium & your application.

          reasoning_token_count: The number of reasoning tokens in the completion

          response_quality_score: The quality score of the response

          subscriber: The subscriber metadata

          subscription_id: Unique identifier of the subscription from your own system that you wish to use
              to correlate usage between Revenium & your application.

          system_fingerprint: A unique identifier that represents the statistical signature of the language
              model that generated a specific chat completion. This fingerprint can be used
              for model attribution, debugging, and monitoring model behavior across request

          task_type: If you wish to track the costs or performance of a specific task and compare the
              values over time or compare the performance across AI models or vendors, use a
              consistent taskType for all related tasks.

          temperature: The temperature setting used for the LLM completion

          time_to_first_token: The time to first token in milliseconds

          total_cost: The total cost associated with the LLM completion. Note that if you send a
              valuefor this parameter in your request, it will override Revenium's automatic
              calculation of tokencost by AI model.

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
                    "completion_start_time": completion_start_time,
                    "cost_type": cost_type,
                    "input_token_count": input_token_count,
                    "is_streamed": is_streamed,
                    "model": model,
                    "output_token_count": output_token_count,
                    "provider": provider,
                    "request_duration": request_duration,
                    "request_time": request_time,
                    "response_time": response_time,
                    "stop_reason": stop_reason,
                    "total_token_count": total_token_count,
                    "transaction_id": transaction_id,
                    "agent": agent,
                    "cache_creation_token_cost": cache_creation_token_cost,
                    "cache_creation_token_count": cache_creation_token_count,
                    "cache_read_token_cost": cache_read_token_cost,
                    "cache_read_token_count": cache_read_token_count,
                    "error_reason": error_reason,
                    "input_token_cost": input_token_cost,
                    "mediation_latency": mediation_latency,
                    "middleware_source": middleware_source,
                    "model_source": model_source,
                    "operation_type": operation_type,
                    "organization_id": organization_id,
                    "output_token_cost": output_token_cost,
                    "product_id": product_id,
                    "reasoning_token_count": reasoning_token_count,
                    "response_quality_score": response_quality_score,
                    "subscriber": subscriber,
                    "subscription_id": subscription_id,
                    "system_fingerprint": system_fingerprint,
                    "task_type": task_type,
                    "temperature": temperature,
                    "time_to_first_token": time_to_first_token,
                    "total_cost": total_cost,
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
        completion_start_time: str,
        cost_type: Literal["AI"],
        input_token_count: int,
        is_streamed: bool,
        model: str,
        output_token_count: int,
        provider: str,
        request_duration: int,
        request_time: str,
        response_time: str,
        stop_reason: Literal[
            "END", "END_SEQUENCE", "TIMEOUT", "TOKEN_LIMIT", "COST_LIMIT", "COMPLETION_LIMIT", "ERROR", "CANCELLED"
        ],
        total_token_count: int,
        transaction_id: str,
        agent: str | NotGiven = NOT_GIVEN,
        cache_creation_token_cost: float | NotGiven = NOT_GIVEN,
        cache_creation_token_count: int | NotGiven = NOT_GIVEN,
        cache_read_token_cost: float | NotGiven = NOT_GIVEN,
        cache_read_token_count: int | NotGiven = NOT_GIVEN,
        error_reason: str | NotGiven = NOT_GIVEN,
        input_token_cost: float | NotGiven = NOT_GIVEN,
        mediation_latency: int | NotGiven = NOT_GIVEN,
        middleware_source: str | NotGiven = NOT_GIVEN,
        model_source: str | NotGiven = NOT_GIVEN,
        operation_type: Literal["CHAT", "GENERATE", "EMBED", "CLASSIFY", "SUMMARIZE", "TRANSLATE", "OTHER"]
        | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        output_token_cost: float | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        reasoning_token_count: int | NotGiven = NOT_GIVEN,
        response_quality_score: float | NotGiven = NOT_GIVEN,
        subscriber: ai_create_completion_params.Subscriber | NotGiven = NOT_GIVEN,
        subscription_id: str | NotGiven = NOT_GIVEN,
        system_fingerprint: str | NotGiven = NOT_GIVEN,
        task_type: str | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        time_to_first_token: int | NotGiven = NOT_GIVEN,
        total_cost: float | NotGiven = NOT_GIVEN,
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
          completion_start_time: Time to first token for streaming requests

          cost_type: Cost type for the completion

          input_token_count: The count of consumed input tokens

          is_streamed: Indicates if the completion was streamed

          model: The model used for generating the LLM completion

          output_token_count: The count of consumed output tokens

          provider: Vendor providing the LLM completion service

          request_duration: The duration of the request in milliseconds

          request_time: The timestamp when the request was made

          response_time: The timestamp when the response was generated. If streaming, this is the time to
              first token

          stop_reason: The reason for stopping the completion

          total_token_count: The total number of tokens

          transaction_id: The unique identifier of the LLM completion transaction

          agent: The AI agent that is making the request

          cache_creation_token_cost: The cache creation token cost associated with the LLM completion. Note that if
              you send a valuefor this parameter in your request, it will override Revenium's
              automatic calculation of tokencost by AI model.

          cache_creation_token_count: The number of cached creation tokens in the completion

          cache_read_token_cost: The cache read token cost associated with the LLM completion. Note that if you
              send a valuefor this parameter in your request, it will override Revenium's
              automatic calculation of tokencost by AI model.

          cache_read_token_count: The number of cached read tokens in the completion

          error_reason: The details of the error that occurred during the LLM completion

          input_token_cost: The input token cost associated with the LLM completion

          mediation_latency: The latency, in milliseconds, of latency by an AI or API gateway

          middleware_source: The source middleware or SDK that generated this AI completion request

          model_source: The source of the AI model used for the completion

          operation_type: The type of operation performed

          organization_id: Populate the ID of the subscriber’s organization from your system to allow
              Revenium to track usage & costs by company. i.e. AcmeCorp. If several
              subscriberIds have the same organizationId, Revenium’s reporting will show usage
              for the entire organization broken down by subscriberId.

          output_token_cost: The output token cost associated with the LLM completion. Note that if you send
              a valuefor this parameter in your request, it will override Revenium's automatic
              calculation of tokencost by AI model. This option may not be available on all
              Revenium plans.

          product_id: Identifier of the product from your own system that you wish to use to correlate
              usage between Revenium & your application.

          reasoning_token_count: The number of reasoning tokens in the completion

          response_quality_score: The quality score of the response

          subscriber: The subscriber metadata

          subscription_id: Unique identifier of the subscription from your own system that you wish to use
              to correlate usage between Revenium & your application.

          system_fingerprint: A unique identifier that represents the statistical signature of the language
              model that generated a specific chat completion. This fingerprint can be used
              for model attribution, debugging, and monitoring model behavior across request

          task_type: If you wish to track the costs or performance of a specific task and compare the
              values over time or compare the performance across AI models or vendors, use a
              consistent taskType for all related tasks.

          temperature: The temperature setting used for the LLM completion

          time_to_first_token: The time to first token in milliseconds

          total_cost: The total cost associated with the LLM completion. Note that if you send a
              valuefor this parameter in your request, it will override Revenium's automatic
              calculation of tokencost by AI model.

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
                    "completion_start_time": completion_start_time,
                    "cost_type": cost_type,
                    "input_token_count": input_token_count,
                    "is_streamed": is_streamed,
                    "model": model,
                    "output_token_count": output_token_count,
                    "provider": provider,
                    "request_duration": request_duration,
                    "request_time": request_time,
                    "response_time": response_time,
                    "stop_reason": stop_reason,
                    "total_token_count": total_token_count,
                    "transaction_id": transaction_id,
                    "agent": agent,
                    "cache_creation_token_cost": cache_creation_token_cost,
                    "cache_creation_token_count": cache_creation_token_count,
                    "cache_read_token_cost": cache_read_token_cost,
                    "cache_read_token_count": cache_read_token_count,
                    "error_reason": error_reason,
                    "input_token_cost": input_token_cost,
                    "mediation_latency": mediation_latency,
                    "middleware_source": middleware_source,
                    "model_source": model_source,
                    "operation_type": operation_type,
                    "organization_id": organization_id,
                    "output_token_cost": output_token_cost,
                    "product_id": product_id,
                    "reasoning_token_count": reasoning_token_count,
                    "response_quality_score": response_quality_score,
                    "subscriber": subscriber,
                    "subscription_id": subscription_id,
                    "system_fingerprint": system_fingerprint,
                    "task_type": task_type,
                    "temperature": temperature,
                    "time_to_first_token": time_to_first_token,
                    "total_cost": total_cost,
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
