"""Distance calculation utilities."""

from math import atan2, cos, radians, sin, sqrt

from placekit.exceptions import InvalidCoordinateError
from placekit.models import Distance, Location

EARTH_RADIUS_KM = 6371.0
KM_TO_MILES = 0.621371


def _normalize_coordinate(
    coordinate: tuple[float, float] | Location,
) -> tuple[float, float]:
    """Normalize a coordinate input into a latitude/logitude tuple."""
    if isinstance(coordinate, Location):
        return coordinate.latitude, coordinate.longitude

    return coordinate


def _validate_coordinate(coordinate: tuple[float, float]) -> None:
    """Validate a latitude/longitude coordinate pair."""
    latitude, longitude = coordinate

    if not -90 <= latitude <= 90:
        raise InvalidCoordinateError("Latitude must be between -90 and 90.")

    if not -180 <= longitude <= 180:
        raise InvalidCoordinateError("Longitude must be between -180 and 180.")


def distance_between(
    origin: tuple[float, float] | Location,
    destination: tuple[float, float] | Location,
) -> Distance:
    """Calculate the distance between two latitude/longitude coordinates."""
    origin_coordinate = _normalize_coordinate(origin)
    destination_coordinate = _normalize_coordinate(destination)

    _validate_coordinate(origin_coordinate)
    _validate_coordinate(destination_coordinate)

    origin_lat, origin_lon = origin_coordinate
    destination_lat, destination_lon = destination_coordinate

    origin_lat_rad = radians(origin_lat)
    origin_lon_rad = radians(origin_lon)
    destination_lat_rad = radians(destination_lat)
    destination_lon_rad = radians(destination_lon)

    lat_difference = destination_lat_rad - origin_lat_rad
    lon_difference = destination_lon_rad - origin_lon_rad

    a = (
        sin(lat_difference / 2) ** 2
        + cos(origin_lat_rad) * cos(destination_lat_rad) * sin(lon_difference / 2) ** 2
    )
    a = min(1.0, max(0.0, a))

    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance_km = EARTH_RADIUS_KM * c
    distance_meters = distance_km * 1000
    distance_miles = distance_km * KM_TO_MILES

    return Distance(
        km=round(distance_km, 3),
        meters=round(distance_meters, 2),
        miles=round(distance_miles, 3),
    )
