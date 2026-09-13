"""Tests for OpenStreetMap provider integration."""

from unittest.mock import patch

from placekit import Location, Place, PlaceCategory
from placekit.providers import OpenStreetMapProvider
from placekit.providers.overpass import DEFAULT_OVERPASS_ENDPOINT, DEFAULT_USER_AGENT


def test_openstreetmap_provider_uses_default_configuration():
    provider = OpenStreetMapProvider()

    assert provider.endpoint == DEFAULT_OVERPASS_ENDPOINT
    assert provider.timeout == 25
    assert provider.user_agent == DEFAULT_USER_AGENT


def test_openstreetmap_provider_accepts_custom_configuration():
    provider = OpenStreetMapProvider(
        endpoint="https://example.com/api/interpreter",
        timeout=10,
        user_agent="my-app/1.0",
    )

    assert provider.endpoint == "https://example.com/api/interpreter"
    assert provider.timeout == 10
    assert provider.user_agent == "my-app/1.0"


def test_openstreetmap_provider_nearby_uses_overpass_helpers():
    provider = OpenStreetMapProvider(
        endpoint="https://example.com/api/interpreter",
        timeout=10,
        user_agent="my-app/1.0",
    )
    location = Location(latitude=6.9147, longitude=79.9729)

    parsed_places = [
        Place(
            name="ABC University",
            category=PlaceCategory.UNIVERSITY,
            location=location,
        )
    ]

    with (
        patch(
            "placekit.providers.osm.get_osm_tags",
            return_value={"amenity": "university"},
        ) as mock_get_tags,
        patch(
            "placekit.providers.osm.build_overpass_query",
            return_value="sample query",
        ) as mock_build_query,
        patch(
            "placekit.providers.osm.fetch_overpass_data",
            return_value={"elements": []},
        ) as mock_fetch_data,
        patch(
            "placekit.providers.osm.parse_overpass_response",
            return_value=parsed_places,
        ) as mock_parse_response,
    ):
        places = provider.nearby(
            location=location,
            categories=[PlaceCategory.UNIVERSITY],
            radius_km=2,
            limit=10,
        )

    assert places == parsed_places

    mock_get_tags.assert_called_once_with(PlaceCategory.UNIVERSITY)
    mock_build_query.assert_called_once_with(
        latitude=6.9147,
        longitude=79.9729,
        radius_meters=2000,
        tags={"amenity": "university"},
    )
    mock_fetch_data.assert_called_once_with(
        query="sample query",
        endpoint="https://example.com/api/interpreter",
        timeout=10,
        user_agent="my-app/1.0",
    )
    mock_parse_response.assert_called_once_with(
        data={"elements": []},
        category=PlaceCategory.UNIVERSITY,
    )


def test_openstreetmap_provider_nearby_skips_unsupported_categories():
    provider = OpenStreetMapProvider()
    location = Location(latitude=6.9147, longitude=79.9729)

    with (
        patch(
            "placekit.providers.osm.get_osm_tags", return_value=None
        ) as mock_get_tags,
        patch("placekit.providers.osm.build_overpass_query") as mock_build_query,
        patch("placekit.providers.osm.fetch_overpass_data") as mock_fetch_data,
        patch("placekit.providers.osm.parse_overpass_response") as mock_parse_response,
    ):
        places = provider.nearby(
            location=location,
            categories=["gym"],
            radius_km=2,
        )

    assert places == []

    mock_get_tags.assert_called_once_with("gym")
    mock_build_query.assert_not_called()
    mock_fetch_data.assert_not_called()
    mock_parse_response.assert_not_called()


def test_openstreetmap_provider_nearby_applies_limit():
    provider = OpenStreetMapProvider()
    location = Location(latitude=6.9147, longitude=79.9729)

    parsed_places = [
        Place(name="Place A", category=PlaceCategory.CAFE, location=location),
        Place(name="Place B", category=PlaceCategory.CAFE, location=location),
        Place(name="Place C", category=PlaceCategory.CAFE, location=location),
    ]

    with (
        patch("placekit.providers.osm.get_osm_tags", return_value={"amenity": "cafe"}),
        patch(
            "placekit.providers.osm.build_overpass_query", return_value="sample query"
        ),
        patch(
            "placekit.providers.osm.fetch_overpass_data", return_value={"elements": []}
        ),
        patch(
            "placekit.providers.osm.parse_overpass_response",
            return_value=parsed_places,
        ),
    ):
        places = provider.nearby(
            location=location,
            categories=[PlaceCategory.CAFE],
            radius_km=1,
            limit=2,
        )

    assert places == parsed_places[:2]
