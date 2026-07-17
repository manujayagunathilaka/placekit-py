"""Custom exceptions used by placekit."""


class PlaceKitError(Exception):
    """Base exception for all placekit errors."""


class InvalidCoordinateError(PlaceKitError):
    """Raised when a latitude or longitude value is invalid."""
