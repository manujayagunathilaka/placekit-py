"""Tests for Google Places type mapping utilities."""

from placekit import PlaceCategory
from placekit.providers.google_types import get_google_place_type


def test_get_google_place_type_for_restaurant():
    assert get_google_place_type(PlaceCategory.RESTAURANT) == "restaurant"


def test_get_google_place_type_for_hospital():
    assert get_google_place_type(PlaceCategory.HOSPITAL) == "hospital"


def test_get_google_place_type_for_pharmacy():
    assert get_google_place_type(PlaceCategory.PHARMACY) == "pharmacy"


def test_get_google_place_type_for_supermarket():
    assert get_google_place_type(PlaceCategory.SUPERMARKET) == "supermarket"


def test_get_google_place_type_for_atm():
    assert get_google_place_type(PlaceCategory.ATM) == "atm"


def test_get_google_place_type_for_bank():
    assert get_google_place_type(PlaceCategory.BANK) == "bank"


def test_get_google_place_type_for_cafe():
    assert get_google_place_type(PlaceCategory.CAFE) == "cafe"


def test_get_google_place_type_for_school():
    assert get_google_place_type(PlaceCategory.SCHOOL) == "school"


def test_get_google_place_type_for_university():
    assert get_google_place_type(PlaceCategory.UNIVERSITY) == "university"


def test_get_google_place_type_returns_none_for_unsupported_category():
    assert get_google_place_type("gym") is None
