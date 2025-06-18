# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from revenium_metering import ReveniumMetering, AsyncReveniumMetering
from revenium_metering.types import MeteringResponseResource

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_completion(self, client: ReveniumMetering) -> None:
        ai = client.ai.create_completion(
            completion_start_time="2025-03-02T15:04:05Z",
            cost_type="AI",
            input_token_count=50,
            is_streamed=False,
            model="gpt4",
            output_token_count=150,
            provider="OpenAI",
            request_duration=1000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:06Z",
            stop_reason="END",
            total_token_count=200,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_completion_with_all_params(self, client: ReveniumMetering) -> None:
        ai = client.ai.create_completion(
            completion_start_time="2025-03-02T15:04:05Z",
            cost_type="AI",
            input_token_count=50,
            is_streamed=False,
            model="gpt4",
            output_token_count=150,
            provider="OpenAI",
            request_duration=1000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:06Z",
            stop_reason="END",
            total_token_count=200,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
            agent="marketing-agent",
            cache_creation_token_cost=12.34,
            cache_creation_token_count=1300,
            cache_read_token_cost=12.34,
            cache_read_token_count=1300,
            error_reason="key not allowed to access model",
            input_token_cost=12.34,
            mediation_latency=1000,
            middleware_source="openai-python-sdk",
            model_source="ANTHROPIC",
            operation_type="CHAT",
            organization_id="organizationId-123456",
            output_token_cost=12.34,
            product_id="Free Trial",
            reasoning_token_count=1300,
            response_quality_score=45,
            subscriber={
                "id": "subscriberId-123456",
                "credential": {
                    "name": "OpenAI Key (Production)",
                    "value": "pk-1234567",
                },
                "email": "user@example.com",
            },
            subscription_id="subscriptionId-456789",
            system_fingerprint="fp_44z789a1c23def456gh7890ijkl1234mnopq567rstuv8910wxyz",
            task_type="image-generation",
            temperature=0.78,
            time_to_first_token=10200,
            total_cost=12.34,
            trace_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_completion(self, client: ReveniumMetering) -> None:
        response = client.ai.with_raw_response.create_completion(
            completion_start_time="2025-03-02T15:04:05Z",
            cost_type="AI",
            input_token_count=50,
            is_streamed=False,
            model="gpt4",
            output_token_count=150,
            provider="OpenAI",
            request_duration=1000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:06Z",
            stop_reason="END",
            total_token_count=200,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_completion(self, client: ReveniumMetering) -> None:
        with client.ai.with_streaming_response.create_completion(
            completion_start_time="2025-03-02T15:04:05Z",
            cost_type="AI",
            input_token_count=50,
            is_streamed=False,
            model="gpt4",
            output_token_count=150,
            provider="OpenAI",
            request_duration=1000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:06Z",
            stop_reason="END",
            total_token_count=200,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(MeteringResponseResource, ai, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAI:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_completion(self, async_client: AsyncReveniumMetering) -> None:
        ai = await async_client.ai.create_completion(
            completion_start_time="2025-03-02T15:04:05Z",
            cost_type="AI",
            input_token_count=50,
            is_streamed=False,
            model="gpt4",
            output_token_count=150,
            provider="OpenAI",
            request_duration=1000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:06Z",
            stop_reason="END",
            total_token_count=200,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_completion_with_all_params(self, async_client: AsyncReveniumMetering) -> None:
        ai = await async_client.ai.create_completion(
            completion_start_time="2025-03-02T15:04:05Z",
            cost_type="AI",
            input_token_count=50,
            is_streamed=False,
            model="gpt4",
            output_token_count=150,
            provider="OpenAI",
            request_duration=1000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:06Z",
            stop_reason="END",
            total_token_count=200,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
            agent="marketing-agent",
            cache_creation_token_cost=12.34,
            cache_creation_token_count=1300,
            cache_read_token_cost=12.34,
            cache_read_token_count=1300,
            error_reason="key not allowed to access model",
            input_token_cost=12.34,
            mediation_latency=1000,
            middleware_source="openai-python-sdk",
            model_source="ANTHROPIC",
            operation_type="CHAT",
            organization_id="organizationId-123456",
            output_token_cost=12.34,
            product_id="Free Trial",
            reasoning_token_count=1300,
            response_quality_score=45,
            subscriber={
                "id": "subscriberId-123456",
                "credential": {
                    "name": "OpenAI Key (Production)",
                    "value": "pk-1234567",
                },
                "email": "user@example.com",
            },
            subscription_id="subscriptionId-456789",
            system_fingerprint="fp_44z789a1c23def456gh7890ijkl1234mnopq567rstuv8910wxyz",
            task_type="image-generation",
            temperature=0.78,
            time_to_first_token=10200,
            total_cost=12.34,
            trace_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncReveniumMetering) -> None:
        response = await async_client.ai.with_raw_response.create_completion(
            completion_start_time="2025-03-02T15:04:05Z",
            cost_type="AI",
            input_token_count=50,
            is_streamed=False,
            model="gpt4",
            output_token_count=150,
            provider="OpenAI",
            request_duration=1000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:06Z",
            stop_reason="END",
            total_token_count=200,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_completion(self, async_client: AsyncReveniumMetering) -> None:
        async with async_client.ai.with_streaming_response.create_completion(
            completion_start_time="2025-03-02T15:04:05Z",
            cost_type="AI",
            input_token_count=50,
            is_streamed=False,
            model="gpt4",
            output_token_count=150,
            provider="OpenAI",
            request_duration=1000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:06Z",
            stop_reason="END",
            total_token_count=200,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(MeteringResponseResource, ai, path=["response"])

        assert cast(Any, response.is_closed) is True
