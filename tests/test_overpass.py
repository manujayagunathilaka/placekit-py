"""Tests for Overpass query building utilities."""

from placekit.providers.overpass import build_overpass_query


def test_build_overpass_query_for_single_tag():
    query = build_overpass_query(
        latitude=6.9147,
        longitude=79.9729,
        radius_meters=2000,
        tags={"amenity": "university"},
    )

    assert "[out:json][timeout:25];" in query
    assert 'node["amenity"="university"](around:2000,6.9147,79.9729);' in query
    assert 'way["amenity"="university"](around:2000,6.9147,79.9729);' in query
    assert 'relation["amenity"="university"](around:2000,6.9147,79.9729);' in query
    assert "out center;" in query


def test_build_overpass_query_with_custom_timeout():
    query = build_overpass_query(
        latitude=6.9147,
        longitude=79.9729,
        radius_meters=1000,
        tags={"amenity": "hospital"},
        timeout=10,
    )

    assert "[out:json][timeout:10];" in query
    assert 'node["amenity"="hospital"](around:1000,6.9147,79.9729);' in query


def test_build_overpass_query_for_shop_tag():
    query = build_overpass_query(
        latitude=6.9147,
        longitude=79.9729,
        radius_meters=1500,
        tags={"shop": "supermarket"},
    )

    assert 'node["shop"="supermarket"](around:1500,6.9147,79.9729);' in query
    assert 'way["shop"="supermarket"](around:1500,6.9147,79.9729);' in query
    assert 'relation["shop"="supermarket"](around:1500,6.9147,79.9729);' in query
