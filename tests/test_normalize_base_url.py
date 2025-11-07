"""Tests for base URL normalization functionality."""

import httpx

from revenium_metering import ReveniumMetering, AsyncReveniumMetering


class TestNormalizeBaseURL:
    """Test the _normalize_base_url method for both sync and async clients."""

    def test_normalize_url_without_meter(self):
        """Test that /meter is added when not present."""
        url = "https://api.example.com"
        normalized = ReveniumMetering._normalize_base_url(url)
        assert normalized == "https://api.example.com/meter/"

    def test_normalize_url_with_meter(self):
        """Test that /meter is not duplicated when already present."""
        url = "https://api.example.com/meter"
        normalized = ReveniumMetering._normalize_base_url(url)
        assert normalized == "https://api.example.com/meter/"

    def test_normalize_url_with_meter_and_trailing_slash(self):
        """Test that /meter with trailing slash is handled correctly."""
        url = "https://api.example.com/meter/"
        normalized = ReveniumMetering._normalize_base_url(url)
        assert normalized == "https://api.example.com/meter/"

    def test_normalize_url_without_meter_with_trailing_slash(self):
        """Test that /meter is added when URL has trailing slash but no /meter."""
        url = "https://api.example.com/"
        normalized = ReveniumMetering._normalize_base_url(url)
        assert normalized == "https://api.example.com/meter/"

    def test_normalize_url_case_insensitive_meter(self):
        """Test that /Meter (different case) is recognized and normalized."""
        url = "https://api.example.com/Meter"
        normalized = ReveniumMetering._normalize_base_url(url)
        # Should preserve the original case but ensure trailing slash
        assert normalized == "https://api.example.com/Meter/"

    def test_normalize_url_with_port(self):
        """Test normalization with port number."""
        url = "https://api.example.com:8080"
        normalized = ReveniumMetering._normalize_base_url(url)
        assert normalized == "https://api.example.com:8080/meter/"

    def test_normalize_url_with_port_and_meter(self):
        """Test normalization with port number and /meter."""
        url = "https://api.example.com:8080/meter"
        normalized = ReveniumMetering._normalize_base_url(url)
        assert normalized == "https://api.example.com:8080/meter/"

    def test_normalize_url_with_existing_path(self):
        """Test normalization when URL has a path before /meter."""
        url = "https://api.example.com/api/v1"
        normalized = ReveniumMetering._normalize_base_url(url)
        assert normalized == "https://api.example.com/api/v1/meter/"

    def test_normalize_url_with_existing_path_and_meter(self):
        """Test normalization when URL has a path with /meter."""
        url = "https://api.example.com/api/v1/meter"
        normalized = ReveniumMetering._normalize_base_url(url)
        assert normalized == "https://api.example.com/api/v1/meter/"

    def test_normalize_url_with_meter_in_middle(self):
        """Test that /meter in the middle of path is handled correctly."""
        url = "https://api.example.com/meter/extra"
        normalized = ReveniumMetering._normalize_base_url(url)
        # Should keep everything up to and including /meter
        assert normalized == "https://api.example.com/meter/"

    def test_normalize_httpx_url_object(self):
        """Test normalization with httpx.URL object."""
        url = httpx.URL("https://api.example.com")
        normalized = ReveniumMetering._normalize_base_url(url)
        assert normalized == "https://api.example.com/meter/"

    def test_normalize_httpx_url_object_with_meter(self):
        """Test normalization with httpx.URL object that has /meter."""
        url = httpx.URL("https://api.example.com/meter")
        normalized = ReveniumMetering._normalize_base_url(url)
        assert normalized == "https://api.example.com/meter/"

    def test_async_client_normalize_url_without_meter(self):
        """Test that async client normalizes URL without /meter."""
        url = "https://api.example.com"
        normalized = AsyncReveniumMetering._normalize_base_url(url)
        assert normalized == "https://api.example.com/meter/"

    def test_async_client_normalize_url_with_meter(self):
        """Test that async client normalizes URL with /meter."""
        url = "https://api.example.com/meter"
        normalized = AsyncReveniumMetering._normalize_base_url(url)
        assert normalized == "https://api.example.com/meter/"

    def test_localhost_without_meter(self):
        """Test normalization with localhost."""
        url = "http://localhost:3000"
        normalized = ReveniumMetering._normalize_base_url(url)
        assert normalized == "http://localhost:3000/meter/"

    def test_localhost_with_meter(self):
        """Test normalization with localhost and /meter."""
        url = "http://localhost:3000/meter"
        normalized = ReveniumMetering._normalize_base_url(url)
        assert normalized == "http://localhost:3000/meter/"

    def test_ip_address_without_meter(self):
        """Test normalization with IP address."""
        url = "http://192.168.1.1:8080"
        normalized = ReveniumMetering._normalize_base_url(url)
        assert normalized == "http://192.168.1.1:8080/meter/"

    def test_ip_address_with_meter(self):
        """Test normalization with IP address and /meter."""
        url = "http://192.168.1.1:8080/meter"
        normalized = ReveniumMetering._normalize_base_url(url)
        assert normalized == "http://192.168.1.1:8080/meter/"


class TestClientInitializationWithNormalization:
    """Test that clients properly normalize base URLs during initialization."""

    def test_sync_client_with_base_url_without_meter(self):
        """Test sync client initialization with base URL without /meter."""
        client = ReveniumMetering(
            api_key="test_key",
            base_url="https://api.example.com"
        )
        assert str(client.base_url) == "https://api.example.com/meter/"

    def test_sync_client_with_base_url_with_meter(self):
        """Test sync client initialization with base URL with /meter."""
        client = ReveniumMetering(
            api_key="test_key",
            base_url="https://api.example.com/meter"
        )
        assert str(client.base_url) == "https://api.example.com/meter/"

    def test_async_client_with_base_url_without_meter(self):
        """Test async client initialization with base URL without /meter."""
        client = AsyncReveniumMetering(
            api_key="test_key",
            base_url="https://api.example.com"
        )
        assert str(client.base_url) == "https://api.example.com/meter/"

    def test_async_client_with_base_url_with_meter(self):
        """Test async client initialization with base URL with /meter."""
        client = AsyncReveniumMetering(
            api_key="test_key",
            base_url="https://api.example.com/meter"
        )
        assert str(client.base_url) == "https://api.example.com/meter/"

    def test_sync_client_default_base_url(self):
        """Test that default base URL is properly set."""
        client = ReveniumMetering(api_key="test_key")
        assert str(client.base_url) == "https://api.revenium.ai/meter/"

    def test_async_client_default_base_url(self):
        """Test that default base URL is properly set for async client."""
        client = AsyncReveniumMetering(api_key="test_key")
        assert str(client.base_url) == "https://api.revenium.ai/meter/"

