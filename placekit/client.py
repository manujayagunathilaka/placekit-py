"""Main client interface for placekit."""

from placekit.models import Location, Place
from placekit.providers.base import BasePlaceProvider


class PlaceKitClient:
    """Main client for working with place providers."""

    def __init__(self, provider: BasePlaceProvider) -> None:
        self.provider = provider

    def nearby(
        self,
        location: Location,
        categories: list[str],
        radius_km: float,
        limit: int = 10,
    ) -> list[Place]:
        """Find nearby places using the configured provider."""
        return self.provider.nearby(
            location=location, categories=categories, radius_km=radius_km, limit=limit
        )
