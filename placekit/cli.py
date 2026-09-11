"""Command-line interface for placekit-py."""

import argparse

from placekit.client import PlaceKitClient
from placekit.distance import distance_between
from placekit.exceptions import OverpassRequestError, OverpassResponseError
from placekit.models import Location
from placekit.providers import OpenStreetMapProvider


def main() -> None:
    """Run the placekit command-line interface."""
    parser = argparse.ArgumentParser(
        prog="placekit",
        description="Location utilities from placekit-py.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    distance_parser = subparsers.add_parser(
        "distance",
        help="Calculate distance between two coordinates.",
    )
    distance_parser.add_argument("origin_lat", type=float)
    distance_parser.add_argument("origin_lon", type=float)
    distance_parser.add_argument("destination_lat", type=float)
    distance_parser.add_argument("destination_lon", type=float)

    nearby_parser = subparsers.add_parser(
        "nearby",
        help="Search nearby places using OpenStreetMap.",
    )
    nearby_parser.add_argument("--lat", type=float, required=True)
    nearby_parser.add_argument("--lon", type=float, required=True)
    nearby_parser.add_argument("--category", required=True)
    nearby_parser.add_argument("--radius", type=float, required=True)
    nearby_parser.add_argument("--limit", type=int, default=10)

    args = parser.parse_args()

    if args.command == "distance":
        distance = distance_between(
            (args.origin_lat, args.origin_lon),
            (args.destination_lat, args.destination_lon),
        )

        print("Distance:")
        print(f"- Kilometers: {distance.km} km")
        print(f"- Meters: {distance.meters} m")
        print(f"- Miles: {distance.miles} mi")

    if args.command == "nearby":
        client = PlaceKitClient(OpenStreetMapProvider())

        try:
            places = client.nearby(
                location=Location(latitude=args.lat, longitude=args.lon),
                categories=[args.category],
                radius_km=args.radius,
                limit=args.limit,
            )
        except OverpassRequestError as error:
            print(f"Error: {error}")
            return
        except OverpassResponseError as error:
            print(f"Error: {error}")
            return

        if not places:
            print("No nearby places found.")
            return

        print("Nearby places:")

        for index, place in enumerate(places, start=1):
            print(f"{index}. {place.name} - {place.category}")
