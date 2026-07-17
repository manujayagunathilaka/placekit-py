"""Tests for distance calculation utilities."""

import pytest

from placekit import InvalidCoordinateError, Location, distance_between


def test_distance_between_same_coordinates():
    distance = distance_between(
        (6.9147, 79.9729),
        (6.9147, 79.9729),
    )

    assert distance.km == 0
    assert distance.meters == 0
    assert distance.miles == 0


def test_distance_between_two_coordinates():
    distance = distance_between(
        (6.9147, 79.9729),
        (6.9271, 79.8612),
    )

    assert distance.km == 12.407
    assert distance.meters == 12406.83
    assert distance.miles == 7.709


def test_distance_between_invalid_latitude():
    with pytest.raises(
        InvalidCoordinateError, match="Latitude must be between -90 and 90."
    ):
        distance_between(
            (200, 79.9729),
            (6.9271, 79.8612),
        )


def test_distance_between_invalid_longitude():
    with pytest.raises(
        InvalidCoordinateError, match="Longitude must be between -180 and 180."
    ):
        distance_between(
            (6.9147, 200),
            (6.9271, 79.8612),
        )


def test_distance_between_location_objects():
    origin = Location(latitude=6.9147, longitude=79.9729)
    destination = Location(latitude=6.9271, longitude=79.8612)

    distance = distance_between(origin, destination)

    assert distance.km == 12.407
    assert distance.meters == 12406.83
    assert distance.miles == 7.709
