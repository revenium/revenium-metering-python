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

    @pytest.mark.skip()
    @parametrize
    def test_method_create_audio(self, client: ReveniumMetering) -> None:
        ai = client.ai.create_audio(
            model="whisper-1",
            provider="OpenAI",
            request_duration=5000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:10Z",
            transaction_id="audio-txn-123",
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_audio_with_all_params(self, client: ReveniumMetering) -> None:
        ai = client.ai.create_audio(
            model="whisper-1",
            provider="OpenAI",
            request_duration=5000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:10Z",
            transaction_id="audio-txn-123",
            duration_seconds=120.5,
            character_count=500,
            input_audio_token_count=1500,
            output_audio_token_count=2000,
            input_token_count=100,
            output_token_count=150,
            operation_subtype="transcription",
            billing_unit="PER_MINUTE",
            language="en",
            voice="alloy",
            audio_format="mp3",
            quality="hd",
            speed=1.0,
            sample_rate=44100,
            response_format="verbose_json",
            source_language="es",
            target_language="en",
            is_realtime=False,
            total_cost=0.006,
            error_reason="Audio file too large",
            error_code=413,
            billing_skipped=False,
            skip_reason="FREE_TIER",
            subscriber={
                "id": "subscriber-123",
                "credential": {
                    "name": "OpenAI Key",
                    "value": "sk-123",
                },
                "email": "user@example.com",
            },
            subscriber_email="user@example.com",
            subscriber_id="subscriber-123",
            subscription_id="sub-456",
            organization_id="org-789",
            product_id="audio-product",
            trace_id="trace-123",
            trace_type="audio-workflow",
            trace_name="Audio Transcription",
            parent_transaction_id="parent-txn-123",
            transaction_name="Transcribe Audio",
            task_type="transcription",
            agent="audio-agent",
            environment="production",
            region="us-east-1",
            retry_number=0,
            middleware_source="openai-python-sdk",
            model_source="OPENAI",
            credential_alias="Production Key",
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_video(self, client: ReveniumMetering) -> None:
        ai = client.ai.create_video(
            model="gen-3",
            provider="RunwayML",
            request_duration=30000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:35Z",
            transaction_id="video-txn-123",
            duration_seconds=10.0,
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_video_with_all_params(self, client: ReveniumMetering) -> None:
        ai = client.ai.create_video(
            model="gen-3",
            provider="RunwayML",
            request_duration=30000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:35Z",
            transaction_id="video-txn-123",
            duration_seconds=10.0,
            credits_consumed=10.0,
            requested_duration_seconds=15.0,
            credit_rate=1.0,
            fps=30,
            resolution="1080p",
            video_job_id="job-12345",
            async_operation=False,
            operation_subtype="generation",
            total_cost=0.50,
            error_reason="Video generation failed",
            error_code=500,
            billing_skipped=False,
            skip_reason="FREE_TIER",
            subscriber={
                "id": "subscriber-123",
                "credential": {
                    "name": "RunwayML Key",
                    "value": "rw-123",
                },
                "email": "user@example.com",
            },
            subscriber_email="user@example.com",
            subscriber_id="subscriber-123",
            subscription_id="sub-456",
            organization_id="org-789",
            product_id="video-product",
            trace_id="trace-123",
            trace_type="video-workflow",
            trace_name="Video Generation",
            parent_transaction_id="parent-txn-123",
            transaction_name="Generate Video",
            task_type="video_generation",
            agent="video-agent",
            environment="production",
            region="us-east-1",
            retry_number=0,
            middleware_source="runway-sdk",
            model_source="RUNWAY",
            credential_alias="Production Key",
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_image(self, client: ReveniumMetering) -> None:
        ai = client.ai.create_image(
            model="dall-e-3",
            provider="OpenAI",
            request_duration=5000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:10Z",
            transaction_id="image-txn-123",
            requested_image_count=2,
            actual_image_count=2,
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_image_with_all_params(self, client: ReveniumMetering) -> None:
        ai = client.ai.create_image(
            model="dall-e-3",
            provider="OpenAI",
            request_duration=5000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:10Z",
            transaction_id="image-txn-123",
            requested_image_count=2,
            actual_image_count=2,
            resolution="1024x1024",
            quality="hd",
            style="vivid",
            format="url",
            revised_prompt_provided=True,
            operation_subtype="generation",
            total_cost=0.08,
            error_reason="Invalid prompt",
            error_code=400,
            billing_skipped=False,
            skip_reason="FREE_TIER",
            subscriber={
                "id": "subscriber-123",
                "credential": {
                    "name": "OpenAI Key",
                    "value": "sk-123",
                },
                "email": "user@example.com",
            },
            subscriber_email="user@example.com",
            subscriber_id="subscriber-123",
            subscription_id="sub-456",
            organization_id="org-789",
            product_id="image-product",
            trace_id="trace-123",
            trace_type="image-workflow",
            trace_name="Image Generation",
            parent_transaction_id="parent-txn-123",
            transaction_name="Generate Image",
            task_type="image_generation",
            agent="image-agent",
            environment="production",
            region="us-east-1",
            retry_number=0,
            middleware_source="openai-python-sdk",
            model_source="OPENAI",
            credential_alias="Production Key",
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])


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

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_audio(self, async_client: AsyncReveniumMetering) -> None:
        ai = await async_client.ai.create_audio(
            model="whisper-1",
            provider="OpenAI",
            request_duration=5000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:10Z",
            transaction_id="audio-txn-123",
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_audio_with_all_params(self, async_client: AsyncReveniumMetering) -> None:
        ai = await async_client.ai.create_audio(
            model="whisper-1",
            provider="OpenAI",
            request_duration=5000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:10Z",
            transaction_id="audio-txn-123",
            duration_seconds=120.5,
            character_count=500,
            input_audio_token_count=1500,
            output_audio_token_count=2000,
            input_token_count=100,
            output_token_count=150,
            operation_subtype="transcription",
            billing_unit="PER_MINUTE",
            language="en",
            voice="alloy",
            audio_format="mp3",
            quality="hd",
            speed=1.0,
            sample_rate=44100,
            response_format="verbose_json",
            source_language="es",
            target_language="en",
            is_realtime=False,
            total_cost=0.006,
            error_reason="Audio file too large",
            error_code=413,
            billing_skipped=False,
            skip_reason="FREE_TIER",
            subscriber={
                "id": "subscriber-123",
                "credential": {
                    "name": "OpenAI Key",
                    "value": "sk-123",
                },
                "email": "user@example.com",
            },
            subscriber_email="user@example.com",
            subscriber_id="subscriber-123",
            subscription_id="sub-456",
            organization_id="org-789",
            product_id="audio-product",
            trace_id="trace-123",
            trace_type="audio-workflow",
            trace_name="Audio Transcription",
            parent_transaction_id="parent-txn-123",
            transaction_name="Transcribe Audio",
            task_type="transcription",
            agent="audio-agent",
            environment="production",
            region="us-east-1",
            retry_number=0,
            middleware_source="openai-python-sdk",
            model_source="OPENAI",
            credential_alias="Production Key",
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_video(self, async_client: AsyncReveniumMetering) -> None:
        ai = await async_client.ai.create_video(
            model="gen-3",
            provider="RunwayML",
            request_duration=30000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:35Z",
            transaction_id="video-txn-123",
            duration_seconds=10.0,
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_video_with_all_params(self, async_client: AsyncReveniumMetering) -> None:
        ai = await async_client.ai.create_video(
            model="gen-3",
            provider="RunwayML",
            request_duration=30000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:35Z",
            transaction_id="video-txn-123",
            duration_seconds=10.0,
            credits_consumed=10.0,
            requested_duration_seconds=15.0,
            credit_rate=1.0,
            fps=30,
            resolution="1080p",
            video_job_id="job-12345",
            async_operation=False,
            operation_subtype="generation",
            total_cost=0.50,
            error_reason="Video generation failed",
            error_code=500,
            billing_skipped=False,
            skip_reason="FREE_TIER",
            subscriber={
                "id": "subscriber-123",
                "credential": {
                    "name": "RunwayML Key",
                    "value": "rw-123",
                },
                "email": "user@example.com",
            },
            subscriber_email="user@example.com",
            subscriber_id="subscriber-123",
            subscription_id="sub-456",
            organization_id="org-789",
            product_id="video-product",
            trace_id="trace-123",
            trace_type="video-workflow",
            trace_name="Video Generation",
            parent_transaction_id="parent-txn-123",
            transaction_name="Generate Video",
            task_type="video_generation",
            agent="video-agent",
            environment="production",
            region="us-east-1",
            retry_number=0,
            middleware_source="runway-sdk",
            model_source="RUNWAY",
            credential_alias="Production Key",
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_image(self, async_client: AsyncReveniumMetering) -> None:
        ai = await async_client.ai.create_image(
            model="dall-e-3",
            provider="OpenAI",
            request_duration=5000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:10Z",
            transaction_id="image-txn-123",
            requested_image_count=2,
            actual_image_count=2,
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_image_with_all_params(self, async_client: AsyncReveniumMetering) -> None:
        ai = await async_client.ai.create_image(
            model="dall-e-3",
            provider="OpenAI",
            request_duration=5000,
            request_time="2025-03-02T15:04:05Z",
            response_time="2025-03-02T15:04:10Z",
            transaction_id="image-txn-123",
            requested_image_count=2,
            actual_image_count=2,
            resolution="1024x1024",
            quality="hd",
            style="vivid",
            format="url",
            revised_prompt_provided=True,
            operation_subtype="generation",
            total_cost=0.08,
            error_reason="Invalid prompt",
            error_code=400,
            billing_skipped=False,
            skip_reason="FREE_TIER",
            subscriber={
                "id": "subscriber-123",
                "credential": {
                    "name": "OpenAI Key",
                    "value": "sk-123",
                },
                "email": "user@example.com",
            },
            subscriber_email="user@example.com",
            subscriber_id="subscriber-123",
            subscription_id="sub-456",
            organization_id="org-789",
            product_id="image-product",
            trace_id="trace-123",
            trace_type="image-workflow",
            trace_name="Image Generation",
            parent_transaction_id="parent-txn-123",
            transaction_name="Generate Image",
            task_type="image_generation",
            agent="image-agent",
            environment="production",
            region="us-east-1",
            retry_number=0,
            middleware_source="openai-python-sdk",
            model_source="OPENAI",
            credential_alias="Production Key",
        )
        assert_matches_type(MeteringResponseResource, ai, path=["response"])
