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
- Coordinate validation
- `Location` object support
- `Place` object support
- Place category constants
- Place category helper methods
- Custom exceptions for invalid coordinates
- Automated tests with `pytest`

Planned features:

- Nearby places finder
- Provider support for OpenStreetMap and Google Places
- CLI support
- PyPI release

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

## Using Location Objects

In addition to coordinate tuples, `placekit-py` also supports `Location` objects.

```python
from placekit import Location, distance_between

origin = Location(latitude=6.9147, longitude=79.9729)
destination = Location(latitude=6.9271, longitude=79.8612)

distance = distance_between(origin, destination)

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

## Using Place Objects

`placekit-py` provides a `Place` model for representing real-world places.

A `Place` includes:

- `name`: The name of the place
- `category`: The type or category of the place
- `location`: A `Location` object containing latitude and longitude

```python
from placekit import Location, Place

place = Place(
    name="ABC University",
    category="university",
    location=Location(latitude=6.9147, longitude=79.9729),
)

print(place.name)
print(place.category)
print(place.location.latitude)
print(place.location.longitude)
```

Example output:

```text
ABC University
university
6.9147
79.9729
```

## Using Place Categories

`placekit-py` provides common place category constants through `PlaceCategory`.

These constants are provided for convenience and to reduce spelling mistakes. You can still use custom category strings when needed.

```python
from placekit import Location, Place, PlaceCategory

place = Place(
    name="ABC University",
    category=PlaceCategory.UNIVERSITY,
    location=Location(latitude=6.9147, longitude=79.9729),
)

print(place.name)
print(place.category)
```

Example output:

```text
ABC University
university
```

Custom categories are also allowed:

```python
from placekit import Location, Place

place = Place(
    name="Sample Gym",
    category="gym",
    location=Location(latitude=6.9147, longitude=79.9729),
)

print(place.category)
```

Example output:

```text
gym
```

You can also list the built-in categories:

```python
from placekit import PlaceCategory

categories = PlaceCategory.all()

print(categories)
```

Example output:

```text
['university', 'school', 'hospital', 'pharmacy', 'restaurant', 'cafe', 'supermarket', 'atm', 'bank', 'bus_stop', 'train_station', 'hotel']
```

## Coordinate Validation

`placekit-py` validates latitude and longitude values before calculating distance.

Valid coordinate ranges:

- Latitude: `-90` to `90`
- Longitude: `-180` to `180`

If an invalid coordinate is provided, `InvalidCoordinateError` will be raised.

```python
from placekit import InvalidCoordinateError, distance_between

try:
    distance = distance_between(
        (200, 79.9729),
        (6.9271, 79.8612),
    )
except InvalidCoordinateError as error:
    print(error)
```

Example output:

```text
Latitude must be between -90 and 90.
```

## API Reference

### `distance_between(origin, destination)`

Calculates the straight-line distance between two geographic coordinates.

The `origin` and `destination` values can be either coordinate tuples or `Location` objects.

Tuple example:

```python
from placekit import distance_between

distance = distance_between(
    (6.9147, 79.9729),
    (6.9271, 79.8612),
)
```

`Location` object example:

```python
from placekit import Location, distance_between

distance = distance_between(
    Location(latitude=6.9147, longitude=79.9729),
    Location(latitude=6.9271, longitude=79.8612),
)
```

Returns a `Distance` object:

```python
Distance(km=12.407, meters=12406.83, miles=7.709)
```

### `Location`

Represents a geographic location using latitude and longitude.

```python
from placekit import Location

location = Location(latitude=6.9147, longitude=79.9729)
```

### `Place`

Represents a place with a name, category, and location.

```python
from placekit import Location, Place

place = Place(
    name="ABC University",
    category="university",
    location=Location(latitude=6.9147, longitude=79.9729),
)
```

### `PlaceCategory`

Provides common place category constants.

```python
from placekit import PlaceCategory

category = PlaceCategory.UNIVERSITY
```

List all built-in categories:

```python
from placekit import PlaceCategory

categories = PlaceCategory.all()
```

### `Distance`

Represents a distance value in multiple units.

```python
from placekit import Distance

distance = Distance(km=1.0, meters=1000.0, miles=0.621)
```

### `InvalidCoordinateError`

Raised when latitude or longitude values are outside the valid coordinate range.

```python
from placekit import InvalidCoordinateError
```

## Provider Architecture

`placekit-py` is designed to support multiple nearby place providers in the future.

Planned providers include:

- OpenStreetMap
- Google Places

The provider layer will allow the same high-level API to work with different data sources.

Current provider foundation:

```python
from placekit.providers.base import BasePlaceProvider

provider = BasePlaceProvider()
```

`BasePlaceProvider` defines the expected structure for future providers.

Provider implementations should define a `nearby()` method for finding places around a location.


## Client Interface

`placekit-py` provides a `PlaceKitClient` class as the main entry point for provider-based features.

The client accepts a place provider instance.

```python
from placekit import PlaceKitClient
from placekit.providers.base import BasePlaceProvider

provider = BasePlaceProvider()
client = PlaceKitClient(provider=provider)

print(client.provider)
```

`BasePlaceProvider` is only a base class. Real providers such as OpenStreetMap and Google Places will be added in future versions.

## Roadmap

- [x] Add distance model
- [x] Add distance calculator
- [x] Add example usage
- [x] Add automated tests
- [x] Add development dependencies
- [x] Add coordinate validation
- [x] Add custom exceptions
- [x] Add `Location` model
- [x] Add `Location` object support for distance calculation
- [x] Add `Place` model
- [x] Add place category constants
- [x] Add place category helper methods
- [x] Add provider base structure
- [x] Add client skeleton
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