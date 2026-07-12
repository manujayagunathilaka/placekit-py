from placekit import Location, Place


def test_place_mode():
    location = Location(latitude=6.9147, longitude=79.9729)

    place = Place(
        name = "ABC University",
        category = "university",
        location = location,
    )

    assert place.name == "ABC University"
    assert place.category == "university"
    assert place.location == location
    assert place.location.latitude == 6.9147
    assert place.location.longitude == 79.9729