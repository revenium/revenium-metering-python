# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import ai_create_completion_params
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
        agent: str | Omit = omit,
        cache_creation_token_cost: float | Omit = omit,
        cache_creation_token_count: int | Omit = omit,
        cache_read_token_cost: float | Omit = omit,
        cache_read_token_count: int | Omit = omit,
        environment: str | Omit = omit,
        error_reason: str | Omit = omit,
        input_token_cost: float | Omit = omit,
        mediation_latency: int | Omit = omit,
        middleware_source: str | Omit = omit,
        model_source: str | Omit = omit,
        operation_subtype: str | Omit = omit,
        operation_type: Literal[
            "CHAT",
            "GENERATE",
            "EMBED",
            "CLASSIFY",
            "SUMMARIZE",
            "TRANSLATE",
            "OTHER",
            "TOOL_CALL",
            "RERANK",
            "SEARCH",
            "MODERATION",
            "VISION",
            "TRANSFORM",
            "GUARDRAIL",
        ]
        | Omit = omit,
        organization_id: str | Omit = omit,
        output_token_cost: float | Omit = omit,
        parent_transaction_id: str | Omit = omit,
        product_id: str | Omit = omit,
        reasoning_token_count: int | Omit = omit,
        region: str | Omit = omit,
        response_quality_score: float | Omit = omit,
        retry_number: int | Omit = omit,
        subscriber: ai_create_completion_params.Subscriber | Omit = omit,
        subscription_id: str | Omit = omit,
        system_fingerprint: str | Omit = omit,
        task_type: str | Omit = omit,
        temperature: float | Omit = omit,
        time_to_first_token: int | Omit = omit,
        total_cost: float | Omit = omit,
        trace_id: str | Omit = omit,
        trace_name: str | Omit = omit,
        trace_type: str | Omit = omit,
        transaction_id: str | Omit = omit,
        transaction_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeteringResponseResource:
        """
        Submit AI completion metadata for metering and billing purposes.

        Args:
          completion_start_time: The timestamp when the AI completion started generating output, in ISO 8601
              format with UTC timezone. For streaming requests, this is when the first token
              was received. For non-streaming requests, this is typically the same as or very
              close to responseTime. Used to calculate time-to-first-token latency for
              streaming completions.

          cost_type: The type of cost being tracked. Currently always 'AI' for AI completion costs.
              This field is used internally by Revenium to categorize different types of
              metered usage. You typically do not need to set this field as it defaults to
              'AI'.

          input_token_count: The count of consumed input tokens

          is_streamed: Indicates whether this completion used streaming (true) or non-streaming/batch
              mode (false). Streaming completions receive tokens incrementally as they're
              generated, while non-streaming completions wait for the complete response. This
              affects how timeToFirstToken and responseTime are interpreted.

          model: The AI model identifier used for this completion. Should match the exact model
              name from your AI provider (e.g., 'gpt-4', 'claude-3-opus-20240229',
              'gemini-pro'). This is used for cost calculation, performance analytics, and
              model comparison reporting in Revenium. Valid model names in Revenium for proper
              cost estimate can be verified using the sources/ai/models endpoint.

          output_token_count: The count of consumed output tokens

          provider: The underlying AI provider/vendor whose model is actually processing the
              request. This identifies which company's AI model is being used, regardless of
              how you're accessing it (direct API, proxy, or gateway).

              Common values: 'OpenAI' (for GPT models), 'Anthropic' (for Claude models),
              'Google' (for Gemini models), 'Cohere', 'Mistral', 'Meta' (for Llama models),
              'Amazon Bedrock', 'Azure'.

              Custom values are accepted but may affect analytics categorization. Revenium
              looks up model pricing primarily by model name (e.g., 'gpt-4', 'claude-3-opus'),
              so using non-standard provider names will not break cost calculation. However,
              using standard provider names ensures proper categorization in analytics and
              reporting.

              If using an aggregation service like LiteLLM or OpenRouter, this should still be
              the actual provider (e.g., 'Anthropic' not 'LiteLLM'). If using Revenium
              middleware, this is typically auto-populated from the AI provider's API
              response. Supported provider models can be verified using the sources/ai/models
              endpoint which returns both providers and model names.

          request_duration: The total duration of the AI completion request in milliseconds, from request
              start to completion. Calculated as (responseTime - requestTime). This includes
              network latency, AI processing time, and any mediation/gateway overhead. Used
              for performance analytics and SLA monitoring.

          request_time: The timestamp when your application sent the request to the AI provider, in ISO
              8601 format with UTC timezone (e.g., '2025-03-02T15:04:05Z'). This is used to
              calculate request duration and analyze usage patterns over time. Set this to the
              time immediately before calling the AI provider's API.

          response_time: The timestamp when the AI completion finished, in ISO 8601 format with UTC
              timezone. For streaming requests, this is when the last token was received and
              the stream closed. For non-streaming requests, this is when the complete
              response was received. Used to calculate total request duration.

          stop_reason: The reason for stopping the completion

          total_token_count: The total number of tokens

          agent: The AI agent that is making the request

          cache_creation_token_cost: The cost in USD for cache creation tokens in this completion. Typically leave
              null to let Revenium automatically calculate costs based on the model and
              provider's caching pricing. Only provide a value if you have custom pricing
              agreements or want to override Revenium's cost calculation. If provided, this
              will override Revenium's automatic calculation.

          cache_creation_token_count: The number of tokens used to create new cache entries (prompt caching). When you
              send a long prompt for the first time, the AI provider may cache it for faster
              subsequent requests. Cache creation tokens are typically billed at a higher rate
              than regular input tokens. Only include if your provider supports prompt caching
              (e.g., Anthropic Claude, OpenAI with cache-enabled models). Revenium's
              middleware will always populate this field automatically. Leave null otherwise.

          cache_read_token_cost: The cost in USD for cache read tokens in this completion. Typically leave null
              to let Revenium automatically calculate costs based on the model and provider's
              caching pricing. Only provide a value if you have custom pricing agreements or
              want to override Revenium's cost calculation. If provided, this will override
              Revenium's automatic calculation.

          cache_read_token_count: The number of tokens read from cache (prompt caching). When reusing a previously
              cached prompt, these tokens are read from cache instead of being processed as
              new input tokens. Cache read tokens are typically billed at a lower rate than
              regular input tokens. Only include if your provider supports prompt caching and
              reports cache hits. Revenium's middleware will always populate this field
              automatically. Leave null otherwise.

          environment: Deployment environment where this AI completion was executed. Used for filtering
              and analyzing usage patterns across different deployment stages. Common values:
              'production', 'staging', 'development', 'test'. Leave null if not tracking by
              environment.

          error_reason: Error message or reason if the AI completion failed. Include this field when the
              AI provider returns an error (e.g., rate limit exceeded, invalid API key, model
              not found, content policy violation). Used for error rate analytics and
              debugging. Leave null for successful completions.

          input_token_cost: The cost in USD for input tokens in this completion. Typically leave null to let
              Revenium automatically calculate costs based on the model and provider's current
              pricing. Only provide a value if you have custom pricing agreements or want to
              override Revenium's cost calculation. Note: Manual cost override may not be
              available on all Revenium plans.

          mediation_latency: The latency in milliseconds introduced by intermediate systems between your
              application and the AI provider, such as API gateways, proxies, or AI mediation
              layers. This helps identify performance bottlenecks outside of the AI provider's
              processing time. Leave null if not using intermediate systems or if latency is
              not tracked separately.

          middleware_source: Identifier of the Revenium middleware package or SDK that captured and submitted
              this AI completion metadata. This field is AUTOMATICALLY SET by Revenium's
              middleware packages (e.g., 'revenium-openai-python', 'revenium-anthropic-node').
              You typically should NOT manually set this field. It is used for analytics to
              track which integration methods are being used and for debugging
              middleware-specific issues.

          model_source: The routing or aggregation layer used to access the AI model. This identifies
              whether you're calling the AI provider directly or through an intermediary
              service.

              Common values: 'DIRECT', 'LITELLM', 'OPENROUTER', 'PORTKEY', 'AZURE_OPENAI', or
              provider names ('OPENAI', 'ANTHROPIC', 'GOOGLE', etc.) when calling directly.

              Custom values are accepted for specialized routing layers or gateways. This
              field is used for integration tracking and analytics.

          operation_subtype: Technical classification of the specific operation or tool used within the AI
              completion. This provides finer-grained categorization than operationType.
              Examples: 'web_search', 'function_call', 'code_interpreter', 'sql_query',
              'http_request', 'file_read', 'ocr'. Used for analyzing which tools or
              capabilities are being used most frequently. Leave null for standard completions
              without tool usage.

          operation_type: The type of operation performed

          organization_id: Populate the ID of the subscriber’s organization from your system to allow
              Revenium to track usage & costs by company. i.e. AcmeCorp. If several
              subscriberIds have the same organizationId, Revenium’s reporting will show usage
              for the entire organization broken down by subscriberId.

          output_token_cost: The cost in USD for output tokens in this completion. Typically leave null to
              let Revenium automatically calculate costs based on the model and provider's
              current pricing. Only provide a value if you have custom pricing agreements or
              want to override Revenium's cost calculation. If provided, this will override
              Revenium's automatic calculation. Note: Manual cost override may not be
              available on all Revenium plans.

          parent_transaction_id: Parent transaction ID for hierarchical tracing. When an AI completion is part of
              a larger workflow or spawned by another AI call, this field references the
              parent's spanId/transactionId. Used to build transaction trees and understand
              call hierarchies in complex multi-step AI workflows. Leave null for root-level
              transactions. You can use either 'parentSpanId' (recommended) or
              'parentTransactionId'.

          product_id: Identifier of the product from your own system that you wish to use to correlate
              usage between Revenium & your application.

          reasoning_token_count: The number of reasoning tokens used in the completion. Reasoning tokens are
              extended thinking tokens used by AI models for complex problem-solving. These
              are sometimes billed separately from regular input/output tokens. Only include
              this field if your AI provider reports reasoning tokens Revenium's middleware
              will always populate this field if reasoning tokens are reported by the AI
              provider. Leave null for models without reasoning capabilities.

          region: Cloud region or geographic location where this AI completion was processed. Used
              for analyzing latency patterns, compliance requirements, and regional cost
              differences. Examples: 'us-east-1', 'eu-west-1', 'ap-southeast-2'. Leave null if
              not tracking by region.

          response_quality_score: Optional quality score for the AI response on a 0.0-1.0 scale. Set by your
              application's evaluation logic (e.g., RAGAS, human feedback, custom scoring).
              Used in Revenium analytics to correlate quality with cost, model choice, and
              other metrics. Leave null if not tracking quality scores.

          retry_number: Retry attempt number for this AI completion. 0 indicates the first attempt (no
              retry), 1 indicates first retry, 2 indicates second retry, etc. Used for
              analyzing failure rates and retry patterns. Each retry attempt should be a
              separate transaction with incrementing retryNumber and the same traceId. Leave
              null or set to 0 for first attempts.

          subscriber: Metadata about the subscriber/end-user making this AI request. Include this to
              track usage by individual users within an organization. Contains user
              identifiers and associated credential information. Leave null if not tracking
              individual user-level usage.

          subscription_id: Unique identifier of the subscription from your own system that you wish to use
              to correlate usage between Revenium & your application.

          system_fingerprint: A unique identifier provided by the AI provider that represents the statistical
              signature of the language model that generated this completion. This fingerprint
              can be used for model attribution, debugging, and monitoring model behavior
              across requests. Automatically provided by some AI providers (e.g., OpenAI) in
              their API responses. Leave null if your provider does not supply this value.

          task_type: Optional category to group related AI tasks for cost and performance analysis.
              Use consistent values to compare metrics across different models or vendors
              performing the same type of work. Examples: 'chat', 'summarization',
              'code-generation', 'translation', 'image-generation', 'embeddings',
              'classification', 'sentiment-analysis'. This is freeform text - choose values
              that match your use cases.

          temperature: The temperature parameter used for this completion, controlling randomness in
              the AI's output. Typically ranges from 0.0 (deterministic) to 2.0 (very random).
              Track this to correlate temperature settings with response quality, cost, or
              other metrics. Useful for A/B testing different temperature values.

          time_to_first_token: The latency in milliseconds from request start to first token received.
              Calculated as (completionStartTime - requestTime). This metric is particularly
              important for streaming completions to measure perceived responsiveness. For
              non-streaming completions, this may be null or equal to requestDuration.

          total_cost: The total cost in USD for this completion (sum of all token costs). Typically
              leave null to let Revenium automatically calculate the total based on token
              counts and current pricing. Only provide a value if you have custom pricing
              agreements or want to override Revenium's cost calculation. If provided, this
              will override Revenium's automatic calculation.

          trace_id: Optional trace identifier to group multiple related AI completion calls that
              belong to the same overall user request or workflow. For example, if a single
              user query triggers multiple LLM calls (e.g., retrieval + generation), use the
              same traceId for all calls to analyze them together in Revenium's analytics.
              Leave null for standalone completions.

          trace_name: Human-readable label for individual trace instances (e.g., 'Marketing Video Q4
              2025'). Enables finding specific workflow executions. Can contain any UTF-8
              string. Max 256 characters. All transactions in the same trace must have the
              same traceName.

          trace_type: Categorical identifier for grouping similar workflows (e.g., 'create_video',
              'write_script'). Enables trace-level analytics and anomaly detection within
              workflow cohorts. Must contain only alphanumeric characters, hyphens, and
              underscores. Max 128 characters. Defaults to 'uncategorized' if not provided or
              invalid. All transactions in the same trace must have the same traceType.

          transaction_id: Unique identifier for this specific AI completion transaction. Used for
              deduplication, correlation with request/response pairs, and transaction lookup
              in Revenium analytics. If not provided, a UUID will be auto-generated. For best
              practices, generate a UUID in your application before making the AI call and use
              the same ID when submitting to Revenium. You can use either 'spanId'
              (recommended) or 'transactionId'.

          transaction_name: Human-readable name for this transaction. Provides context about what this AI
              completion is doing in business terms. Examples: 'Summarize Application',
              'Credit Risk Analysis', 'Customer Support Response'. Used in trace visualization
              for better readability. Falls back to taskType if not provided.

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
                    "agent": agent,
                    "cache_creation_token_cost": cache_creation_token_cost,
                    "cache_creation_token_count": cache_creation_token_count,
                    "cache_read_token_cost": cache_read_token_cost,
                    "cache_read_token_count": cache_read_token_count,
                    "environment": environment,
                    "error_reason": error_reason,
                    "input_token_cost": input_token_cost,
                    "mediation_latency": mediation_latency,
                    "middleware_source": middleware_source,
                    "model_source": model_source,
                    "operation_subtype": operation_subtype,
                    "operation_type": operation_type,
                    "organization_id": organization_id,
                    "output_token_cost": output_token_cost,
                    "parent_transaction_id": parent_transaction_id,
                    "product_id": product_id,
                    "reasoning_token_count": reasoning_token_count,
                    "region": region,
                    "response_quality_score": response_quality_score,
                    "retry_number": retry_number,
                    "subscriber": subscriber,
                    "subscription_id": subscription_id,
                    "system_fingerprint": system_fingerprint,
                    "task_type": task_type,
                    "temperature": temperature,
                    "time_to_first_token": time_to_first_token,
                    "total_cost": total_cost,
                    "trace_id": trace_id,
                    "trace_name": trace_name,
                    "trace_type": trace_type,
                    "transaction_id": transaction_id,
                    "transaction_name": transaction_name,
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
        agent: str | Omit = omit,
        cache_creation_token_cost: float | Omit = omit,
        cache_creation_token_count: int | Omit = omit,
        cache_read_token_cost: float | Omit = omit,
        cache_read_token_count: int | Omit = omit,
        environment: str | Omit = omit,
        error_reason: str | Omit = omit,
        input_token_cost: float | Omit = omit,
        mediation_latency: int | Omit = omit,
        middleware_source: str | Omit = omit,
        model_source: str | Omit = omit,
        operation_subtype: str | Omit = omit,
        operation_type: Literal[
            "CHAT",
            "GENERATE",
            "EMBED",
            "CLASSIFY",
            "SUMMARIZE",
            "TRANSLATE",
            "OTHER",
            "TOOL_CALL",
            "RERANK",
            "SEARCH",
            "MODERATION",
            "VISION",
            "TRANSFORM",
            "GUARDRAIL",
        ]
        | Omit = omit,
        organization_id: str | Omit = omit,
        output_token_cost: float | Omit = omit,
        parent_transaction_id: str | Omit = omit,
        product_id: str | Omit = omit,
        reasoning_token_count: int | Omit = omit,
        region: str | Omit = omit,
        response_quality_score: float | Omit = omit,
        retry_number: int | Omit = omit,
        subscriber: ai_create_completion_params.Subscriber | Omit = omit,
        subscription_id: str | Omit = omit,
        system_fingerprint: str | Omit = omit,
        task_type: str | Omit = omit,
        temperature: float | Omit = omit,
        time_to_first_token: int | Omit = omit,
        total_cost: float | Omit = omit,
        trace_id: str | Omit = omit,
        trace_name: str | Omit = omit,
        trace_type: str | Omit = omit,
        transaction_id: str | Omit = omit,
        transaction_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MeteringResponseResource:
        """
        Submit AI completion metadata for metering and billing purposes.

        Args:
          completion_start_time: The timestamp when the AI completion started generating output, in ISO 8601
              format with UTC timezone. For streaming requests, this is when the first token
              was received. For non-streaming requests, this is typically the same as or very
              close to responseTime. Used to calculate time-to-first-token latency for
              streaming completions.

          cost_type: The type of cost being tracked. Currently always 'AI' for AI completion costs.
              This field is used internally by Revenium to categorize different types of
              metered usage. You typically do not need to set this field as it defaults to
              'AI'.

          input_token_count: The count of consumed input tokens

          is_streamed: Indicates whether this completion used streaming (true) or non-streaming/batch
              mode (false). Streaming completions receive tokens incrementally as they're
              generated, while non-streaming completions wait for the complete response. This
              affects how timeToFirstToken and responseTime are interpreted.

          model: The AI model identifier used for this completion. Should match the exact model
              name from your AI provider (e.g., 'gpt-4', 'claude-3-opus-20240229',
              'gemini-pro'). This is used for cost calculation, performance analytics, and
              model comparison reporting in Revenium. Valid model names in Revenium for proper
              cost estimate can be verified using the sources/ai/models endpoint.

          output_token_count: The count of consumed output tokens

          provider: The underlying AI provider/vendor whose model is actually processing the
              request. This identifies which company's AI model is being used, regardless of
              how you're accessing it (direct API, proxy, or gateway).

              Common values: 'OpenAI' (for GPT models), 'Anthropic' (for Claude models),
              'Google' (for Gemini models), 'Cohere', 'Mistral', 'Meta' (for Llama models),
              'Amazon Bedrock', 'Azure'.

              Custom values are accepted but may affect analytics categorization. Revenium
              looks up model pricing primarily by model name (e.g., 'gpt-4', 'claude-3-opus'),
              so using non-standard provider names will not break cost calculation. However,
              using standard provider names ensures proper categorization in analytics and
              reporting.

              If using an aggregation service like LiteLLM or OpenRouter, this should still be
              the actual provider (e.g., 'Anthropic' not 'LiteLLM'). If using Revenium
              middleware, this is typically auto-populated from the AI provider's API
              response. Supported provider models can be verified using the sources/ai/models
              endpoint which returns both providers and model names.

          request_duration: The total duration of the AI completion request in milliseconds, from request
              start to completion. Calculated as (responseTime - requestTime). This includes
              network latency, AI processing time, and any mediation/gateway overhead. Used
              for performance analytics and SLA monitoring.

          request_time: The timestamp when your application sent the request to the AI provider, in ISO
              8601 format with UTC timezone (e.g., '2025-03-02T15:04:05Z'). This is used to
              calculate request duration and analyze usage patterns over time. Set this to the
              time immediately before calling the AI provider's API.

          response_time: The timestamp when the AI completion finished, in ISO 8601 format with UTC
              timezone. For streaming requests, this is when the last token was received and
              the stream closed. For non-streaming requests, this is when the complete
              response was received. Used to calculate total request duration.

          stop_reason: The reason for stopping the completion

          total_token_count: The total number of tokens

          agent: The AI agent that is making the request

          cache_creation_token_cost: The cost in USD for cache creation tokens in this completion. Typically leave
              null to let Revenium automatically calculate costs based on the model and
              provider's caching pricing. Only provide a value if you have custom pricing
              agreements or want to override Revenium's cost calculation. If provided, this
              will override Revenium's automatic calculation.

          cache_creation_token_count: The number of tokens used to create new cache entries (prompt caching). When you
              send a long prompt for the first time, the AI provider may cache it for faster
              subsequent requests. Cache creation tokens are typically billed at a higher rate
              than regular input tokens. Only include if your provider supports prompt caching
              (e.g., Anthropic Claude, OpenAI with cache-enabled models). Revenium's
              middleware will always populate this field automatically. Leave null otherwise.

          cache_read_token_cost: The cost in USD for cache read tokens in this completion. Typically leave null
              to let Revenium automatically calculate costs based on the model and provider's
              caching pricing. Only provide a value if you have custom pricing agreements or
              want to override Revenium's cost calculation. If provided, this will override
              Revenium's automatic calculation.

          cache_read_token_count: The number of tokens read from cache (prompt caching). When reusing a previously
              cached prompt, these tokens are read from cache instead of being processed as
              new input tokens. Cache read tokens are typically billed at a lower rate than
              regular input tokens. Only include if your provider supports prompt caching and
              reports cache hits. Revenium's middleware will always populate this field
              automatically. Leave null otherwise.

          environment: Deployment environment where this AI completion was executed. Used for filtering
              and analyzing usage patterns across different deployment stages. Common values:
              'production', 'staging', 'development', 'test'. Leave null if not tracking by
              environment.

          error_reason: Error message or reason if the AI completion failed. Include this field when the
              AI provider returns an error (e.g., rate limit exceeded, invalid API key, model
              not found, content policy violation). Used for error rate analytics and
              debugging. Leave null for successful completions.

          input_token_cost: The cost in USD for input tokens in this completion. Typically leave null to let
              Revenium automatically calculate costs based on the model and provider's current
              pricing. Only provide a value if you have custom pricing agreements or want to
              override Revenium's cost calculation. Note: Manual cost override may not be
              available on all Revenium plans.

          mediation_latency: The latency in milliseconds introduced by intermediate systems between your
              application and the AI provider, such as API gateways, proxies, or AI mediation
              layers. This helps identify performance bottlenecks outside of the AI provider's
              processing time. Leave null if not using intermediate systems or if latency is
              not tracked separately.

          middleware_source: Identifier of the Revenium middleware package or SDK that captured and submitted
              this AI completion metadata. This field is AUTOMATICALLY SET by Revenium's
              middleware packages (e.g., 'revenium-openai-python', 'revenium-anthropic-node').
              You typically should NOT manually set this field. It is used for analytics to
              track which integration methods are being used and for debugging
              middleware-specific issues.

          model_source: The routing or aggregation layer used to access the AI model. This identifies
              whether you're calling the AI provider directly or through an intermediary
              service.

              Common values: 'DIRECT', 'LITELLM', 'OPENROUTER', 'PORTKEY', 'AZURE_OPENAI', or
              provider names ('OPENAI', 'ANTHROPIC', 'GOOGLE', etc.) when calling directly.

              Custom values are accepted for specialized routing layers or gateways. This
              field is used for integration tracking and analytics.

          operation_subtype: Technical classification of the specific operation or tool used within the AI
              completion. This provides finer-grained categorization than operationType.
              Examples: 'web_search', 'function_call', 'code_interpreter', 'sql_query',
              'http_request', 'file_read', 'ocr'. Used for analyzing which tools or
              capabilities are being used most frequently. Leave null for standard completions
              without tool usage.

          operation_type: The type of operation performed

          organization_id: Populate the ID of the subscriber’s organization from your system to allow
              Revenium to track usage & costs by company. i.e. AcmeCorp. If several
              subscriberIds have the same organizationId, Revenium’s reporting will show usage
              for the entire organization broken down by subscriberId.

          output_token_cost: The cost in USD for output tokens in this completion. Typically leave null to
              let Revenium automatically calculate costs based on the model and provider's
              current pricing. Only provide a value if you have custom pricing agreements or
              want to override Revenium's cost calculation. If provided, this will override
              Revenium's automatic calculation. Note: Manual cost override may not be
              available on all Revenium plans.

          parent_transaction_id: Parent transaction ID for hierarchical tracing. When an AI completion is part of
              a larger workflow or spawned by another AI call, this field references the
              parent's spanId/transactionId. Used to build transaction trees and understand
              call hierarchies in complex multi-step AI workflows. Leave null for root-level
              transactions. You can use either 'parentSpanId' (recommended) or
              'parentTransactionId'.

          product_id: Identifier of the product from your own system that you wish to use to correlate
              usage between Revenium & your application.

          reasoning_token_count: The number of reasoning tokens used in the completion. Reasoning tokens are
              extended thinking tokens used by AI models for complex problem-solving. These
              are sometimes billed separately from regular input/output tokens. Only include
              this field if your AI provider reports reasoning tokens Revenium's middleware
              will always populate this field if reasoning tokens are reported by the AI
              provider. Leave null for models without reasoning capabilities.

          region: Cloud region or geographic location where this AI completion was processed. Used
              for analyzing latency patterns, compliance requirements, and regional cost
              differences. Examples: 'us-east-1', 'eu-west-1', 'ap-southeast-2'. Leave null if
              not tracking by region.

          response_quality_score: Optional quality score for the AI response on a 0.0-1.0 scale. Set by your
              application's evaluation logic (e.g., RAGAS, human feedback, custom scoring).
              Used in Revenium analytics to correlate quality with cost, model choice, and
              other metrics. Leave null if not tracking quality scores.

          retry_number: Retry attempt number for this AI completion. 0 indicates the first attempt (no
              retry), 1 indicates first retry, 2 indicates second retry, etc. Used for
              analyzing failure rates and retry patterns. Each retry attempt should be a
              separate transaction with incrementing retryNumber and the same traceId. Leave
              null or set to 0 for first attempts.

          subscriber: Metadata about the subscriber/end-user making this AI request. Include this to
              track usage by individual users within an organization. Contains user
              identifiers and associated credential information. Leave null if not tracking
              individual user-level usage.

          subscription_id: Unique identifier of the subscription from your own system that you wish to use
              to correlate usage between Revenium & your application.

          system_fingerprint: A unique identifier provided by the AI provider that represents the statistical
              signature of the language model that generated this completion. This fingerprint
              can be used for model attribution, debugging, and monitoring model behavior
              across requests. Automatically provided by some AI providers (e.g., OpenAI) in
              their API responses. Leave null if your provider does not supply this value.

          task_type: Optional category to group related AI tasks for cost and performance analysis.
              Use consistent values to compare metrics across different models or vendors
              performing the same type of work. Examples: 'chat', 'summarization',
              'code-generation', 'translation', 'image-generation', 'embeddings',
              'classification', 'sentiment-analysis'. This is freeform text - choose values
              that match your use cases.

          temperature: The temperature parameter used for this completion, controlling randomness in
              the AI's output. Typically ranges from 0.0 (deterministic) to 2.0 (very random).
              Track this to correlate temperature settings with response quality, cost, or
              other metrics. Useful for A/B testing different temperature values.

          time_to_first_token: The latency in milliseconds from request start to first token received.
              Calculated as (completionStartTime - requestTime). This metric is particularly
              important for streaming completions to measure perceived responsiveness. For
              non-streaming completions, this may be null or equal to requestDuration.

          total_cost: The total cost in USD for this completion (sum of all token costs). Typically
              leave null to let Revenium automatically calculate the total based on token
              counts and current pricing. Only provide a value if you have custom pricing
              agreements or want to override Revenium's cost calculation. If provided, this
              will override Revenium's automatic calculation.

          trace_id: Optional trace identifier to group multiple related AI completion calls that
              belong to the same overall user request or workflow. For example, if a single
              user query triggers multiple LLM calls (e.g., retrieval + generation), use the
              same traceId for all calls to analyze them together in Revenium's analytics.
              Leave null for standalone completions.

          trace_name: Human-readable label for individual trace instances (e.g., 'Marketing Video Q4
              2025'). Enables finding specific workflow executions. Can contain any UTF-8
              string. Max 256 characters. All transactions in the same trace must have the
              same traceName.

          trace_type: Categorical identifier for grouping similar workflows (e.g., 'create_video',
              'write_script'). Enables trace-level analytics and anomaly detection within
              workflow cohorts. Must contain only alphanumeric characters, hyphens, and
              underscores. Max 128 characters. Defaults to 'uncategorized' if not provided or
              invalid. All transactions in the same trace must have the same traceType.

          transaction_id: Unique identifier for this specific AI completion transaction. Used for
              deduplication, correlation with request/response pairs, and transaction lookup
              in Revenium analytics. If not provided, a UUID will be auto-generated. For best
              practices, generate a UUID in your application before making the AI call and use
              the same ID when submitting to Revenium. You can use either 'spanId'
              (recommended) or 'transactionId'.

          transaction_name: Human-readable name for this transaction. Provides context about what this AI
              completion is doing in business terms. Examples: 'Summarize Application',
              'Credit Risk Analysis', 'Customer Support Response'. Used in trace visualization
              for better readability. Falls back to taskType if not provided.

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
                    "agent": agent,
                    "cache_creation_token_cost": cache_creation_token_cost,
                    "cache_creation_token_count": cache_creation_token_count,
                    "cache_read_token_cost": cache_read_token_cost,
                    "cache_read_token_count": cache_read_token_count,
                    "environment": environment,
                    "error_reason": error_reason,
                    "input_token_cost": input_token_cost,
                    "mediation_latency": mediation_latency,
                    "middleware_source": middleware_source,
                    "model_source": model_source,
                    "operation_subtype": operation_subtype,
                    "operation_type": operation_type,
                    "organization_id": organization_id,
                    "output_token_cost": output_token_cost,
                    "parent_transaction_id": parent_transaction_id,
                    "product_id": product_id,
                    "reasoning_token_count": reasoning_token_count,
                    "region": region,
                    "response_quality_score": response_quality_score,
                    "retry_number": retry_number,
                    "subscriber": subscriber,
                    "subscription_id": subscription_id,
                    "system_fingerprint": system_fingerprint,
                    "task_type": task_type,
                    "temperature": temperature,
                    "time_to_first_token": time_to_first_token,
                    "total_cost": total_cost,
                    "trace_id": trace_id,
                    "trace_name": trace_name,
                    "trace_type": trace_type,
                    "transaction_id": transaction_id,
                    "transaction_name": transaction_name,
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
