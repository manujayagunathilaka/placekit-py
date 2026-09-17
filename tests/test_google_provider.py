"""Tests for Google Places provider."""

from unittest.mock import patch

from placekit import Location, Place, PlaceCategory
from placekit.providers import GooglePlacesProvider
from placekit.providers.base import BasePlaceProvider
from placekit.providers.google_places import (
    DEFAULT_GOOGLE_PLACES_ENDPOINT,
    DEFAULT_GOOGLE_PLACES_TIMEOUT,
)


def test_google_places_provider_inherits_from_base_provider():
    assert issubclass(GooglePlacesProvider, BasePlaceProvider)


def test_google_places_provider_stores_api_key():
    provider = GooglePlacesProvider(api_key="test-api-key")

    assert provider.api_key == "test-api-key"


def test_google_places_provider_uses_default_configuration():
    provider = GooglePlacesProvider(api_key="test-api-key")

    assert provider.endpoint == DEFAULT_GOOGLE_PLACES_ENDPOINT
    assert provider.timeout == DEFAULT_GOOGLE_PLACES_TIMEOUT


def test_google_places_provider_accepts_custom_configuration():
    provider = GooglePlacesProvider(
        api_key="test-api-key",
        endpoint="https://example.com/places",
        timeout=10,
    )

    assert provider.api_key == "test-api-key"
    assert provider.endpoint == "https://example.com/places"
    assert provider.timeout == 10


def test_google_places_provider_nearby_uses_google_helpers():
    provider = GooglePlacesProvider(
        api_key="test-api-key",
        endpoint="https://example.com/places",
        timeout=10,
    )
    location = Location(latitude=6.9147, longitude=79.9729)

    parsed_places = [
        Place(
            name="ABC Restaurant",
            category=PlaceCategory.RESTAURANT,
            location=location,
        )
    ]

    with (
        patch(
            "placekit.providers.google.get_google_place_type",
            return_value="restaurant",
        ) as mock_get_place_type,
        patch(
            "placekit.providers.google.fetch_google_places_data",
            return_value={"results": []},
        ) as mock_fetch_data,
        patch(
            "placekit.providers.google.parse_google_places_response",
            return_value=parsed_places,
        ) as mock_parse_response,
    ):
        places = provider.nearby(
            location=location,
            categories=[PlaceCategory.RESTAURANT],
            radius_km=2,
            limit=10,
        )

    assert places == parsed_places

    mock_get_place_type.assert_called_once_with(PlaceCategory.RESTAURANT)
    mock_fetch_data.assert_called_once_with(
        api_key="test-api-key",
        latitude=6.9147,
        longitude=79.9729,
        radius_meters=2000,
        place_type="restaurant",
        endpoint="https://example.com/places",
        timeout=10,
    )
    mock_parse_response.assert_called_once_with(
        data={"results": []},
        category=PlaceCategory.RESTAURANT,
    )


def test_google_places_provider_nearby_skips_unsupported_categories():
    provider = GooglePlacesProvider(api_key="test-api-key")
    location = Location(latitude=6.9147, longitude=79.9729)

    with (
        patch(
            "placekit.providers.google.get_google_place_type",
            return_value=None,
        ) as mock_get_place_type,
        patch("placekit.providers.google.fetch_google_places_data") as mock_fetch_data,
        patch(
            "placekit.providers.google.parse_google_places_response",
        ) as mock_parse_response,
    ):
        places = provider.nearby(
            location=location,
            categories=["gym"],
            radius_km=2,
        )

    assert places == []

    mock_get_place_type.assert_called_once_with("gym")
    mock_fetch_data.assert_not_called()
    mock_parse_response.assert_not_called()


def test_google_places_provider_nearby_applies_limit():
    provider = GooglePlacesProvider(api_key="test-api-key")
    location = Location(latitude=6.9147, longitude=79.9729)

    parsed_places = [
        Place(name="Place A", category=PlaceCategory.RESTAURANT, location=location),
        Place(name="Place B", category=PlaceCategory.RESTAURANT, location=location),
        Place(name="Place C", category=PlaceCategory.RESTAURANT, location=location),
    ]

    with (
        patch(
            "placekit.providers.google.get_google_place_type",
            return_value="restaurant",
        ),
        patch(
            "placekit.providers.google.fetch_google_places_data",
            return_value={"results": []},
        ),
        patch(
            "placekit.providers.google.parse_google_places_response",
            return_value=parsed_places,
        ),
    ):
        places = provider.nearby(
            location=location,
            categories=[PlaceCategory.RESTAURANT],
            radius_km=2,
            limit=2,
        )

    assert places == parsed_places[:2]
