"""Distance calculation utilities."""

from math import atan2, cos, radians, sin, sqrt

from placekit.models import Distance


EARTH_RADIUS_KM = 6371.0
KM_TO_MILES = 0.621371


def distance_between(
    origin: tuple[float, float],
    destination: tuple[float, float],
) -> Distance:
    """Calculate the distance between two latitude/longitude coordinates."""
    origin_lat, origin_lon = origin
    destination_lat, destination_lon = destination

    origin_lat_rad = radians(origin_lat)
    origin_lon_rad = radians(origin_lon)
    destination_lat_rad = radians(destination_lat)
    destination_lon_rad = radians(destination_lon)

    lat_difference = destination_lat_rad - origin_lat_rad
    lon_difference = destination_lon_rad - origin_lon_rad

    a = (
        sin(lat_difference / 2) ** 2
        + cos(origin_lat_rad)
        * cos(destination_lat_rad)
        * sin(lon_difference / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance_km = EARTH_RADIUS_KM * c
    distance_meters = distance_km * 1000
    distance_miles = distance_km * KM_TO_MILES

    return Distance(
        km=round(distance_km, 3),
        meters=round(distance_meters, 2),
        miles=round(distance_miles, 3),
    )