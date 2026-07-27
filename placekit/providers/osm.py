"""OpenStreetMap place provider."""

from placekit.models import Location, Place
from placekit.providers.base import BasePlaceProvider


class OpenStreetMapProvider(BasePlaceProvider):
    """Place provider for OpenStreetMap-based nearby search."""

    def nearby(
        self,
        location: Location,
        categories: list[str],
        radius_km: float,
        limit: int = 10,
    ) -> list[Place]:
        """Find nearby places using OpenStreetMap data."""
        raise NotImplementedError(
            "OpenStreetMapProvider nearby search is not implemented yet."
        )
