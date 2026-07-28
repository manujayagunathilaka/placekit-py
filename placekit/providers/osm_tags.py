"""OpenStreetMap tag mappings for place categories."""

from placekit.categories import PlaceCategory

OSM_TAGS_BY_CATEGORY = {
    PlaceCategory.UNIVERSITY: {"amenity": "university"},
    PlaceCategory.SCHOOL: {"amenity": "school"},
    PlaceCategory.HOSPITAL: {"amenity": "hospital"},
    PlaceCategory.PHARMACY: {"amenity": "pharmacy"},
    PlaceCategory.RESTAURANT: {"amenity": "restaurant"},
    PlaceCategory.CAFE: {"amenity": "cafe"},
    PlaceCategory.SUPERMARKET: {"shop": "supermarket"},
    PlaceCategory.ATM: {"amenity": "atm"},
    PlaceCategory.BANK: {"amenity": "bank"},
    PlaceCategory.BUS_STOP: {"highway": "bus_stop"},
    PlaceCategory.TRAIN_STATION: {"railway": "station"},
    PlaceCategory.HOTEL: {"tourism": "hotel"},
}


def get_osm_tags(category: str) -> dict[str, str] | None:
    """Return OpenStreetMap tags for a place category."""
    return OSM_TAGS_BY_CATEGORY.get(category)
