"""Tests for custom exceptions."""

from placekit import (
    InvalidCoordinateError,
    OverpassRequestError,
    OverpassResponseError,
    PlaceKitError,
    ProviderError,
    UnsupportedCategoryError,
)


def test_invalid_coordinate_error_inherits_from_placekit_error():
    assert issubclass(InvalidCoordinateError, PlaceKitError)


def test_provider_error_inherits_from_placekit_error():
    assert issubclass(ProviderError, PlaceKitError)


def test_overpass_request_error_inherits_from_provider_error():
    assert issubclass(OverpassRequestError, ProviderError)


def test_overpass_response_error_inherits_from_provider_error():
    assert issubclass(OverpassResponseError, ProviderError)


def test_unsupported_category_error_inherits_from_provider_error():
    assert issubclass(UnsupportedCategoryError, ProviderError)
