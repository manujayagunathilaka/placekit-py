"""Google Places type mapping utilities."""

from placekit.categories import PlaceCategory

GOOGLE_PLACE_TYPES = {
    PlaceCategory.RESTAURANT: "restaurant",
    PlaceCategory.HOSPITAL: "hospital",
    PlaceCategory.PHARMACY: "pharmacy",
    PlaceCategory.SUPERMARKET: "supermarket",
    PlaceCategory.ATM: "atm",
    PlaceCategory.BANK: "bank",
    PlaceCategory.CAFE: "cafe",
    PlaceCategory.SCHOOL: "school",
    PlaceCategory.UNIVERSITY: "university",
}


def get_google_place_type(category: str) -> str | None:
    """Return the Google Places type for a supported category."""
    return GOOGLE_PLACE_TYPES.get(category)
