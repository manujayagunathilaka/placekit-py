# placekit-py

A Python toolkit for distance calculations, nearby places, and geolocation provider integrations.

> This project is currently in early development.

## Overview

`placekit-py` is a lightweight Python package for building location-based applications.

It is designed to help developers work with:

- Distance calculations
- Nearby places
- Geolocation providers
- Location-based app utilities

This package can be useful for projects such as:

- Boarding and hostel finder apps
- Real estate applications
- Travel applications
- Delivery applications
- Campus location apps
- Emergency service apps

## Features

Current features:

- Distance calculation between two coordinates
- Distance result in kilometers, meters, and miles

Planned features:

- Location and place data models
- Nearby places finder
- Provider support for OpenStreetMap and Google Places
- CLI support

## Installation

This package is not published to PyPI yet.

For local development:

```bash
git clone https://github.com/manujayagunathilaka/placekit-py.git
cd placekit-py
```

## Development Setup

Clone the repository:

```bash
git clone https://github.com/manujayagunathilaka/placekit-py.git
cd placekit-py
```

Install the package in editable mode with development dependencies:

```bash
pip install -e ".[dev]"
```

Run the tests:

```bash
pytest
```

Run the distance example:

```bash
python examples/distance_example.py
```

## Quick Example

```python
from placekit import distance_between

distance = distance_between(
    (6.9147, 79.9729),
    (6.9271, 79.8612),
)

print(distance.km)
print(distance.meters)
print(distance.miles)
```

Example output:

```text
12.407
12406.83
7.709
```

## Distance Calculation

`placekit-py` currently provides a simple straight-line distance calculator using latitude and longitude coordinates.

This calculates the direct distance between two points, not road or travel distance.

```python
from placekit import distance_between

distance = distance_between(
    (6.9147, 79.9729),
    (6.9271, 79.8612),
)

print(f"{distance.km} km")
```

## Roadmap

- [x] Add distance model
- [x] Add distance calculator
- [x] Add example usage
- [x] Add automated tests
- [x] Add development dependencies
- [ ] Add location and place data models
- [ ] Add geocoding support
- [ ] Add nearby places finder
- [ ] Add OpenStreetMap provider
- [ ] Add Google Places provider
- [ ] Add CLI support
- [ ] Publish to PyPI

## Project Status

This project is in the initial development stage.

The first milestone is focused on building a simple and reliable distance calculation utility before adding external geolocation providers.

## Contributing

Contributions are welcome.

Since this project is still in early development, please open an issue before adding large features or changing the core API design.

## License

This project is licensed under the MIT License.