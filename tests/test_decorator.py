"""Tests for the meter_tool decorator, report_tool_call, and configure."""

from __future__ import annotations

import asyncio
from typing import Any, Dict
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

import revenium_metering
from revenium_metering import configure, meter_tool, set_context, clear_context, report_tool_call

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(autouse=True)
def _clean_state() -> None:  # pyright: ignore[reportUnusedFunction]
    """Reset global state between tests."""
    clear_context()
    configure(metering_url="http://localhost:8082", api_key="test-key")


# ---------------------------------------------------------------------------
# meter_tool — naming / import
# ---------------------------------------------------------------------------


class TestMeterToolNaming:
    def test_meter_tool_importable_from_package(self) -> None:
        assert hasattr(revenium_metering, "meter_tool")

    def test_meter_tool_in_all(self) -> None:
        assert "meter_tool" in revenium_metering.__all__

    def test_old_name_meter_not_exported(self) -> None:
        """The old name 'meter' should no longer be in __all__."""
        assert "meter" not in revenium_metering.__all__


# ---------------------------------------------------------------------------
# meter_tool — sync
# ---------------------------------------------------------------------------


class TestMeterToolSync:
    def test_basic_sync_function(self) -> None:
        """Decorated sync function should return its result normally."""
        with patch("revenium_metering.decorator._send_tool_event") as mock_send:
            mock_send.return_value = None

            @meter_tool("test-tool")
            def add(a: int, b: int) -> int:
                return a + b

            result = add(2, 3)
            assert result == 5
            mock_send.assert_called_once()

    def test_sync_captures_timing(self) -> None:
        with patch("revenium_metering.decorator._send_tool_event") as mock_send:
            mock_send.return_value = None

            @meter_tool("timer-tool")
            def noop() -> str:
                return "done"

            noop()
            call_kwargs = mock_send.call_args
            assert call_kwargs[1]["duration_ms"] >= 0
            assert call_kwargs[1]["success"] is True
            assert call_kwargs[1]["error_message"] is None

    def test_sync_captures_failure(self) -> None:
        with patch("revenium_metering.decorator._send_tool_event") as mock_send:
            mock_send.return_value = None

            @meter_tool("fail-tool")
            def boom() -> None:
                raise ValueError("kaboom")

            with pytest.raises(ValueError, match="kaboom"):
                boom()

            call_kwargs = mock_send.call_args
            assert call_kwargs[1]["success"] is False
            assert call_kwargs[1]["error_message"] == "kaboom"

    def test_sync_preserves_function_metadata(self) -> None:
        with patch("revenium_metering.decorator._send_tool_event"):

            @meter_tool("meta-tool")
            def my_function() -> None:
                """My docstring."""

            assert my_function.__name__ == "my_function"
            assert my_function.__doc__ == "My docstring."

    def test_sync_with_operation(self) -> None:
        with patch("revenium_metering.decorator._send_tool_event") as mock_send:
            mock_send.return_value = None

            @meter_tool("scraper", operation="scrape")
            def scrape(url: str) -> str:
                return f"scraped {url}"

            scrape("https://example.com")
            assert mock_send.call_args[1]["operation"] == "scrape"

    def test_sync_with_output_fields_dict(self) -> None:
        with patch("revenium_metering.decorator._send_tool_event") as mock_send:
            mock_send.return_value = None

            @meter_tool("extractor", output_fields=["pages", "size_mb"])
            def fetch() -> Dict[str, Any]:
                return {"pages": 5, "size_mb": 2.3, "secret": "hidden"}

            fetch()
            usage = mock_send.call_args[1]["usage_metadata"]
            assert usage == {"pages": 5, "size_mb": 2.3}

    def test_sync_with_output_fields_object(self) -> None:
        with patch("revenium_metering.decorator._send_tool_event") as mock_send:
            mock_send.return_value = None

            class Result:
                duration_seconds = 12
                resolution = "1080p"

            @meter_tool("video-gen", output_fields=["duration_seconds", "resolution"])
            def generate() -> Result:
                return Result()

            generate()
            usage = mock_send.call_args[1]["usage_metadata"]
            assert usage == {"duration_seconds": 12, "resolution": "1080p"}


# ---------------------------------------------------------------------------
# meter_tool — async
# ---------------------------------------------------------------------------


class TestMeterToolAsync:
    async def test_basic_async_function(self) -> None:
        with patch("revenium_metering.decorator._send_tool_event_async", new_callable=AsyncMock) as mock_send:

            @meter_tool("async-tool")
            async def fetch_data() -> str:
                return "data"

            result = await fetch_data()
            assert result == "data"
            mock_send.assert_called_once()

    async def test_async_captures_failure(self) -> None:
        with patch("revenium_metering.decorator._send_tool_event_async", new_callable=AsyncMock) as mock_send:

            @meter_tool("async-fail")
            async def boom() -> None:
                raise RuntimeError("async boom")

            with pytest.raises(RuntimeError, match="async boom"):
                await boom()

            call_kwargs = mock_send.call_args
            assert call_kwargs[1]["success"] is False
            assert call_kwargs[1]["error_message"] == "async boom"

    async def test_async_preserves_function_metadata(self) -> None:
        with patch("revenium_metering.decorator._send_tool_event_async", new_callable=AsyncMock):

            @meter_tool("async-meta")
            async def my_async_fn() -> None:
                """Async docstring."""

            assert my_async_fn.__name__ == "my_async_fn"
            assert my_async_fn.__doc__ == "Async docstring."

    async def test_async_detects_coroutine_function(self) -> None:
        with patch("revenium_metering.decorator._send_tool_event_async", new_callable=AsyncMock):

            @meter_tool("detect-async")
            async def coro() -> str:
                return "ok"

            assert asyncio.iscoroutinefunction(coro)


# ---------------------------------------------------------------------------
# meter_tool — context integration
# ---------------------------------------------------------------------------


class TestMeterToolContext:
    def test_uses_global_context(self) -> None:
        with patch("revenium_metering.decorator._send_tool_event") as mock_send:
            mock_send.return_value = None

            set_context(agent="test-agent", organization_name="AcmeCorp")

            @meter_tool("ctx-tool")
            def work() -> str:
                return "done"

            work()
            ctx = mock_send.call_args[1]["context"]
            assert ctx.agent == "test-agent"
            assert ctx.organization_name == "AcmeCorp"

    def test_decorator_params_override_context(self) -> None:
        with patch("revenium_metering.decorator._send_tool_event") as mock_send:
            mock_send.return_value = None

            set_context(agent="global-agent")

            @meter_tool("override-tool", agent="decorator-agent")
            def work() -> str:
                return "done"

            work()
            ctx = mock_send.call_args[1]["context"]
            assert ctx.agent == "decorator-agent"


# ---------------------------------------------------------------------------
# report_tool_call
# ---------------------------------------------------------------------------


class TestReportToolCall:
    def test_basic_report(self) -> None:
        with patch("revenium_metering.decorator._send_tool_event") as mock_send:
            mock_send.return_value = None

            report_tool_call(
                tool_id="manual-tool",
                operation="query",
                duration_ms=500,
                success=True,
            )

            mock_send.assert_called_once()
            assert mock_send.call_args[1]["tool_id"] == "manual-tool"
            assert mock_send.call_args[1]["operation"] == "query"
            assert mock_send.call_args[1]["duration_ms"] == 500
            assert mock_send.call_args[1]["success"] is True

    def test_report_with_context_fields(self) -> None:
        with patch("revenium_metering.decorator._send_tool_event") as mock_send:
            mock_send.return_value = None

            report_tool_call(
                tool_id="ctx-report",
                agent="reporter",
                organization_name="TestOrg",
                product_name="chatbot",
            )

            ctx = mock_send.call_args[1]["context"]
            assert ctx.agent == "reporter"
            assert ctx.organization_name == "TestOrg"
            assert ctx.product_name == "chatbot"

    def test_report_failure(self) -> None:
        with patch("revenium_metering.decorator._send_tool_event") as mock_send:
            mock_send.return_value = None

            report_tool_call(
                tool_id="fail-report",
                success=False,
                error_message="timeout",
                duration_ms=30000,
            )

            assert mock_send.call_args[1]["success"] is False
            assert mock_send.call_args[1]["error_message"] == "timeout"


# ---------------------------------------------------------------------------
# configure
# ---------------------------------------------------------------------------


class TestConfigure:
    def test_configure_sets_url_and_key(self) -> None:
        from revenium_metering import decorator

        configure(metering_url="http://custom:9999", api_key="my-key")
        assert decorator._metering_url == "http://custom:9999"
        assert decorator._api_key == "my-key"


# ---------------------------------------------------------------------------
# _build_event_payload
# ---------------------------------------------------------------------------


class TestBuildEventPayload:
    def test_payload_structure(self) -> None:
        from revenium_metering.context import ReveniumContext
        from revenium_metering.decorator import _build_event_payload

        ctx = ReveniumContext(
            agent="test-agent",
            organization_name="TestOrg",
            product_name="chatbot",
            subscriber_credential="cust_123",
            workflow_id="wf-1",
            trace_id="tr-1",
            transaction_id="tx-abc",
        )

        payload = _build_event_payload(
            tool_id="firecrawl",
            operation="scrape",
            duration_ms=1234,
            success=True,
            error_message=None,
            usage_metadata={"pages": 5},
            context=ctx,
        )

        assert payload["toolId"] == "firecrawl"
        assert payload["operation"] == "scrape"
        assert payload["durationMs"] == 1234
        assert payload["success"] is True
        assert payload["transactionId"] == "tx-abc"
        assert payload["agent"] == "test-agent"
        assert payload["organizationName"] == "TestOrg"
        assert payload["productName"] == "chatbot"
        assert payload["subscriberCredential"] == "cust_123"
        assert payload["workflowId"] == "wf-1"
        assert payload["traceId"] == "tr-1"
        assert payload["usageMetadata"] == {"pages": 5}
        assert "timestamp" in payload
        assert "errorMessage" not in payload

    def test_payload_with_error(self) -> None:
        from revenium_metering.context import ReveniumContext
        from revenium_metering.decorator import _build_event_payload

        ctx = ReveniumContext()
        payload = _build_event_payload(
            tool_id="bad-tool",
            operation=None,
            duration_ms=100,
            success=False,
            error_message="connection refused",
            usage_metadata=None,
            context=ctx,
        )

        assert payload["success"] is False
        assert payload["errorMessage"] == "connection refused"
        assert payload["operation"] == "execute"
        assert "usageMetadata" not in payload


# ---------------------------------------------------------------------------
# _send_tool_event — HTTP integration
# ---------------------------------------------------------------------------


class TestSendToolEvent:
    def test_posts_to_correct_endpoint(self) -> None:
        from revenium_metering.context import ReveniumContext
        from revenium_metering.decorator import _send_tool_event

        configure(metering_url="http://test-host:8082", api_key="test-api-key")
        ctx = ReveniumContext(agent="http-test")

        with patch("revenium_metering.decorator.httpx.Client") as MockClient:
            mock_instance = MagicMock()
            mock_response = MagicMock()
            mock_response.raise_for_status = MagicMock()
            mock_instance.post.return_value = mock_response
            mock_instance.__enter__ = MagicMock(return_value=mock_instance)
            mock_instance.__exit__ = MagicMock(return_value=False)
            MockClient.return_value = mock_instance

            _send_tool_event(
                tool_id="http-tool",
                operation="test",
                duration_ms=100,
                success=True,
                error_message=None,
                usage_metadata=None,
                context=ctx,
            )

            mock_instance.post.assert_called_once()
            call_args = mock_instance.post.call_args
            assert call_args[0][0] == "http://test-host:8082/v2/tool/events"
            assert call_args[1]["headers"]["x-api-key"] == "test-api-key"

    def test_http_error_does_not_raise(self) -> None:
        """Metering errors should be swallowed so they don't break the user's code."""
        from revenium_metering.context import ReveniumContext
        from revenium_metering.decorator import _send_tool_event

        ctx = ReveniumContext()

        with patch("revenium_metering.decorator.httpx.Client") as MockClient:
            mock_instance = MagicMock()
            mock_instance.post.side_effect = httpx.ConnectError("refused")
            mock_instance.__enter__ = MagicMock(return_value=mock_instance)
            mock_instance.__exit__ = MagicMock(return_value=False)
            MockClient.return_value = mock_instance

            # Should NOT raise
            _send_tool_event(
                tool_id="fail-http",
                operation=None,
                duration_ms=0,
                success=True,
                error_message=None,
                usage_metadata=None,
                context=ctx,
            )


# ---------------------------------------------------------------------------
# _extract_output_fields
# ---------------------------------------------------------------------------


class TestExtractOutputFields:
    def test_none_result(self) -> None:
        from revenium_metering.decorator import _extract_output_fields

        assert _extract_output_fields(None, ["field"]) is None

    def test_no_output_fields(self) -> None:
        from revenium_metering.decorator import _extract_output_fields

        assert _extract_output_fields({"key": "val"}, None) is None
        assert _extract_output_fields({"key": "val"}, []) is None

    def test_dict_result(self) -> None:
        from revenium_metering.decorator import _extract_output_fields

        result = _extract_output_fields(
            {"pages": 5, "size": 100, "secret": "x"},
            ["pages", "size"],
        )
        assert result == {"pages": 5, "size": 100}

    def test_missing_fields_skipped(self) -> None:
        from revenium_metering.decorator import _extract_output_fields

        result = _extract_output_fields({"pages": 5}, ["pages", "missing"])
        assert result == {"pages": 5}

    def test_object_result(self) -> None:
        from revenium_metering.decorator import _extract_output_fields

        class Obj:
            x = 10
            y = 20

        result = _extract_output_fields(Obj(), ["x", "y"])
        assert result == {"x": 10, "y": 20}

    def test_error_in_accessor_returns_none(self) -> None:
        from revenium_metering.decorator import _extract_output_fields

        class BadObj:
            @property
            def explode(self) -> None:
                raise RuntimeError("boom")

        result = _extract_output_fields(BadObj(), ["explode"])
        assert result is None
