# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from revenium_metering import ReveniumMetering, AsyncReveniumMetering
from revenium_metering.types import MeteringResponseResource

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_meter_request(self, client: ReveniumMetering) -> None:
        api = client.apis.meter_request(
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(MeteringResponseResource, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_meter_request_with_all_params(self, client: ReveniumMetering) -> None:
        api = client.apis.meter_request(
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
            content_type="application/json",
            credential="The credential used to access the API.  Visible on the subscriber credentials in page in the Revenium platform.",
            method="GET",
            remote_host="192.168.1.1",
            request_message_size=1024,
            resource="https://api.example.com/resource",
            source_id="5Agqrm:c4917580-281d-48e1-a206-05e595f006ec",
            source_type="KONG",
            user_agent="Mozilla/5.0",
        )
        assert_matches_type(MeteringResponseResource, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_meter_request(self, client: ReveniumMetering) -> None:
        response = client.apis.with_raw_response.meter_request(
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(MeteringResponseResource, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_meter_request(self, client: ReveniumMetering) -> None:
        with client.apis.with_streaming_response.meter_request(
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(MeteringResponseResource, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_meter_response(self, client: ReveniumMetering) -> None:
        api = client.apis.meter_response(
            response_code=200,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(MeteringResponseResource, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_meter_response_with_all_params(self, client: ReveniumMetering) -> None:
        api = client.apis.meter_response(
            response_code=200,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
            backend_latency=1200,
            content_type="application/json",
            gateway_latency=50,
            response_message_size=1024,
            total_duration=1500,
        )
        assert_matches_type(MeteringResponseResource, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_meter_response(self, client: ReveniumMetering) -> None:
        response = client.apis.with_raw_response.meter_response(
            response_code=200,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = response.parse()
        assert_matches_type(MeteringResponseResource, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_meter_response(self, client: ReveniumMetering) -> None:
        with client.apis.with_streaming_response.meter_response(
            response_code=200,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = response.parse()
            assert_matches_type(MeteringResponseResource, api, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPIs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_meter_request(self, async_client: AsyncReveniumMetering) -> None:
        api = await async_client.apis.meter_request(
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(MeteringResponseResource, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_meter_request_with_all_params(self, async_client: AsyncReveniumMetering) -> None:
        api = await async_client.apis.meter_request(
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
            content_type="application/json",
            credential="The credential used to access the API.  Visible on the subscriber credentials in page in the Revenium platform.",
            method="GET",
            remote_host="192.168.1.1",
            request_message_size=1024,
            resource="https://api.example.com/resource",
            source_id="5Agqrm:c4917580-281d-48e1-a206-05e595f006ec",
            source_type="KONG",
            user_agent="Mozilla/5.0",
        )
        assert_matches_type(MeteringResponseResource, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_meter_request(self, async_client: AsyncReveniumMetering) -> None:
        response = await async_client.apis.with_raw_response.meter_request(
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(MeteringResponseResource, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_meter_request(self, async_client: AsyncReveniumMetering) -> None:
        async with async_client.apis.with_streaming_response.meter_request(
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(MeteringResponseResource, api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_meter_response(self, async_client: AsyncReveniumMetering) -> None:
        api = await async_client.apis.meter_response(
            response_code=200,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )
        assert_matches_type(MeteringResponseResource, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_meter_response_with_all_params(self, async_client: AsyncReveniumMetering) -> None:
        api = await async_client.apis.meter_response(
            response_code=200,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
            backend_latency=1200,
            content_type="application/json",
            gateway_latency=50,
            response_message_size=1024,
            total_duration=1500,
        )
        assert_matches_type(MeteringResponseResource, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_meter_response(self, async_client: AsyncReveniumMetering) -> None:
        response = await async_client.apis.with_raw_response.meter_response(
            response_code=200,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api = await response.parse()
        assert_matches_type(MeteringResponseResource, api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_meter_response(self, async_client: AsyncReveniumMetering) -> None:
        async with async_client.apis.with_streaming_response.meter_response(
            response_code=200,
            transaction_id="123e4567-e89b-12d3-a456-426614174000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api = await response.parse()
            assert_matches_type(MeteringResponseResource, api, path=["response"])

        assert cast(Any, response.is_closed) is True
