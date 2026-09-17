"""placekit-py: A Python toolkit for location-based applications."""

from placekit.categories import PlaceCategory
from placekit.client import PlaceKitClient
from placekit.distance import distance_between
from placekit.exceptions import (
    InvalidCoordinateError,
    OverpassRequestError,
    OverpassResponseError,
    PlaceKitError,
    ProviderError,
    UnsupportedCategoryError,
)
from placekit.models import Distance, Location, Place

__version__ = "0.11.0"

__all__ = [
    "Distance",
    "Location",
    "Place",
    "distance_between",
    "InvalidCoordinateError",
    "PlaceKitError",
    "PlaceKitClient",
    "PlaceCategory",
    "ProviderError",
    "OverpassRequestError",
    "OverpassResponseError",
    "UnsupportedCategoryError",
]
