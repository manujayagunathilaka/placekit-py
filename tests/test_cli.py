"""Tests for the placekit command-line interface."""

from unittest.mock import patch

from placekit import OverpassRequestError
from placekit.cli import main


def test_cli_distance_command_outputs_distance(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "placekit",
            "distance",
            "6.9147",
            "79.9729",
            "6.9271",
            "79.8612",
        ],
    )

    main()

    output = capsys.readouterr().out

    assert "Distance:" in output
    assert "- Kilometers: 12.407 km" in output
    assert "- Meters: 12406.83 m" in output
    assert "- Miles: 7.709 mi" in output


def test_cli_nearby_command_handles_overpass_request_error(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "placekit",
            "nearby",
            "--lat",
            "6.9147",
            "--lon",
            "79.9729",
            "--category",
            "university",
            "--radius",
            "2",
        ],
    )

    with patch(
        "placekit.cli.PlaceKitClient.nearby",
        side_effect=OverpassRequestError("Failed to fetch data from Overpass API."),
    ):
        main()

    output = capsys.readouterr().out

    assert "Error: Failed to fetch data from Overpass API." in output
