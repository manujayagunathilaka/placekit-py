"""Tests for OpenStreetMap tag mappings."""

from placekit import PlaceCategory
from placekit.providers.osm_tags import get_osm_tags


def test_get_osm_tags_for_supported_category():
    tags = get_osm_tags(PlaceCategory.UNIVERSITY)

    assert tags == {"amenity": "university"}


def test_get_osm_tags_for_shop_category():
    tags = get_osm_tags(PlaceCategory.SUPERMARKET)

    assert tags == {"shop": "supermarket"}


def test_get_osm_tags_for_transport_category():
    tags = get_osm_tags(PlaceCategory.BUS_STOP)

    assert tags == {"highway": "bus_stop"}


def test_get_osm_tags_for_unsupported_category():
    tags = get_osm_tags("gym")

    assert tags is None
