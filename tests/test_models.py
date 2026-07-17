from placekit import Location, Place, PlaceCategory


def test_place_mode():
    location = Location(latitude=6.9147, longitude=79.9729)

    place = Place(
        name="ABC University",
        category="university",
        location=location,
    )

    assert place.name == "ABC University"
    assert place.category == "university"
    assert place.location == location
    assert place.location.latitude == 6.9147
    assert place.location.longitude == 79.9729


def test_place_category_constants():
    assert PlaceCategory.UNIVERSITY == "university"
    assert PlaceCategory.HOSPITAL == "hospital"
    assert PlaceCategory.BUS_STOP == "bus_stop"


def test_place_model_with_place_category():
    location = Location(latitude=6.9147, longitude=79.9729)

    place = Place(
        name="ABC University",
        category=PlaceCategory.UNIVERSITY,
        location=location,
    )

    assert place.name == "ABC University"
    assert place.category == "university"
    assert place.location == location


def test_place_category_all():
    categories = PlaceCategory.all()

    assert "university" in categories
    assert "hospital" in categories
    assert "bus_stop" in categories
    assert "hotel" in categories
    assert len(categories) == 12
