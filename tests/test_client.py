"""Tests for the main PlaceKit client."""

from placekit import PlaceKitClient
from placekit.providers.base import BasePlaceProvider


def test_placekit_client_stores_provider():
    provider = BasePlaceProvider()

    client = PlaceKitClient(provider=provider)

    assert client.provider == provider