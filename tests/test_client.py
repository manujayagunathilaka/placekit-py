"""Tests for the main PlaceKit client."""

from placekit import Location, Place, PlaceCategory, PlaceKitClient
from placekit.providers import BasePlaceProvider


class MockPlaceProvider(BasePlaceProvider):
    """Mock provider used for testing the client."""

    def nearby(
        self,
        location: Location,
        categories: list[str],
        radius_km: float,
        limit: int = 10,
    ) -> list[Place]:
        return [
            Place(
                name="ABC University",
                category=PlaceCategory.UNIVERSITY,
                location=location,
            )
        ]


def test_placekit_client_stores_provider():
    provider = BasePlaceProvider()

    client = PlaceKitClient(provider=provider)

    assert client.provider == provider


def test_placekit_client_nearby_delegates_to_provider():
    provider = MockPlaceProvider()
    client = PlaceKitClient(provider=provider)

    location = Location(latitude=6.9147, longitude=79.9729)

    places = client.nearby(
        location=location,
        categories=[PlaceCategory.UNIVERSITY],
        radius_km=2,
    )

    assert len(places) == 1
    assert places[0].name == "ABC University"
    assert places[0].category == PlaceCategory.UNIVERSITY
    assert places[0].location == location
