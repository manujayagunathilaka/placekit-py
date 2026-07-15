"""Tests for place providers."""

import pytest

from placekit import Location
from placekit.providers.base import BasePlaceProvider


def test_base_place_provider_nearby_not_implemented():
    provider = BasePlaceProvider()

    with pytest.raises(NotImplementedError, match="Providers must implement the nearby method."):
        provider.nearby(
            location=Location(latitude=6.9147, longitude=79.9729),
            categories=["university"],
            radius_km=2,
        )