"""placekit-py: A Python toolkit for location-based applications."""

from placekit.distance import distance_between
from placekit.models import Distance, Location, Place
from placekit.exceptions import PlaceKitError, InvalidCoordinateError
from placekit.categories import PlaceCategory
from placekit.client import PlaceKitClient

__version__ = "0.1.0"

__all__ = [
    "Distance",
    "Location",
    "Place",
    "distance_between",
    "InvalidCoordinateError",
    "PlaceKitError",
    "PlaceKitClient",
    "PlaceCategory",
]