"""Place category constants used by placekit."""


class PlaceCategory:
    """Common place categories."""

    UNIVERSITY = "university"
    SCHOOL = "school"
    HOSPITAL = "hospital"
    PHARMACY = "pharmacy"
    RESTAURANT = "restaurant"
    CAFE = "cafe"
    SUPERMARKET = "supermarket"
    ATM = "atm"
    BANK = "bank"
    BUS_STOP = "bus_stop"
    TRAIN_STATION = "train_station"
    HOTEL = "hotel"

    @classmethod
    def all(cls) -> list[str]:
        """Return all supported place categories."""
        return [
            cls.UNIVERSITY,
            cls.SCHOOL,
            cls.HOSPITAL,
            cls.PHARMACY,
            cls.RESTAURANT,
            cls.CAFE,
            cls.SUPERMARKET,
            cls.ATM,
            cls.BANK,
            cls.BUS_STOP,
            cls.TRAIN_STATION,
            cls.HOTEL,
        ]
