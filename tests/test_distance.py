"""Tests for distance calculation utilities."""

from placekit import distance_between


def test_distance_between_same_coordinates():
    distance = distance_between(
        (6.9147, 79.9729),
        (6.9147, 79.9729),
    )

    assert distance.km == 0
    assert distance.meters == 0
    assert distance.miles == 0