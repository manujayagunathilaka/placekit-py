"""Tests for the placekit command-line interface."""

from unittest.mock import patch

from placekit import Location, OverpassRequestError, Place, PlaceCategory
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


def test_cli_distance_command_outputs_json(capsys, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "placekit",
            "distance",
            "6.9147",
            "79.9729",
            "6.9271",
            "79.8612",
            "--format",
            "json",
        ],
    )

    main()

    output = capsys.readouterr().out

    assert '"kilometers": 12.407' in output
    assert '"meters": 12406.83' in output
    assert '"miles": 7.709' in output


def test_cli_nearby_command_outputs_json(capsys, monkeypatch):
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
            "--limit",
            "1",
            "--format",
            "json",
        ],
    )

    places = [
        Place(
            name="ABC University",
            category=PlaceCategory.UNIVERSITY,
            location=Location(latitude=6.9147, longitude=79.9729),
        )
    ]

    with patch("placekit.cli.PlaceKitClient.nearby", return_value=places):
        main()

    output = capsys.readouterr().out

    assert '"name": "ABC University"' in output
    assert '"category": "university"' in output
    assert '"latitude": 6.9147' in output
    assert '"longitude": 79.9729' in output


def test_cli_nearby_command_outputs_empty_json(capsys, monkeypatch):
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
            "--format",
            "json",
        ],
    )

    with patch("placekit.cli.PlaceKitClient.nearby", return_value=[]):
        main()

    output = capsys.readouterr().out

    assert output.strip() == "[]"
