"""Google Places provider."""

from placekit.models import Location, Place
from placekit.providers.base import BasePlaceProvider
from placekit.providers.google_places import (
    DEFAULT_GOOGLE_PLACES_ENDPOINT,
    DEFAULT_GOOGLE_PLACES_TIMEOUT,
    fetch_google_places_data,
    parse_google_places_response,
)
from placekit.providers.google_types import get_google_place_type


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

    def nearby(
        self,
        location: Location,
        categories: list[str],
        radius_km: float,
        limit: int = 10,
    ) -> list[Place]:
        """Find nearby places using Google Places data."""
        places = []
        radius_meters = int(radius_km * 1000)

        for category in categories:
            place_type = get_google_place_type(category)

            if place_type is None:
                continue

            data = fetch_google_places_data(
                api_key=self.api_key,
                latitude=location.latitude,
                longitude=location.longitude,
                radius_meters=radius_meters,
                place_type=place_type,
                endpoint=self.endpoint,
                timeout=self.timeout,
            )

            parsed_places = parse_google_places_response(
                data=data,
                category=category,
            )

            places.extend(parsed_places)

        return places[:limit]
