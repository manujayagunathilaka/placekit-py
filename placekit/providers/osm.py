"""OpenStreetMap place provider."""

from placekit.models import Location, Place
from placekit.providers.base import BasePlaceProvider
from placekit.providers.osm_tags import get_osm_tags
from placekit.providers.overpass import (
    DEFAULT_OVERPASS_ENDPOINT,
    DEFAULT_USER_AGENT,
    build_overpass_query,
    fetch_overpass_data,
    parse_overpass_response,
)


class OpenStreetMapProvider(BasePlaceProvider):
    """Place provider for OpenStreetMap-based nearby search."""

    def __init__(
        self,
        endpoint: str = DEFAULT_OVERPASS_ENDPOINT,
        timeout: int = 25,
        user_agent: str = DEFAULT_USER_AGENT,
    ) -> None:
        """Create an OpenStreetMap provider."""
        self.endpoint = endpoint
        self.timeout = timeout
        self.user_agent = user_agent

    def nearby(
        self,
        location: Location,
        categories: list[str],
        radius_km: float,
        limit: int = 10,
    ) -> list[Place]:
        """Find nearby places using OpenStreetMap data."""
        places = []
        radius_meters = int(radius_km * 1000)

        for category in categories:
            tags = get_osm_tags(category)

            if tags is None:
                continue

            query = build_overpass_query(
                latitude=location.latitude,
                longitude=location.longitude,
                radius_meters=radius_meters,
                tags=tags,
            )

            data = fetch_overpass_data(
                query=query,
                endpoint=self.endpoint,
                timeout=self.timeout,
                user_agent=self.user_agent,
            )

            parsed_places = parse_overpass_response(
                data=data,
                category=category,
            )

            places.extend(parsed_places)

        return places[:limit]
