"""Tests for OpenStreetMap provider integration."""

from unittest.mock import patch

from placekit import Location, Place, PlaceCategory
from placekit.providers import OpenStreetMapProvider


def test_openstreetmap_provider_nearby_uses_overpass_helpers():
    provider = OpenStreetMapProvider()
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
    mock_fetch_data.assert_called_once_with(query="sample query")
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


def test_openstreetmap_provider_nearby_stops_after_limit_is_reached():
    provider = OpenStreetMapProvider()
    location = Location(latitude=6.9147, longitude=79.9729)

    parsed_places = [
        Place(name="Cafe A", category=PlaceCategory.CAFE, location=location),
        Place(name="Cafe B", category=PlaceCategory.CAFE, location=location),
    ]

    with (
        patch(
            "placekit.providers.osm.get_osm_tags",
            side_effect=[{"amenity": "cafe"}, {"amenity": "restaurant"}],
        ) as mock_get_tags,
        patch(
            "placekit.providers.osm.build_overpass_query",
            return_value="sample query",
        ),
        patch(
            "placekit.providers.osm.fetch_overpass_data",
            return_value={"elements": []},
        ) as mock_fetch_data,
        patch(
            "placekit.providers.osm.parse_overpass_response",
            return_value=parsed_places,
        ),
    ):
        places = provider.nearby(
            location=location,
            categories=[PlaceCategory.CAFE, PlaceCategory.RESTAURANT],
            radius_km=1,
            limit=2,
        )

    assert places == parsed_places
    assert mock_get_tags.call_count == 1
    assert mock_fetch_data.call_count == 1


def test_openstreetmap_provider_nearby_returns_empty_list_for_zero_limit():
    provider = OpenStreetMapProvider()
    location = Location(latitude=6.9147, longitude=79.9729)

    with (
        patch("placekit.providers.osm.get_osm_tags") as mock_get_tags,
        patch("placekit.providers.osm.build_overpass_query") as mock_build_query,
        patch("placekit.providers.osm.fetch_overpass_data") as mock_fetch_data,
        patch("placekit.providers.osm.parse_overpass_response") as mock_parse_response,
    ):
        places = provider.nearby(
            location=location,
            categories=[PlaceCategory.CAFE],
            radius_km=1,
            limit=0,
        )

    assert places == []
    mock_get_tags.assert_not_called()
    mock_build_query.assert_not_called()
    mock_fetch_data.assert_not_called()
    mock_parse_response.assert_not_called()
