"""Main client interface for placekit."""

from placekit.providers.base import BasePlaceProvider


class PlaceKitClient:
    """Main client for working with place providers."""

    def __init__(self, provider: BasePlaceProvider) -> None:
        self.provider = provider