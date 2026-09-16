"""Google Places response parsing and HTTP utilities."""

import requests

from placekit.exceptions import OverpassRequestError, OverpassResponseError
from placekit.models import Location, Place

DEFAULT_GOOGLE_PLACES_ENDPOINT = (
    "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
)
DEFAULT_GOOGLE_PLACES_TIMEOUT = 25


def fetch_google_places_data(
    api_key: str,
    latitude: float,
    longitude: float,
    radius_meters: int,
    place_type: str,
    endpoint: str = DEFAULT_GOOGLE_PLACES_ENDPOINT,
    timeout: int = DEFAULT_GOOGLE_PLACES_TIMEOUT,
) -> dict:
    """Fetch nearby place data from the Google Places API."""
    try:
        response = requests.get(
            endpoint,
            params={
                "key": api_key,
                "location": f"{latitude},{longitude}",
                "radius": radius_meters,
                "type": place_type,
            },
            timeout=timeout,
        )
        response.raise_for_status()
    except requests.RequestException as error:
        raise OverpassRequestError(
            "Failed to fetch data from Google Places API."
        ) from error

    try:
        return response.json()
    except ValueError as error:
        raise OverpassResponseError(
            "Failed to parse Google Places API response."
        ) from error


def parse_google_places_response(data: dict, category: str) -> list[Place]:
    """Parse Google Places API response data into Place objects."""
    places = []

    for result in data.get("results", []):
        name = result.get("name")
        location_data = result.get("geometry", {}).get("location", {})

        latitude = location_data.get("lat")
        longitude = location_data.get("lng")

        if not name:
            continue

        if latitude is None or longitude is None:
            continue

        places.append(
            Place(
                name=name,
                category=category,
                location=Location(
                    latitude=latitude,
                    longitude=longitude,
                ),
            )
        )

    return places
