"""Command-line interface for placekit-py."""

import argparse

from placekit.distance import distance_between


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
