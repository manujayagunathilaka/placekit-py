"""Tests for Google Places provider."""

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
