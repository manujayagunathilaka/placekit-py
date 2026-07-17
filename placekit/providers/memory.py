"""In-memory place provider."""

from placekit.distance import distance_between
from placekit.models import Location, Place
from placekit.providers.base import BasePlaceProvider


class InMemoryPlaceProvider(BasePlaceProvider):
    """A place provider that searches from an in-memory list of places."""

    def __init__(self, places: list[Place]) -> None:
        self.places = places

    def nearby(
        self,
        location: Location,
        categories: list[str],
        radius_km: float,
        limit: int = 10,
    ) -> list[Place]:
        """Find nearby places from the in-memory place list."""

        filtered_places = []

        for place in self.places:
            if place.category not in categories:
                continue

            distance = distance_between(location, place.location)

            if distance.km <= radius_km:
                filtered_places.append(place)

        def get_place_distance(place: Place) -> float:
            distance = distance_between(location, place.location)
            return distance.km

        filtered_places.sort(key=get_place_distance)

        return filtered_places[:limit]
