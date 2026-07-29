"""Tests for Overpass response parsing utilities."""

from placekit import Location, Place
from placekit.providers.overpass import parse_overpass_response


def test_parse_overpass_response_with_node_element():
    data = {
        "elements": [
            {
                "type": "node",
                "id": 1,
                "lat": 6.9147,
                "lon": 79.9729,
                "tags": {
                    "name": "ABC University",
                    "amenity": "university",
                },
            }
        ]
    }

    places = parse_overpass_response(data, category="university")

    assert places == [
        Place(
            name="ABC University",
            category="university",
            location=Location(latitude=6.9147, longitude=79.9729),
        )
    ]


def test_parse_overpass_response_with_way_center():
    data = {
        "elements": [
            {
                "type": "way",
                "id": 2,
                "center": {
                    "lat": 6.9150,
                    "lon": 79.9730,
                },
                "tags": {
                    "name": "Sample Hospital",
                    "amenity": "hospital",
                },
            }
        ]
    }

    places = parse_overpass_response(data, category="hospital")

    assert places == [
        Place(
            name="Sample Hospital",
            category="hospital",
            location=Location(latitude=6.9150, longitude=79.9730),
        )
    ]


def test_parse_overpass_response_skips_elements_without_name():
    data = {
        "elements": [
            {
                "type": "node",
                "id": 3,
                "lat": 6.9147,
                "lon": 79.9729,
                "tags": {
                    "amenity": "university",
                },
            }
        ]
    }

    places = parse_overpass_response(data, category="university")

    assert places == []


def test_parse_overpass_response_skips_elements_without_location():
    data = {
        "elements": [
            {
                "type": "way",
                "id": 4,
                "tags": {
                    "name": "No Location Place",
                    "amenity": "cafe",
                },
            }
        ]
    }

    places = parse_overpass_response(data, category="cafe")

    assert places == []


def test_parse_overpass_response_with_empty_elements():
    places = parse_overpass_response(data={"elements": []}, category="university")

    assert places == []
