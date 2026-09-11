"""Tests for the placekit command-line interface."""

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
