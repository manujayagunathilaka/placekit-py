"""Tests for Google Places response parsing and HTTP utilities."""

from unittest.mock import Mock, patch

import pytest
import requests

from placekit import Location, OverpassRequestError, OverpassResponseError, Place
from placekit.providers.google_places import (
    DEFAULT_GOOGLE_PLACES_ENDPOINT,
    DEFAULT_GOOGLE_PLACES_TIMEOUT,
    fetch_google_places_data,
    parse_google_places_response,
)


def test_fetch_google_places_data_returns_json_response():
    mock_response = Mock()
    mock_response.json.return_value = {"results": []}

    with patch(
        "placekit.providers.google_places.requests.get",
        return_value=mock_response,
    ):
        data = fetch_google_places_data(
            api_key="test-api-key",
            latitude=6.9147,
            longitude=79.9729,
            radius_meters=2000,
            place_type="restaurant",
        )

    assert data == {"results": []}
    mock_response.raise_for_status.assert_called_once()


def test_fetch_google_places_data_sends_expected_request_parameters():
    mock_response = Mock()
    mock_response.json.return_value = {"results": []}

    with patch(
        "placekit.providers.google_places.requests.get",
        return_value=mock_response,
    ) as mock_get:
        fetch_google_places_data(
            api_key="test-api-key",
            latitude=6.9147,
            longitude=79.9729,
            radius_meters=2000,
            place_type="restaurant",
        )

    mock_get.assert_called_once_with(
        DEFAULT_GOOGLE_PLACES_ENDPOINT,
        params={
            "key": "test-api-key",
            "location": "6.9147,79.9729",
            "radius": 2000,
            "type": "restaurant",
        },
        timeout=DEFAULT_GOOGLE_PLACES_TIMEOUT,
    )


def test_fetch_google_places_data_supports_custom_endpoint_and_timeout():
    mock_response = Mock()
    mock_response.json.return_value = {"results": []}

    with patch(
        "placekit.providers.google_places.requests.get",
        return_value=mock_response,
    ) as mock_get:
        fetch_google_places_data(
            api_key="test-api-key",
            latitude=6.9147,
            longitude=79.9729,
            radius_meters=2000,
            place_type="restaurant",
            endpoint="https://example.com/places",
            timeout=10,
        )

    mock_get.assert_called_once_with(
        "https://example.com/places",
        params={
            "key": "test-api-key",
            "location": "6.9147,79.9729",
            "radius": 2000,
            "type": "restaurant",
        },
        timeout=10,
    )


def test_fetch_google_places_data_raises_custom_error_for_http_errors():
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.HTTPError("HTTP error")

    with patch(
        "placekit.providers.google_places.requests.get",
        return_value=mock_response,
    ):
        with pytest.raises(
            OverpassRequestError,
            match="Failed to fetch data from Google Places API.",
        ):
            fetch_google_places_data(
                api_key="test-api-key",
                latitude=6.9147,
                longitude=79.9729,
                radius_meters=2000,
                place_type="restaurant",
            )


def test_fetch_google_places_data_raises_custom_error_for_request_errors():
    with patch(
        "placekit.providers.google_places.requests.get",
        side_effect=requests.Timeout("Request timed out"),
    ):
        with pytest.raises(
            OverpassRequestError,
            match="Failed to fetch data from Google Places API.",
        ):
            fetch_google_places_data(
                api_key="test-api-key",
                latitude=6.9147,
                longitude=79.9729,
                radius_meters=2000,
                place_type="restaurant",
            )


def test_fetch_google_places_data_raises_custom_error_for_invalid_json():
    mock_response = Mock()
    mock_response.json.side_effect = ValueError("Invalid JSON")

    with patch(
        "placekit.providers.google_places.requests.get",
        return_value=mock_response,
    ):
        with pytest.raises(
            OverpassResponseError,
            match="Failed to parse Google Places API response.",
        ):
            fetch_google_places_data(
                api_key="test-api-key",
                latitude=6.9147,
                longitude=79.9729,
                radius_meters=2000,
                place_type="restaurant",
            )


def test_parse_google_places_response_returns_places():
    data = {
        "results": [
            {
                "name": "ABC Restaurant",
                "geometry": {
                    "location": {
                        "lat": 6.9147,
                        "lng": 79.9729,
                    }
                },
            }
        ]
    }

    places = parse_google_places_response(
        data=data,
        category="restaurant",
    )

    assert places == [
        Place(
            name="ABC Restaurant",
            category="restaurant",
            location=Location(latitude=6.9147, longitude=79.9729),
        )
    ]


def test_parse_google_places_response_skips_results_without_name():
    data = {
        "results": [
            {
                "geometry": {
                    "location": {
                        "lat": 6.9147,
                        "lng": 79.9729,
                    }
                },
            }
        ]
    }

    places = parse_google_places_response(
        data=data,
        category="restaurant",
    )

    assert places == []


def test_parse_google_places_response_skips_results_without_location():
    data = {
        "results": [
            {
                "name": "ABC Restaurant",
            }
        ]
    }

    places = parse_google_places_response(
        data=data,
        category="restaurant",
    )

    assert places == []


def test_parse_google_places_response_skips_results_without_latitude():
    data = {
        "results": [
            {
                "name": "ABC Restaurant",
                "geometry": {
                    "location": {
                        "lng": 79.9729,
                    }
                },
            }
        ]
    }

    places = parse_google_places_response(
        data=data,
        category="restaurant",
    )

    assert places == []


def test_parse_google_places_response_skips_results_without_longitude():
    data = {
        "results": [
            {
                "name": "ABC Restaurant",
                "geometry": {
                    "location": {
                        "lat": 6.9147,
                    }
                },
            }
        ]
    }

    places = parse_google_places_response(
        data=data,
        category="restaurant",
    )

    assert places == []


def test_parse_google_places_response_returns_empty_list_for_empty_results():
    data = {"results": []}

    places = parse_google_places_response(
        data=data,
        category="restaurant",
    )

    assert places == []


def test_parse_google_places_response_returns_empty_list_when_results_missing():
    data = {}

    places = parse_google_places_response(
        data=data,
        category="restaurant",
    )

    assert places == []
