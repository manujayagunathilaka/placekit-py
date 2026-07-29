"""Tests for Overpass HTTP client utilities."""

from unittest.mock import Mock, patch

from placekit.providers.overpass import (
    DEFAULT_OVERPASS_ENDPOINT,
    DEFAULT_USER_AGENT,
    fetch_overpass_data,
)


def test_fetch_overpass_data_returns_json_response():
    mock_response = Mock()
    mock_response.json.return_value = {"elements": []}

    with patch("placekit.providers.overpass.requests.post", return_value=mock_response):
        data = fetch_overpass_data(query="sample query")

    assert data == {"elements": []}
    mock_response.raise_for_status.assert_called_once()


def test_fetch_overpass_data_sends_query_to_default_endpoint():
    mock_response = Mock()
    mock_response.json.return_value = {"elements": []}

    with patch(
        "placekit.providers.overpass.requests.post", return_value=mock_response
    ) as mock_post:
        fetch_overpass_data(query="sample query")

    mock_post.assert_called_once_with(
        DEFAULT_OVERPASS_ENDPOINT,
        data={"data": "sample query"},
        headers={"User-Agent": DEFAULT_USER_AGENT},
        timeout=25,
    )


def test_fetch_overpass_data_supports_custom_endpoint_timeout_and_user_agent():
    mock_response = Mock()
    mock_response.json.return_value = {"elements": []}

    with patch(
        "placekit.providers.overpass.requests.post", return_value=mock_response
    ) as mock_post:
        fetch_overpass_data(
            query="sample query",
            endpoint="https://example.com/api/interpreter",
            timeout=10,
            user_agent="my-app/1.0",
        )

    mock_post.assert_called_once_with(
        "https://example.com/api/interpreter",
        data={"data": "sample query"},
        headers={"User-Agent": "my-app/1.0"},
        timeout=10,
    )


def test_fetch_overpass_data_raises_for_http_errors():
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = RuntimeError("HTTP error")

    with patch("placekit.providers.overpass.requests.post", return_value=mock_response):
        try:
            fetch_overpass_data(query="sample query")
        except RuntimeError as error:
            assert str(error) == "HTTP error"
        else:
            raise AssertionError("Expected RuntimeError to be raised")
