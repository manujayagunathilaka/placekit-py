"""Custom exceptions for placekit."""


class PlaceKitError(Exception):
    """Base exception for placekit errors."""


class InvalidCoordinateError(PlaceKitError):
    """Raised when a coordinate value is invalid."""


class ProviderError(PlaceKitError):
    """Base exception for provider-related errors."""


class OverpassRequestError(ProviderError):
    """Raised when an Overpass API request fails."""


class OverpassResponseError(ProviderError):
    """Raised when an Overpass API response cannot be used."""


class UnsupportedCategoryError(ProviderError):
    """Raised when a category is not supported by a provider."""
