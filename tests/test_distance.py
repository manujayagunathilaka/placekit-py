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


def test_distance_between_two_coordinates():
    distance = distance_between(
        (6.9147, 79.9729),
        (6.9271, 79.8612),
    )

    assert distance.km == 12.407
    assert distance.meters == 12406.83
    assert distance.miles == 7.709