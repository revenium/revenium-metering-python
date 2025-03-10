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
            audio_token_count=150,
            cached_token_count=1300,
            completion_token_count=150,
            cost_type="AI",
            model="gpt4",
            prompt_token_count=50,
            provider="OpenAI",
            reasoning_token_count=1300,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:06Z",
            stop_reason="END",
            total_token_count=200,
            transaction_cost=12.34,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_completion_with_all_params(self, client: ReveniumMetering) -> None:
        ai = client.ai.create_completion(
            audio_token_count=150,
            cached_token_count=1300,
            completion_token_count=150,
            cost_type="AI",
            model="gpt4",
            prompt_token_count=50,
            provider="OpenAI",
            reasoning_token_count=1300,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:06Z",
            stop_reason="END",
            total_token_count=200,
            transaction_cost=12.34,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
            ai_provider_key_name="Production Key (OpenAI)",
            api_key="apiKey",
            organization_id="org-123",
            product_id="Free Trial",
            source_id="source-123",
            subscriber_id="sub-001",
            subscription_id="subscr-456",
            task_id="task-123",
            task_type="completion",
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_completion(self, client: ReveniumMetering) -> None:
        response = client.ai.with_raw_response.create_completion(
            audio_token_count=150,
            cached_token_count=1300,
            completion_token_count=150,
            cost_type="AI",
            model="gpt4",
            prompt_token_count=50,
            provider="OpenAI",
            reasoning_token_count=1300,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:06Z",
            stop_reason="END",
            total_token_count=200,
            transaction_cost=12.34,
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
            audio_token_count=150,
            cached_token_count=1300,
            completion_token_count=150,
            cost_type="AI",
            model="gpt4",
            prompt_token_count=50,
            provider="OpenAI",
            reasoning_token_count=1300,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:06Z",
            stop_reason="END",
            total_token_count=200,
            transaction_cost=12.34,
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
            audio_token_count=150,
            cached_token_count=1300,
            completion_token_count=150,
            cost_type="AI",
            model="gpt4",
            prompt_token_count=50,
            provider="OpenAI",
            reasoning_token_count=1300,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:06Z",
            stop_reason="END",
            total_token_count=200,
            transaction_cost=12.34,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_completion_with_all_params(self, async_client: AsyncReveniumMetering) -> None:
        ai = await async_client.ai.create_completion(
            audio_token_count=150,
            cached_token_count=1300,
            completion_token_count=150,
            cost_type="AI",
            model="gpt4",
            prompt_token_count=50,
            provider="OpenAI",
            reasoning_token_count=1300,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:06Z",
            stop_reason="END",
            total_token_count=200,
            transaction_cost=12.34,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
            ai_provider_key_name="Production Key (OpenAI)",
            api_key="apiKey",
            organization_id="org-123",
            product_id="Free Trial",
            source_id="source-123",
            subscriber_id="sub-001",
            subscription_id="subscr-456",
            task_id="task-123",
            task_type="completion",
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_completion(self, async_client: AsyncReveniumMetering) -> None:
        response = await async_client.ai.with_raw_response.create_completion(
            audio_token_count=150,
            cached_token_count=1300,
            completion_token_count=150,
            cost_type="AI",
            model="gpt4",
            prompt_token_count=50,
            provider="OpenAI",
            reasoning_token_count=1300,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:06Z",
            stop_reason="END",
            total_token_count=200,
            transaction_cost=12.34,
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
            audio_token_count=150,
            cached_token_count=1300,
            completion_token_count=150,
            cost_type="AI",
            model="gpt4",
            prompt_token_count=50,
            provider="OpenAI",
            reasoning_token_count=1300,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:06Z",
            stop_reason="END",
            total_token_count=200,
            transaction_cost=12.34,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(MeteringResponseResource, ai, path=["response"])

        assert cast(Any, response.is_closed) is True
