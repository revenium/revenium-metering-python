# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import ai_create_audio_params, ai_create_completion_params, ai_create_image_params, ai_create_video_params
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
        operation_type: Literal["CHAT", "GENERATE", "EMBED", "CLASSIFY", "SUMMARIZE", "TRANSLATE", "TOOL_CALL", "RERANK", "SEARCH", "MODERATION", "VISION", "TRANSFORM", "GUARDRAIL", "OTHER"]
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
        credential_alias: str | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        operation_subtype: str | NotGiven = NOT_GIVEN,
        parent_transaction_id: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        retry_number: int | NotGiven = NOT_GIVEN,
        trace_name: str | NotGiven = NOT_GIVEN,
        trace_type: str | NotGiven = NOT_GIVEN,
        transaction_name: str | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        input_messages: str | NotGiven = NOT_GIVEN,
        output_response: str | NotGiven = NOT_GIVEN,
        prompts_truncated: bool | NotGiven = NOT_GIVEN,
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

          credential_alias: Human-readable name for the API key being used

          environment: Deployment environment identifier (e.g., 'production', 'staging',
              'development')

          operation_subtype: Additional operation detail (e.g., 'function_call', 'sql_query')

          parent_transaction_id: Link to parent transaction for distributed tracing

          region: Cloud region or data center (e.g., 'us-east-1', 'ap-southeast-2')

          retry_number: Retry attempt counter (0 for first attempt, 1 for first retry, etc.)

          trace_name: Human-readable label for this trace instance (max 256 chars)

          trace_type: Categorical identifier for grouping workflows (alphanumeric, hyphens,
              underscores; max 128 chars)

          transaction_name: Human-friendly name for this operation

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
                    "credential_alias": credential_alias,
                    "environment": environment,
                    "operation_subtype": operation_subtype,
                    "parent_transaction_id": parent_transaction_id,
                    "region": region,
                    "retry_number": retry_number,
                    "trace_name": trace_name,
                    "trace_type": trace_type,
                    "transaction_name": transaction_name,
                    "system_prompt": system_prompt,
                    "input_messages": input_messages,
                    "output_response": output_response,
                    "prompts_truncated": prompts_truncated,
                },
                ai_create_completion_params.AICreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeteringResponseResource,
        )

    def create_audio(
        self,
        *,
        model: str,
        provider: str,
        request_duration: int,
        request_time: str,
        response_time: str,
        transaction_id: str,
        duration_seconds: float | NotGiven = NOT_GIVEN,
        character_count: int | NotGiven = NOT_GIVEN,
        input_audio_token_count: int | NotGiven = NOT_GIVEN,
        output_audio_token_count: int | NotGiven = NOT_GIVEN,
        input_token_count: int | NotGiven = NOT_GIVEN,
        output_token_count: int | NotGiven = NOT_GIVEN,
        operation_subtype: str | NotGiven = NOT_GIVEN,
        billing_unit: Literal["PER_MINUTE", "PER_CHARACTER", "PER_TOKEN"] | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        voice: str | NotGiven = NOT_GIVEN,
        audio_format: str | NotGiven = NOT_GIVEN,
        quality: str | NotGiven = NOT_GIVEN,
        speed: float | NotGiven = NOT_GIVEN,
        sample_rate: int | NotGiven = NOT_GIVEN,
        response_format: str | NotGiven = NOT_GIVEN,
        source_language: str | NotGiven = NOT_GIVEN,
        target_language: str | NotGiven = NOT_GIVEN,
        is_realtime: bool | NotGiven = NOT_GIVEN,
        total_cost: float | NotGiven = NOT_GIVEN,
        error_reason: str | NotGiven = NOT_GIVEN,
        error_code: int | NotGiven = NOT_GIVEN,
        billing_skipped: bool | NotGiven = NOT_GIVEN,
        skip_reason: Literal["FREE_TIER", "RATE_LIMITED", "ERROR_RESPONSE", "INTERNAL_TEST"] | NotGiven = NOT_GIVEN,
        subscriber: ai_create_audio_params.Subscriber | NotGiven = NOT_GIVEN,
        subscriber_email: str | NotGiven = NOT_GIVEN,
        subscriber_id: str | NotGiven = NOT_GIVEN,
        subscription_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        trace_id: str | NotGiven = NOT_GIVEN,
        trace_type: str | NotGiven = NOT_GIVEN,
        trace_name: str | NotGiven = NOT_GIVEN,
        parent_transaction_id: str | NotGiven = NOT_GIVEN,
        transaction_name: str | NotGiven = NOT_GIVEN,
        task_type: str | NotGiven = NOT_GIVEN,
        agent: str | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        retry_number: int | NotGiven = NOT_GIVEN,
        middleware_source: str | NotGiven = NOT_GIVEN,
        model_source: str | NotGiven = NOT_GIVEN,
        credential_alias: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResponseResource:
        """
        Record the details of an AI audio operation

        Args:
          model: The AI model identifier used for this audio operation

          provider: The underlying AI provider/vendor whose model is processing the request

          request_duration: The total duration of the AI audio request in milliseconds

          request_time: The timestamp when your application sent the request to the AI provider (ISO 8601 format)

          response_time: The timestamp when the AI audio operation finished (ISO 8601 format)

          transaction_id: The unique identifier of the audio transaction

          duration_seconds: Duration of the audio in seconds (required for transcription/translation operations)

          character_count: Number of characters in the text (required for TTS/speech operations)

          input_audio_token_count: Number of input audio tokens (for realtime audio operations)

          output_audio_token_count: Number of output audio tokens (for realtime audio operations)

          input_token_count: Number of input text tokens (for realtime audio operations)

          output_token_count: Number of output text tokens (for realtime audio operations)

          operation_subtype: Technical classification of the audio operation (transcription, translation, speech, tts, synthesis, realtime)

          billing_unit: How this operation should be billed

          language: Language code for the audio (e.g., 'en', 'es', 'fr')

          voice: Voice identifier for TTS operations (e.g., 'alloy', 'echo', 'fable')

          audio_format: Audio file format (e.g., 'mp3', 'wav', 'opus')

          quality: Audio quality setting (e.g., 'standard', 'hd')

          speed: Playback speed for TTS (typically 0.25 to 4.0)

          sample_rate: Audio sample rate in Hz (e.g., 16000, 44100)

          response_format: Response format for transcription (e.g., 'json', 'verbose_json', 'text', 'srt', 'vtt')

          source_language: Source language for translation operations

          target_language: Target language for translation operations

          is_realtime: Whether this is a real-time/streaming audio operation

          total_cost: The total cost in USD for this audio operation (overrides automatic calculation)

          error_reason: Error message or reason if the audio operation failed

          error_code: HTTP error code if the operation failed

          billing_skipped: If true, backend returns $0 cost

          skip_reason: Reason why billing was skipped

          subscriber: The subscriber metadata

          subscriber_email: The email address of the subscriber

          subscriber_id: Unique identifier for the subscriber

          subscription_id: Unique identifier of the subscription

          organization_id: ID of the subscriber's organization

          product_id: Identifier of the product

          trace_id: Trace multiple audio calls belonging to same overall request

          trace_type: Categorical identifier for grouping workflows

          trace_name: Human-readable label for this trace instance

          parent_transaction_id: Link to parent transaction for distributed tracing

          transaction_name: Human-friendly name for this operation

          task_type: Task type for tracking costs or performance

          agent: The AI agent that is making the request

          environment: Deployment environment identifier (e.g., 'production', 'staging', 'development')

          region: Cloud region or data center (e.g., 'us-east-1', 'ap-southeast-2')

          retry_number: Retry attempt counter (0 for first attempt, 1 for first retry, etc.)

          middleware_source: The source middleware or SDK that generated this request

          model_source: The source of the AI model used

          credential_alias: Human-readable name for the API key being used

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/ai/audio",
            body=maybe_transform(
                {
                    "model": model,
                    "provider": provider,
                    "request_duration": request_duration,
                    "request_time": request_time,
                    "response_time": response_time,
                    "transaction_id": transaction_id,
                    "duration_seconds": duration_seconds,
                    "character_count": character_count,
                    "input_audio_token_count": input_audio_token_count,
                    "output_audio_token_count": output_audio_token_count,
                    "input_token_count": input_token_count,
                    "output_token_count": output_token_count,
                    "operation_subtype": operation_subtype,
                    "billing_unit": billing_unit,
                    "language": language,
                    "voice": voice,
                    "audio_format": audio_format,
                    "quality": quality,
                    "speed": speed,
                    "sample_rate": sample_rate,
                    "response_format": response_format,
                    "source_language": source_language,
                    "target_language": target_language,
                    "is_realtime": is_realtime,
                    "total_cost": total_cost,
                    "error_reason": error_reason,
                    "error_code": error_code,
                    "billing_skipped": billing_skipped,
                    "skip_reason": skip_reason,
                    "subscriber": subscriber,
                    "subscriber_email": subscriber_email,
                    "subscriber_id": subscriber_id,
                    "subscription_id": subscription_id,
                    "organization_id": organization_id,
                    "product_id": product_id,
                    "trace_id": trace_id,
                    "trace_type": trace_type,
                    "trace_name": trace_name,
                    "parent_transaction_id": parent_transaction_id,
                    "transaction_name": transaction_name,
                    "task_type": task_type,
                    "agent": agent,
                    "environment": environment,
                    "region": region,
                    "retry_number": retry_number,
                    "middleware_source": middleware_source,
                    "model_source": model_source,
                    "credential_alias": credential_alias,
                },
                ai_create_audio_params.AICreateAudioParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeteringResponseResource,
        )

    def create_video(
        self,
        *,
        model: str,
        provider: str,
        request_duration: int,
        request_time: str,
        response_time: str,
        transaction_id: str,
        duration_seconds: float,
        credits_consumed: float | NotGiven = NOT_GIVEN,
        requested_duration_seconds: float | NotGiven = NOT_GIVEN,
        credit_rate: float | NotGiven = NOT_GIVEN,
        fps: int | NotGiven = NOT_GIVEN,
        resolution: str | NotGiven = NOT_GIVEN,
        video_job_id: str | NotGiven = NOT_GIVEN,
        async_operation: bool | NotGiven = NOT_GIVEN,
        operation_subtype: str | NotGiven = NOT_GIVEN,
        total_cost: float | NotGiven = NOT_GIVEN,
        error_reason: str | NotGiven = NOT_GIVEN,
        error_code: int | NotGiven = NOT_GIVEN,
        billing_skipped: bool | NotGiven = NOT_GIVEN,
        skip_reason: Literal["FREE_TIER", "RATE_LIMITED", "ERROR_RESPONSE", "INTERNAL_TEST"] | NotGiven = NOT_GIVEN,
        subscriber: ai_create_video_params.Subscriber | NotGiven = NOT_GIVEN,
        subscriber_email: str | NotGiven = NOT_GIVEN,
        subscriber_id: str | NotGiven = NOT_GIVEN,
        subscription_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        trace_id: str | NotGiven = NOT_GIVEN,
        trace_type: str | NotGiven = NOT_GIVEN,
        trace_name: str | NotGiven = NOT_GIVEN,
        parent_transaction_id: str | NotGiven = NOT_GIVEN,
        transaction_name: str | NotGiven = NOT_GIVEN,
        task_type: str | NotGiven = NOT_GIVEN,
        agent: str | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        retry_number: int | NotGiven = NOT_GIVEN,
        middleware_source: str | NotGiven = NOT_GIVEN,
        model_source: str | NotGiven = NOT_GIVEN,
        credential_alias: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResponseResource:
        """
        Record the details of an AI video operation

        Args:
          model: The AI model identifier used for this video operation

          provider: The underlying AI provider/vendor whose model is processing the request

          request_duration: The total duration of the AI video request in milliseconds

          request_time: The timestamp when your application sent the request to the AI provider (ISO 8601 format)

          response_time: The timestamp when the AI video operation finished (ISO 8601 format)

          transaction_id: The unique identifier of the video transaction

          duration_seconds: Duration of the generated video in seconds

          credits_consumed: Number of credits consumed for this video generation

          requested_duration_seconds: The duration requested by the user (may differ from actual duration)

          credit_rate: The rate at which credits are consumed per second

          fps: Frames per second of the generated video

          resolution: Video resolution (e.g., '1080p', '720p', '4K')

          video_job_id: Unique identifier for the video generation job

          async_operation: Whether this was an asynchronous video generation operation

          operation_subtype: Technical classification of the video operation (e.g., 'generation', 'editing')

          total_cost: The total cost in USD for this video operation (overrides automatic calculation)

          error_reason: Error message or reason if the video operation failed

          error_code: HTTP error code if the operation failed

          billing_skipped: If true, backend returns $0 cost

          skip_reason: Reason why billing was skipped

          subscriber: The subscriber metadata

          subscriber_email: The email address of the subscriber

          subscriber_id: Unique identifier for the subscriber

          subscription_id: Unique identifier of the subscription

          organization_id: ID of the subscriber's organization

          product_id: Identifier of the product

          trace_id: Trace multiple video calls belonging to same overall request

          trace_type: Categorical identifier for grouping workflows

          trace_name: Human-readable label for this trace instance

          parent_transaction_id: Link to parent transaction for distributed tracing

          transaction_name: Human-friendly name for this operation

          task_type: Task type for tracking costs or performance

          agent: The AI agent that is making the request

          environment: Deployment environment identifier (e.g., 'production', 'staging', 'development')

          region: Cloud region or data center (e.g., 'us-east-1', 'ap-southeast-2')

          retry_number: Retry attempt counter (0 for first attempt, 1 for first retry, etc.)

          middleware_source: The source middleware or SDK that generated this request

          model_source: The source of the AI model used

          credential_alias: Human-readable name for the API key being used

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/ai/video",
            body=maybe_transform(
                {
                    "model": model,
                    "provider": provider,
                    "request_duration": request_duration,
                    "request_time": request_time,
                    "response_time": response_time,
                    "transaction_id": transaction_id,
                    "duration_seconds": duration_seconds,
                    "credits_consumed": credits_consumed,
                    "requested_duration_seconds": requested_duration_seconds,
                    "credit_rate": credit_rate,
                    "fps": fps,
                    "resolution": resolution,
                    "video_job_id": video_job_id,
                    "async_operation": async_operation,
                    "operation_subtype": operation_subtype,
                    "total_cost": total_cost,
                    "error_reason": error_reason,
                    "error_code": error_code,
                    "billing_skipped": billing_skipped,
                    "skip_reason": skip_reason,
                    "subscriber": subscriber,
                    "subscriber_email": subscriber_email,
                    "subscriber_id": subscriber_id,
                    "subscription_id": subscription_id,
                    "organization_id": organization_id,
                    "product_id": product_id,
                    "trace_id": trace_id,
                    "trace_type": trace_type,
                    "trace_name": trace_name,
                    "parent_transaction_id": parent_transaction_id,
                    "transaction_name": transaction_name,
                    "task_type": task_type,
                    "agent": agent,
                    "environment": environment,
                    "region": region,
                    "retry_number": retry_number,
                    "middleware_source": middleware_source,
                    "model_source": model_source,
                    "credential_alias": credential_alias,
                },
                ai_create_video_params.AICreateVideoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeteringResponseResource,
        )

    def create_image(
        self,
        *,
        model: str,
        provider: str,
        request_duration: int,
        request_time: str,
        response_time: str,
        transaction_id: str,
        requested_image_count: int,
        actual_image_count: int,
        resolution: str | NotGiven = NOT_GIVEN,
        quality: str | NotGiven = NOT_GIVEN,
        style: str | NotGiven = NOT_GIVEN,
        format: str | NotGiven = NOT_GIVEN,
        revised_prompt_provided: bool | NotGiven = NOT_GIVEN,
        operation_subtype: str | NotGiven = NOT_GIVEN,
        total_cost: float | NotGiven = NOT_GIVEN,
        error_reason: str | NotGiven = NOT_GIVEN,
        error_code: int | NotGiven = NOT_GIVEN,
        billing_skipped: bool | NotGiven = NOT_GIVEN,
        skip_reason: Literal["FREE_TIER", "RATE_LIMITED", "ERROR_RESPONSE", "INTERNAL_TEST"] | NotGiven = NOT_GIVEN,
        subscriber: ai_create_image_params.Subscriber | NotGiven = NOT_GIVEN,
        subscriber_email: str | NotGiven = NOT_GIVEN,
        subscriber_id: str | NotGiven = NOT_GIVEN,
        subscription_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        trace_id: str | NotGiven = NOT_GIVEN,
        trace_type: str | NotGiven = NOT_GIVEN,
        trace_name: str | NotGiven = NOT_GIVEN,
        parent_transaction_id: str | NotGiven = NOT_GIVEN,
        transaction_name: str | NotGiven = NOT_GIVEN,
        task_type: str | NotGiven = NOT_GIVEN,
        agent: str | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        retry_number: int | NotGiven = NOT_GIVEN,
        middleware_source: str | NotGiven = NOT_GIVEN,
        model_source: str | NotGiven = NOT_GIVEN,
        credential_alias: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResponseResource:
        """
        Record the details of an AI image operation

        Args:
          model: The AI model identifier used for this image operation

          provider: The underlying AI provider/vendor whose model is processing the request

          request_duration: The total duration of the AI image request in milliseconds

          request_time: The timestamp when your application sent the request to the AI provider (ISO 8601 format)

          response_time: The timestamp when the AI image operation finished (ISO 8601 format)

          transaction_id: The unique identifier of the image transaction

          requested_image_count: Number of images requested by the user

          actual_image_count: Number of images actually generated

          resolution: Image resolution (e.g., '1024x1024', '1792x1024', '512x512')

          quality: Image quality setting (e.g., 'standard', 'hd')

          style: Image style (e.g., 'vivid', 'natural')

          format: Image format (e.g., 'url', 'b64_json')

          revised_prompt_provided: Whether the AI provider returned a revised/improved version of the prompt

          operation_subtype: Technical classification of the image operation (e.g., 'generation', 'edit', 'variation')

          total_cost: The total cost in USD for this image operation (overrides automatic calculation)

          error_reason: Error message or reason if the image operation failed

          error_code: HTTP error code if the operation failed

          billing_skipped: If true, backend returns $0 cost

          skip_reason: Reason why billing was skipped

          subscriber: The subscriber metadata

          subscriber_email: The email address of the subscriber

          subscriber_id: Unique identifier for the subscriber

          subscription_id: Unique identifier of the subscription

          organization_id: ID of the subscriber's organization

          product_id: Identifier of the product

          trace_id: Trace multiple image calls belonging to same overall request

          trace_type: Categorical identifier for grouping workflows

          trace_name: Human-readable label for this trace instance

          parent_transaction_id: Link to parent transaction for distributed tracing

          transaction_name: Human-friendly name for this operation

          task_type: Task type for tracking costs or performance

          agent: The AI agent that is making the request

          environment: Deployment environment identifier (e.g., 'production', 'staging', 'development')

          region: Cloud region or data center (e.g., 'us-east-1', 'ap-southeast-2')

          retry_number: Retry attempt counter (0 for first attempt, 1 for first retry, etc.)

          middleware_source: The source middleware or SDK that generated this request

          model_source: The source of the AI model used

          credential_alias: Human-readable name for the API key being used

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/ai/images",
            body=maybe_transform(
                {
                    "model": model,
                    "provider": provider,
                    "request_duration": request_duration,
                    "request_time": request_time,
                    "response_time": response_time,
                    "transaction_id": transaction_id,
                    "requested_image_count": requested_image_count,
                    "actual_image_count": actual_image_count,
                    "resolution": resolution,
                    "quality": quality,
                    "style": style,
                    "format": format,
                    "revised_prompt_provided": revised_prompt_provided,
                    "operation_subtype": operation_subtype,
                    "total_cost": total_cost,
                    "error_reason": error_reason,
                    "error_code": error_code,
                    "billing_skipped": billing_skipped,
                    "skip_reason": skip_reason,
                    "subscriber": subscriber,
                    "subscriber_email": subscriber_email,
                    "subscriber_id": subscriber_id,
                    "subscription_id": subscription_id,
                    "organization_id": organization_id,
                    "product_id": product_id,
                    "trace_id": trace_id,
                    "trace_type": trace_type,
                    "trace_name": trace_name,
                    "parent_transaction_id": parent_transaction_id,
                    "transaction_name": transaction_name,
                    "task_type": task_type,
                    "agent": agent,
                    "environment": environment,
                    "region": region,
                    "retry_number": retry_number,
                    "middleware_source": middleware_source,
                    "model_source": model_source,
                    "credential_alias": credential_alias,
                },
                ai_create_image_params.AICreateImageParams,
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
        operation_type: Literal["CHAT", "GENERATE", "EMBED", "CLASSIFY", "SUMMARIZE", "TRANSLATE", "TOOL_CALL", "RERANK", "SEARCH", "MODERATION", "VISION", "TRANSFORM", "GUARDRAIL", "OTHER"]
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
        credential_alias: str | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        operation_subtype: str | NotGiven = NOT_GIVEN,
        parent_transaction_id: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        retry_number: int | NotGiven = NOT_GIVEN,
        trace_name: str | NotGiven = NOT_GIVEN,
        trace_type: str | NotGiven = NOT_GIVEN,
        transaction_name: str | NotGiven = NOT_GIVEN,
        system_prompt: str | NotGiven = NOT_GIVEN,
        input_messages: str | NotGiven = NOT_GIVEN,
        output_response: str | NotGiven = NOT_GIVEN,
        prompts_truncated: bool | NotGiven = NOT_GIVEN,
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

          credential_alias: Human-readable name for the API key being used

          environment: Deployment environment identifier (e.g., 'production', 'staging',
              'development')

          operation_subtype: Additional operation detail (e.g., 'function_call', 'sql_query')

          parent_transaction_id: Link to parent transaction for distributed tracing

          region: Cloud region or data center (e.g., 'us-east-1', 'ap-southeast-2')

          retry_number: Retry attempt counter (0 for first attempt, 1 for first retry, etc.)

          trace_name: Human-readable label for this trace instance (max 256 chars)

          trace_type: Categorical identifier for grouping workflows (alphanumeric, hyphens,
              underscores; max 128 chars)

          transaction_name: Human-friendly name for this operation

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
                    "credential_alias": credential_alias,
                    "environment": environment,
                    "operation_subtype": operation_subtype,
                    "parent_transaction_id": parent_transaction_id,
                    "region": region,
                    "retry_number": retry_number,
                    "trace_name": trace_name,
                    "trace_type": trace_type,
                    "transaction_name": transaction_name,
                    "system_prompt": system_prompt,
                    "input_messages": input_messages,
                    "output_response": output_response,
                    "prompts_truncated": prompts_truncated,
                },
                ai_create_completion_params.AICreateCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeteringResponseResource,
        )

    async def create_audio(
        self,
        *,
        model: str,
        provider: str,
        request_duration: int,
        request_time: str,
        response_time: str,
        transaction_id: str,
        duration_seconds: float | NotGiven = NOT_GIVEN,
        character_count: int | NotGiven = NOT_GIVEN,
        input_audio_token_count: int | NotGiven = NOT_GIVEN,
        output_audio_token_count: int | NotGiven = NOT_GIVEN,
        input_token_count: int | NotGiven = NOT_GIVEN,
        output_token_count: int | NotGiven = NOT_GIVEN,
        operation_subtype: str | NotGiven = NOT_GIVEN,
        billing_unit: Literal["PER_MINUTE", "PER_CHARACTER", "PER_TOKEN"] | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        voice: str | NotGiven = NOT_GIVEN,
        audio_format: str | NotGiven = NOT_GIVEN,
        quality: str | NotGiven = NOT_GIVEN,
        speed: float | NotGiven = NOT_GIVEN,
        sample_rate: int | NotGiven = NOT_GIVEN,
        response_format: str | NotGiven = NOT_GIVEN,
        source_language: str | NotGiven = NOT_GIVEN,
        target_language: str | NotGiven = NOT_GIVEN,
        is_realtime: bool | NotGiven = NOT_GIVEN,
        total_cost: float | NotGiven = NOT_GIVEN,
        error_reason: str | NotGiven = NOT_GIVEN,
        error_code: int | NotGiven = NOT_GIVEN,
        billing_skipped: bool | NotGiven = NOT_GIVEN,
        skip_reason: Literal["FREE_TIER", "RATE_LIMITED", "ERROR_RESPONSE", "INTERNAL_TEST"] | NotGiven = NOT_GIVEN,
        subscriber: ai_create_audio_params.Subscriber | NotGiven = NOT_GIVEN,
        subscriber_email: str | NotGiven = NOT_GIVEN,
        subscriber_id: str | NotGiven = NOT_GIVEN,
        subscription_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        trace_id: str | NotGiven = NOT_GIVEN,
        trace_type: str | NotGiven = NOT_GIVEN,
        trace_name: str | NotGiven = NOT_GIVEN,
        parent_transaction_id: str | NotGiven = NOT_GIVEN,
        transaction_name: str | NotGiven = NOT_GIVEN,
        task_type: str | NotGiven = NOT_GIVEN,
        agent: str | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        retry_number: int | NotGiven = NOT_GIVEN,
        middleware_source: str | NotGiven = NOT_GIVEN,
        model_source: str | NotGiven = NOT_GIVEN,
        credential_alias: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResponseResource:
        """
        Record the details of an AI audio operation

        Args:
          model: The AI model identifier used for this audio operation

          provider: The underlying AI provider/vendor whose model is processing the request

          request_duration: The total duration of the AI audio request in milliseconds

          request_time: The timestamp when your application sent the request to the AI provider (ISO 8601 format)

          response_time: The timestamp when the AI audio operation finished (ISO 8601 format)

          transaction_id: The unique identifier of the audio transaction

          duration_seconds: Duration of the audio in seconds (required for transcription/translation operations)

          character_count: Number of characters in the text (required for TTS/speech operations)

          input_audio_token_count: Number of input audio tokens (for realtime audio operations)

          output_audio_token_count: Number of output audio tokens (for realtime audio operations)

          input_token_count: Number of input text tokens (for realtime audio operations)

          output_token_count: Number of output text tokens (for realtime audio operations)

          operation_subtype: Technical classification of the audio operation (transcription, translation, speech, tts, synthesis, realtime)

          billing_unit: How this operation should be billed

          language: Language code for the audio (e.g., 'en', 'es', 'fr')

          voice: Voice identifier for TTS operations (e.g., 'alloy', 'echo', 'fable')

          audio_format: Audio file format (e.g., 'mp3', 'wav', 'opus')

          quality: Audio quality setting (e.g., 'standard', 'hd')

          speed: Playback speed for TTS (typically 0.25 to 4.0)

          sample_rate: Audio sample rate in Hz (e.g., 16000, 44100)

          response_format: Response format for transcription (e.g., 'json', 'verbose_json', 'text', 'srt', 'vtt')

          source_language: Source language for translation operations

          target_language: Target language for translation operations

          is_realtime: Whether this is a real-time/streaming audio operation

          total_cost: The total cost in USD for this audio operation (overrides automatic calculation)

          error_reason: Error message or reason if the audio operation failed

          error_code: HTTP error code if the operation failed

          billing_skipped: If true, backend returns $0 cost

          skip_reason: Reason why billing was skipped

          subscriber: The subscriber metadata

          subscriber_email: The email address of the subscriber

          subscriber_id: Unique identifier for the subscriber

          subscription_id: Unique identifier of the subscription

          organization_id: ID of the subscriber's organization

          product_id: Identifier of the product

          trace_id: Trace multiple audio calls belonging to same overall request

          trace_type: Categorical identifier for grouping workflows

          trace_name: Human-readable label for this trace instance

          parent_transaction_id: Link to parent transaction for distributed tracing

          transaction_name: Human-friendly name for this operation

          task_type: Task type for tracking costs or performance

          agent: The AI agent that is making the request

          environment: Deployment environment identifier (e.g., 'production', 'staging', 'development')

          region: Cloud region or data center (e.g., 'us-east-1', 'ap-southeast-2')

          retry_number: Retry attempt counter (0 for first attempt, 1 for first retry, etc.)

          middleware_source: The source middleware or SDK that generated this request

          model_source: The source of the AI model used

          credential_alias: Human-readable name for the API key being used

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/ai/audio",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "provider": provider,
                    "request_duration": request_duration,
                    "request_time": request_time,
                    "response_time": response_time,
                    "transaction_id": transaction_id,
                    "duration_seconds": duration_seconds,
                    "character_count": character_count,
                    "input_audio_token_count": input_audio_token_count,
                    "output_audio_token_count": output_audio_token_count,
                    "input_token_count": input_token_count,
                    "output_token_count": output_token_count,
                    "operation_subtype": operation_subtype,
                    "billing_unit": billing_unit,
                    "language": language,
                    "voice": voice,
                    "audio_format": audio_format,
                    "quality": quality,
                    "speed": speed,
                    "sample_rate": sample_rate,
                    "response_format": response_format,
                    "source_language": source_language,
                    "target_language": target_language,
                    "is_realtime": is_realtime,
                    "total_cost": total_cost,
                    "error_reason": error_reason,
                    "error_code": error_code,
                    "billing_skipped": billing_skipped,
                    "skip_reason": skip_reason,
                    "subscriber": subscriber,
                    "subscriber_email": subscriber_email,
                    "subscriber_id": subscriber_id,
                    "subscription_id": subscription_id,
                    "organization_id": organization_id,
                    "product_id": product_id,
                    "trace_id": trace_id,
                    "trace_type": trace_type,
                    "trace_name": trace_name,
                    "parent_transaction_id": parent_transaction_id,
                    "transaction_name": transaction_name,
                    "task_type": task_type,
                    "agent": agent,
                    "environment": environment,
                    "region": region,
                    "retry_number": retry_number,
                    "middleware_source": middleware_source,
                    "model_source": model_source,
                    "credential_alias": credential_alias,
                },
                ai_create_audio_params.AICreateAudioParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeteringResponseResource,
        )

    async def create_video(
        self,
        *,
        model: str,
        provider: str,
        request_duration: int,
        request_time: str,
        response_time: str,
        transaction_id: str,
        duration_seconds: float,
        credits_consumed: float | NotGiven = NOT_GIVEN,
        requested_duration_seconds: float | NotGiven = NOT_GIVEN,
        credit_rate: float | NotGiven = NOT_GIVEN,
        fps: int | NotGiven = NOT_GIVEN,
        resolution: str | NotGiven = NOT_GIVEN,
        video_job_id: str | NotGiven = NOT_GIVEN,
        async_operation: bool | NotGiven = NOT_GIVEN,
        operation_subtype: str | NotGiven = NOT_GIVEN,
        total_cost: float | NotGiven = NOT_GIVEN,
        error_reason: str | NotGiven = NOT_GIVEN,
        error_code: int | NotGiven = NOT_GIVEN,
        billing_skipped: bool | NotGiven = NOT_GIVEN,
        skip_reason: Literal["FREE_TIER", "RATE_LIMITED", "ERROR_RESPONSE", "INTERNAL_TEST"] | NotGiven = NOT_GIVEN,
        subscriber: ai_create_video_params.Subscriber | NotGiven = NOT_GIVEN,
        subscriber_email: str | NotGiven = NOT_GIVEN,
        subscriber_id: str | NotGiven = NOT_GIVEN,
        subscription_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        trace_id: str | NotGiven = NOT_GIVEN,
        trace_type: str | NotGiven = NOT_GIVEN,
        trace_name: str | NotGiven = NOT_GIVEN,
        parent_transaction_id: str | NotGiven = NOT_GIVEN,
        transaction_name: str | NotGiven = NOT_GIVEN,
        task_type: str | NotGiven = NOT_GIVEN,
        agent: str | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        retry_number: int | NotGiven = NOT_GIVEN,
        middleware_source: str | NotGiven = NOT_GIVEN,
        model_source: str | NotGiven = NOT_GIVEN,
        credential_alias: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResponseResource:
        """
        Record the details of an AI video operation

        Args:
          model: The AI model identifier used for this video operation

          provider: The underlying AI provider/vendor whose model is processing the request

          request_duration: The total duration of the AI video request in milliseconds

          request_time: The timestamp when your application sent the request to the AI provider (ISO 8601 format)

          response_time: The timestamp when the AI video operation finished (ISO 8601 format)

          transaction_id: The unique identifier of the video transaction

          duration_seconds: Duration of the generated video in seconds

          credits_consumed: Number of credits consumed for this video generation

          requested_duration_seconds: The duration requested by the user (may differ from actual duration)

          credit_rate: The rate at which credits are consumed per second

          fps: Frames per second of the generated video

          resolution: Video resolution (e.g., '1080p', '720p', '4K')

          video_job_id: Unique identifier for the video generation job

          async_operation: Whether this was an asynchronous video generation operation

          operation_subtype: Technical classification of the video operation (e.g., 'generation', 'editing')

          total_cost: The total cost in USD for this video operation (overrides automatic calculation)

          error_reason: Error message or reason if the video operation failed

          error_code: HTTP error code if the operation failed

          billing_skipped: If true, backend returns $0 cost

          skip_reason: Reason why billing was skipped

          subscriber: The subscriber metadata

          subscriber_email: The email address of the subscriber

          subscriber_id: Unique identifier for the subscriber

          subscription_id: Unique identifier of the subscription

          organization_id: ID of the subscriber's organization

          product_id: Identifier of the product

          trace_id: Trace multiple video calls belonging to same overall request

          trace_type: Categorical identifier for grouping workflows

          trace_name: Human-readable label for this trace instance

          parent_transaction_id: Link to parent transaction for distributed tracing

          transaction_name: Human-friendly name for this operation

          task_type: Task type for tracking costs or performance

          agent: The AI agent that is making the request

          environment: Deployment environment identifier (e.g., 'production', 'staging', 'development')

          region: Cloud region or data center (e.g., 'us-east-1', 'ap-southeast-2')

          retry_number: Retry attempt counter (0 for first attempt, 1 for first retry, etc.)

          middleware_source: The source middleware or SDK that generated this request

          model_source: The source of the AI model used

          credential_alias: Human-readable name for the API key being used

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/ai/video",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "provider": provider,
                    "request_duration": request_duration,
                    "request_time": request_time,
                    "response_time": response_time,
                    "transaction_id": transaction_id,
                    "duration_seconds": duration_seconds,
                    "credits_consumed": credits_consumed,
                    "requested_duration_seconds": requested_duration_seconds,
                    "credit_rate": credit_rate,
                    "fps": fps,
                    "resolution": resolution,
                    "video_job_id": video_job_id,
                    "async_operation": async_operation,
                    "operation_subtype": operation_subtype,
                    "total_cost": total_cost,
                    "error_reason": error_reason,
                    "error_code": error_code,
                    "billing_skipped": billing_skipped,
                    "skip_reason": skip_reason,
                    "subscriber": subscriber,
                    "subscriber_email": subscriber_email,
                    "subscriber_id": subscriber_id,
                    "subscription_id": subscription_id,
                    "organization_id": organization_id,
                    "product_id": product_id,
                    "trace_id": trace_id,
                    "trace_type": trace_type,
                    "trace_name": trace_name,
                    "parent_transaction_id": parent_transaction_id,
                    "transaction_name": transaction_name,
                    "task_type": task_type,
                    "agent": agent,
                    "environment": environment,
                    "region": region,
                    "retry_number": retry_number,
                    "middleware_source": middleware_source,
                    "model_source": model_source,
                    "credential_alias": credential_alias,
                },
                ai_create_video_params.AICreateVideoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MeteringResponseResource,
        )

    async def create_image(
        self,
        *,
        model: str,
        provider: str,
        request_duration: int,
        request_time: str,
        response_time: str,
        transaction_id: str,
        requested_image_count: int,
        actual_image_count: int,
        resolution: str | NotGiven = NOT_GIVEN,
        quality: str | NotGiven = NOT_GIVEN,
        style: str | NotGiven = NOT_GIVEN,
        format: str | NotGiven = NOT_GIVEN,
        revised_prompt_provided: bool | NotGiven = NOT_GIVEN,
        operation_subtype: str | NotGiven = NOT_GIVEN,
        total_cost: float | NotGiven = NOT_GIVEN,
        error_reason: str | NotGiven = NOT_GIVEN,
        error_code: int | NotGiven = NOT_GIVEN,
        billing_skipped: bool | NotGiven = NOT_GIVEN,
        skip_reason: Literal["FREE_TIER", "RATE_LIMITED", "ERROR_RESPONSE", "INTERNAL_TEST"] | NotGiven = NOT_GIVEN,
        subscriber: ai_create_image_params.Subscriber | NotGiven = NOT_GIVEN,
        subscriber_email: str | NotGiven = NOT_GIVEN,
        subscriber_id: str | NotGiven = NOT_GIVEN,
        subscription_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        trace_id: str | NotGiven = NOT_GIVEN,
        trace_type: str | NotGiven = NOT_GIVEN,
        trace_name: str | NotGiven = NOT_GIVEN,
        parent_transaction_id: str | NotGiven = NOT_GIVEN,
        transaction_name: str | NotGiven = NOT_GIVEN,
        task_type: str | NotGiven = NOT_GIVEN,
        agent: str | NotGiven = NOT_GIVEN,
        environment: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        retry_number: int | NotGiven = NOT_GIVEN,
        middleware_source: str | NotGiven = NOT_GIVEN,
        model_source: str | NotGiven = NOT_GIVEN,
        credential_alias: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MeteringResponseResource:
        """
        Record the details of an AI image operation

        Args:
          model: The AI model identifier used for this image operation

          provider: The underlying AI provider/vendor whose model is processing the request

          request_duration: The total duration of the AI image request in milliseconds

          request_time: The timestamp when your application sent the request to the AI provider (ISO 8601 format)

          response_time: The timestamp when the AI image operation finished (ISO 8601 format)

          transaction_id: The unique identifier of the image transaction

          requested_image_count: Number of images requested by the user

          actual_image_count: Number of images actually generated

          resolution: Image resolution (e.g., '1024x1024', '1792x1024', '512x512')

          quality: Image quality setting (e.g., 'standard', 'hd')

          style: Image style (e.g., 'vivid', 'natural')

          format: Image format (e.g., 'url', 'b64_json')

          revised_prompt_provided: Whether the AI provider returned a revised/improved version of the prompt

          operation_subtype: Technical classification of the image operation (e.g., 'generation', 'edit', 'variation')

          total_cost: The total cost in USD for this image operation (overrides automatic calculation)

          error_reason: Error message or reason if the image operation failed

          error_code: HTTP error code if the operation failed

          billing_skipped: If true, backend returns $0 cost

          skip_reason: Reason why billing was skipped

          subscriber: The subscriber metadata

          subscriber_email: The email address of the subscriber

          subscriber_id: Unique identifier for the subscriber

          subscription_id: Unique identifier of the subscription

          organization_id: ID of the subscriber's organization

          product_id: Identifier of the product

          trace_id: Trace multiple image calls belonging to same overall request

          trace_type: Categorical identifier for grouping workflows

          trace_name: Human-readable label for this trace instance

          parent_transaction_id: Link to parent transaction for distributed tracing

          transaction_name: Human-friendly name for this operation

          task_type: Task type for tracking costs or performance

          agent: The AI agent that is making the request

          environment: Deployment environment identifier (e.g., 'production', 'staging', 'development')

          region: Cloud region or data center (e.g., 'us-east-1', 'ap-southeast-2')

          retry_number: Retry attempt counter (0 for first attempt, 1 for first retry, etc.)

          middleware_source: The source middleware or SDK that generated this request

          model_source: The source of the AI model used

          credential_alias: Human-readable name for the API key being used

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/ai/images",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "provider": provider,
                    "request_duration": request_duration,
                    "request_time": request_time,
                    "response_time": response_time,
                    "transaction_id": transaction_id,
                    "requested_image_count": requested_image_count,
                    "actual_image_count": actual_image_count,
                    "resolution": resolution,
                    "quality": quality,
                    "style": style,
                    "format": format,
                    "revised_prompt_provided": revised_prompt_provided,
                    "operation_subtype": operation_subtype,
                    "total_cost": total_cost,
                    "error_reason": error_reason,
                    "error_code": error_code,
                    "billing_skipped": billing_skipped,
                    "skip_reason": skip_reason,
                    "subscriber": subscriber,
                    "subscriber_email": subscriber_email,
                    "subscriber_id": subscriber_id,
                    "subscription_id": subscription_id,
                    "organization_id": organization_id,
                    "product_id": product_id,
                    "trace_id": trace_id,
                    "trace_type": trace_type,
                    "trace_name": trace_name,
                    "parent_transaction_id": parent_transaction_id,
                    "transaction_name": transaction_name,
                    "task_type": task_type,
                    "agent": agent,
                    "environment": environment,
                    "region": region,
                    "retry_number": retry_number,
                    "middleware_source": middleware_source,
                    "model_source": model_source,
                    "credential_alias": credential_alias,
                },
                ai_create_image_params.AICreateImageParams,
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
        self.create_audio = to_raw_response_wrapper(
            ai.create_audio,
        )
        self.create_video = to_raw_response_wrapper(
            ai.create_video,
        )
        self.create_image = to_raw_response_wrapper(
            ai.create_image,
        )


class AsyncAIResourceWithRawResponse:
    def __init__(self, ai: AsyncAIResource) -> None:
        self._ai = ai

        self.create_completion = async_to_raw_response_wrapper(
            ai.create_completion,
        )
        self.create_audio = async_to_raw_response_wrapper(
            ai.create_audio,
        )
        self.create_video = async_to_raw_response_wrapper(
            ai.create_video,
        )
        self.create_image = async_to_raw_response_wrapper(
            ai.create_image,
        )


class AIResourceWithStreamingResponse:
    def __init__(self, ai: AIResource) -> None:
        self._ai = ai

        self.create_completion = to_streamed_response_wrapper(
            ai.create_completion,
        )
        self.create_audio = to_streamed_response_wrapper(
            ai.create_audio,
        )
        self.create_video = to_streamed_response_wrapper(
            ai.create_video,
        )
        self.create_image = to_streamed_response_wrapper(
            ai.create_image,
        )


class AsyncAIResourceWithStreamingResponse:
    def __init__(self, ai: AsyncAIResource) -> None:
        self._ai = ai

        self.create_completion = async_to_streamed_response_wrapper(
            ai.create_completion,
        )
        self.create_audio = async_to_streamed_response_wrapper(
            ai.create_audio,
        )
        self.create_video = async_to_streamed_response_wrapper(
            ai.create_video,
        )
        self.create_image = async_to_streamed_response_wrapper(
            ai.create_image,
        )
