"""Data models used by placekit."""

from dataclasses import dataclass

@dataclass(frozen=True)
class Location:
    """Represents a geographic location using latitude and longitude."""

    latitude: float
    longitude: float


@dataclass(frozen=True)
class Distance:
    """Represents a distance value in different units."""

    km: float
    meters: float
    miles: float