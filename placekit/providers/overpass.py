"""Overpass API query building and parsing utilities."""

import requests

from placekit.models import Location, Place

DEFAULT_OVERPASS_ENDPOINT = "https://overpass-api.de/api/interpreter"
DEFAULT_USER_AGENT = "placekit-py/0.1.0"


def build_overpass_query(
    latitude: float,
    longitude: float,
    radius_meters: int,
    tags: dict[str, str],
    timeout: int = 25,
) -> str:
    """Build an Overpass API query for nearby OSM features."""
    tag_filters = "".join(f'["{key}"="{value}"]' for key, value in tags.items())

    return f"""[out:json][timeout:{timeout}];
(
  node{tag_filters}(around:{radius_meters},{latitude},{longitude});
  way{tag_filters}(around:{radius_meters},{latitude},{longitude});
  relation{tag_filters}(around:{radius_meters},{latitude},{longitude});
);
out center;"""


def parse_overpass_response(
    data: dict,
    category: str,
) -> list[Place]:
    """Parse an Overpass API response into Place objects."""
    places = []

    for element in data.get("elements", []):
        tags = element.get("tags", {})
        name = tags.get("name")

        if not name:
            continue

        location = _extract_location(element)

        if location is None:
            continue

        places.append(
            Place(
                name=name,
                category=category,
                location=location,
            )
        )

    return places


def fetch_overpass_data(
    query: str,
    endpoint: str = DEFAULT_OVERPASS_ENDPOINT,
    timeout: int = 25,
    user_agent: str = DEFAULT_USER_AGENT,
) -> dict:
    """Fetch data from the Overpass API."""
    response = requests.post(
        endpoint,
        data={"data": query},
        headers={"User-Agent": user_agent},
        timeout=timeout,
    )

    response.raise_for_status()

    return response.json()


def _extract_location(element: dict) -> Location | None:
    """Extract a Location from an Overpass element."""
    if "lat" in element and "lon" in element:
        return Location(
            latitude=element["lat"],
            longitude=element["lon"],
        )

    center = element.get("center")

    if isinstance(center, dict) and "lat" in center and "lon" in center:
        return Location(
            latitude=center["lat"],
            longitude=center["lon"],
        )

    return None
