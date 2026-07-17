"""Data models used by placekit."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Location:
    """Represents a geographic location using latitude and longitude."""

    latitude: float
    longitude: float


@dataclass(frozen=True)
class Place:
    """Represents a real-world place with a name, category and location."""

    name: str
    category: str
    location: Location


@dataclass(frozen=True)
class Distance:
    """Represents a distance value in different units."""

    km: float
    meters: float
    miles: float
