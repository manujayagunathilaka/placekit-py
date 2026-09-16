"""Google Places response parsing utilities."""

from placekit.models import Location, Place


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
