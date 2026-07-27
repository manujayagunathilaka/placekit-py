"""Tests for place providers."""

import pytest

from placekit import Location, Place, PlaceCategory
from placekit.providers import (
    BasePlaceProvider,
    InMemoryPlaceProvider,
    OpenStreetMapProvider,
)


def test_base_place_provider_nearby_not_implemented():
    provider = BasePlaceProvider()

    with pytest.raises(
        NotImplementedError, match="Providers must implement the nearby method."
    ):
        provider.nearby(
            location=Location(latitude=6.9147, longitude=79.9729),
            categories=["university"],
            radius_km=2,
        )


def test_in_memory_provider_filters_by_category():
    location = Location(latitude=6.9147, longitude=79.9729)

    provider = InMemoryPlaceProvider(
        places=[
            Place(
                name="ABC University",
                category=PlaceCategory.UNIVERSITY,
                location=location,
            ),
            Place(
                name="Sample Hospital",
                category=PlaceCategory.HOSPITAL,
                location=location,
            ),
        ]
    )

    places = provider.nearby(
        location=location,
        categories=[PlaceCategory.UNIVERSITY],
        radius_km=1,
    )

    assert len(places) == 1
    assert places[0].name == "ABC University"
    assert places[0].category == PlaceCategory.UNIVERSITY


def test_in_memory_provider_filters_by_radius():
    base_location = Location(latitude=6.9147, longitude=79.9729)
    nearby_location = Location(latitude=6.9150, longitude=79.9730)
    far_location = Location(latitude=6.9271, longitude=79.8612)

    provider = InMemoryPlaceProvider(
        places=[
            Place(
                name="Nearby University",
                category=PlaceCategory.UNIVERSITY,
                location=nearby_location,
            ),
            Place(
                name="Far University",
                category=PlaceCategory.UNIVERSITY,
                location=far_location,
            ),
        ]
    )

    places = provider.nearby(
        location=base_location,
        categories=[PlaceCategory.UNIVERSITY],
        radius_km=1,
    )

    assert len(places) == 1
    assert places[0].name == "Nearby University"


def test_in_memory_provider_sorts_by_nearest_distance():
    base_location = Location(latitude=6.9147, longitude=79.9729)
    nearby_location = Location(latitude=6.9150, longitude=79.9730)
    middle_location = Location(latitude=6.9180, longitude=79.9750)

    provider = InMemoryPlaceProvider(
        places=[
            Place(
                name="Middle University",
                category=PlaceCategory.UNIVERSITY,
                location=middle_location,
            ),
            Place(
                name="Nearby University",
                category=PlaceCategory.UNIVERSITY,
                location=nearby_location,
            ),
        ]
    )

    places = provider.nearby(
        location=base_location,
        categories=[PlaceCategory.UNIVERSITY],
        radius_km=1,
    )

    assert places[0].name == "Nearby University"
    assert places[1].name == "Middle University"


def test_in_memory_provider_applies_limit():
    location = Location(latitude=6.9147, longitude=79.9729)

    provider = InMemoryPlaceProvider(
        places=[
            Place(
                name="University A",
                category=PlaceCategory.UNIVERSITY,
                location=location,
            ),
            Place(
                name="University B",
                category=PlaceCategory.UNIVERSITY,
                location=location,
            ),
            Place(
                name="University C",
                category=PlaceCategory.UNIVERSITY,
                location=location,
            ),
        ]
    )

    places = provider.nearby(
        location=location,
        categories=[PlaceCategory.UNIVERSITY],
        radius_km=1,
        limit=2,
    )

    assert len(places) == 2
    assert places[0].name == "University A"
    assert places[1].name == "University B"


def test_openstreetmap_provider_nearby_not_implemented():
    provider = OpenStreetMapProvider()

    with pytest.raises(
        NotImplementedError,
        match="OpenStreetMapProvider nearby search is not implemented yet.",
    ):
        provider.nearby(
            location=Location(latitude=6.9147, longitude=79.9729),
            categories=[PlaceCategory.UNIVERSITY],
            radius_km=2,
        )
