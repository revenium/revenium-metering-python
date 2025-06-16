# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from revenium_metering import ReveniumMetering, AsyncReveniumMetering
from revenium_metering.types import MeteringResponseResource

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: ReveniumMetering) -> None:
        event = client.events.create(
            payload={
                "requestTokens": {},
                "responseTokens": {},
            },
            source_type="UNKNOWN",
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(MeteringResponseResource, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: ReveniumMetering) -> None:
        event = client.events.create(
            payload={
                "requestTokens": {},
                "responseTokens": {},
            },
            source_type="UNKNOWN",
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
            source_id="sourceId",
            subscriber_credential="The credential associated with the event.  Visible on the subscriber credentials in page in the Revenium platform.",
        )
        assert_matches_type(MeteringResponseResource, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: ReveniumMetering) -> None:
        response = client.events.with_raw_response.create(
            payload={
                "requestTokens": {},
                "responseTokens": {},
            },
            source_type="UNKNOWN",
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(MeteringResponseResource, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: ReveniumMetering) -> None:
        with client.events.with_streaming_response.create(
            payload={
                "requestTokens": {},
                "responseTokens": {},
            },
            source_type="UNKNOWN",
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(MeteringResponseResource, event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncReveniumMetering) -> None:
        event = await async_client.events.create(
            payload={
                "requestTokens": {},
                "responseTokens": {},
            },
            source_type="UNKNOWN",
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(MeteringResponseResource, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncReveniumMetering) -> None:
        event = await async_client.events.create(
            payload={
                "requestTokens": {},
                "responseTokens": {},
            },
            source_type="UNKNOWN",
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
            source_id="sourceId",
            subscriber_credential="The credential associated with the event.  Visible on the subscriber credentials in page in the Revenium platform.",
        )
        assert_matches_type(MeteringResponseResource, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncReveniumMetering) -> None:
        response = await async_client.events.with_raw_response.create(
            payload={
                "requestTokens": {},
                "responseTokens": {},
            },
            source_type="UNKNOWN",
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(MeteringResponseResource, event, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncReveniumMetering) -> None:
        async with async_client.events.with_streaming_response.create(
            payload={
                "requestTokens": {},
                "responseTokens": {},
            },
            source_type="UNKNOWN",
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(MeteringResponseResource, event, path=["response"])

        assert cast(Any, response.is_closed) is True
