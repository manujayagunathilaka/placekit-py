"""Tests for Google Places response parsing utilities."""

from placekit import Location, Place
from placekit.providers.google_places import parse_google_places_response


def test_parse_google_places_response_returns_places():
    data = {
        "results": [
            {
                "name": "ABC Restaurant",
                "geometry": {
                    "location": {
                        "lat": 6.9147,
                        "lng": 79.9729,
                    }
                },
            }
        ]
    }

    places = parse_google_places_response(
        data=data,
        category="restaurant",
    )

    assert places == [
        Place(
            name="ABC Restaurant",
            category="restaurant",
            location=Location(latitude=6.9147, longitude=79.9729),
        )
    ]


def test_parse_google_places_response_skips_results_without_name():
    data = {
        "results": [
            {
                "geometry": {
                    "location": {
                        "lat": 6.9147,
                        "lng": 79.9729,
                    }
                },
            }
        ]
    }

    places = parse_google_places_response(
        data=data,
        category="restaurant",
    )

    assert places == []


def test_parse_google_places_response_skips_results_without_location():
    data = {
        "results": [
            {
                "name": "ABC Restaurant",
            }
        ]
    }

    places = parse_google_places_response(
        data=data,
        category="restaurant",
    )

    assert places == []


def test_parse_google_places_response_skips_results_without_latitude():
    data = {
        "results": [
            {
                "name": "ABC Restaurant",
                "geometry": {
                    "location": {
                        "lng": 79.9729,
                    }
                },
            }
        ]
    }

    places = parse_google_places_response(
        data=data,
        category="restaurant",
    )

    assert places == []


def test_parse_google_places_response_skips_results_without_longitude():
    data = {
        "results": [
            {
                "name": "ABC Restaurant",
                "geometry": {
                    "location": {
                        "lat": 6.9147,
                    }
                },
            }
        ]
    }

    places = parse_google_places_response(
        data=data,
        category="restaurant",
    )

    assert places == []


def test_parse_google_places_response_returns_empty_list_for_empty_results():
    data = {"results": []}

    places = parse_google_places_response(
        data=data,
        category="restaurant",
    )

    assert places == []


def test_parse_google_places_response_returns_empty_list_when_results_missing():
    data = {}

    places = parse_google_places_response(
        data=data,
        category="restaurant",
    )

    assert places == []
