"""Google Places provider."""

from placekit.providers.base import BasePlaceProvider
from placekit.providers.google_places import (
    DEFAULT_GOOGLE_PLACES_ENDPOINT,
    DEFAULT_GOOGLE_PLACES_TIMEOUT,
)


class GooglePlacesProvider(BasePlaceProvider):
    """Place provider for Google Places nearby search."""

    def __init__(
        self,
        api_key: str,
        endpoint: str = DEFAULT_GOOGLE_PLACES_ENDPOINT,
        timeout: int = DEFAULT_GOOGLE_PLACES_TIMEOUT,
    ) -> None:
        """Create a Google Places provider."""
        self.api_key = api_key
        self.endpoint = endpoint
        self.timeout = timeout
