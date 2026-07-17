"""Base classes for place providers."""

from placekit.models import Location, Place


class BasePlaceProvider:
    """Base class for nearby place providers."""

    def nearby(
        self,
        location: Location,
        categories: list[str],
        radius_km: float,
        limit: int = 10,
    ) -> list[Place]:
        """Find nearby places around a location."""
        raise NotImplementedError("Providers must implement the nearby method.")
