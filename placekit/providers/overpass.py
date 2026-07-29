"""Overpass API query building and parsing utilities."""

from placekit.models import Location, Place


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
