# placekit-py

[![CI](https://github.com/manujayagunathilaka/placekit-py/actions/workflows/ci.yml/badge.svg)](https://github.com/manujayagunathilaka/placekit-py/actions/workflows/ci.yml)

A Python toolkit for distance calculations, nearby places, and geolocation provider integrations.

> This project is currently in early development.

## Overview

`placekit-py` is a lightweight Python package for building location-based applications.

It provides reusable utilities and models for working with geographic locations, places, categories, distance calculations, provider-based nearby place search, and command-line usage.

## Why placekit-py?

Many location-based applications need the same basic features:

- Calculating distance between two locations
- Representing locations and places in a clean structure
- Filtering nearby places by category and radius
- Sorting nearby places by distance
- Supporting different place data providers
- Running useful location utilities from the terminal

Developers often rebuild these utilities repeatedly for projects such as real estate platforms, travel applications, delivery tools, campus location systems, local discovery apps, and emergency service tools.

`placekit-py` aims to provide a simple, reusable Python toolkit for these common location-based features.

## Features

Current features:

- Distance calculation between two coordinates
- Distance result in kilometers, meters, and miles
- Coordinate validation
- `Location` object support
- `Place` object support
- Place category constants
- Place category helper methods
- Provider base structure
- `PlaceKitClient` interface
- Client nearby delegation
- In-memory place provider
- OpenStreetMap provider with Overpass API support
- OpenStreetMap provider configuration options
- OpenStreetMap tag mapping for place categories
- Overpass query builder
- Overpass response parser
- Overpass HTTP client helper
- Google Places type mapping helper
- Google Places response parser
- Custom exceptions for invalid coordinates
- Custom provider and Overpass exceptions
- CLI distance command
- CLI nearby search command
- JSON output support for CLI commands
- Automated tests with `pytest`
- Code quality checks with `ruff`
- GitHub Actions CI

Planned features:

- Google Places provider
- PyPI release

## Installation

This package is not published to PyPI yet.

Install from source for local development:

```bash
git clone https://github.com/manujayagunathilaka/placekit-py.git
cd placekit-py
pip install -e .
```

For development work, install with development dependencies:

```bash
pip install -e ".[dev]"
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

## Code Quality

Run Ruff lint checks:

```bash
ruff check .
```

Check code formatting:

```bash
ruff format --check .
```

Format code:

```bash
ruff format .
```

Recommended checks before opening a pull request:

```bash
ruff check .
ruff format --check .
pytest
```

## CLI Usage

`placekit-py` includes a basic command-line interface.

Calculate the distance between two coordinates:

```bash
placekit distance 6.9147 79.9729 6.9271 79.8612
```

Example output:

```text
Distance:
- Kilometers: 12.407 km
- Meters: 12406.83 m
- Miles: 7.709 mi
```

JSON output is also supported:

```bash
placekit distance 6.9147 79.9729 6.9271 79.8612 --format json
```

Example output:

```json
{
  "kilometers": 12.407,
  "meters": 12406.83,
  "miles": 7.709
}
```

Search nearby places using OpenStreetMap:

```bash
placekit nearby --lat 6.9147 --lon 79.9729 --category university --radius 2 --limit 3
```

Example output:

```text
Nearby places:
1. South Asian Institute of Technology (SAITM) - university
2. Sri Lanka Institute of Information Technology (SLIIT) - university
3. Faculty of Computing - university
```

Nearby search also supports JSON output:

```bash
placekit nearby --lat 6.9147 --lon 79.9729 --category university --radius 2 --limit 3 --format json
```

Example output:

```json
[
  {
    "name": "South Asian Institute of Technology (SAITM)",
    "category": "university",
    "latitude": 6.9147,
    "longitude": 79.9729
  }
]
```

> Note: The nearby command uses the Overpass API. Results depend on API availability and OpenStreetMap data coverage.

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

> Note: This calculates direct straight-line distance between two points, not road distance, route distance, or travel time.

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

## Provider Architecture

`placekit-py` is designed to support multiple nearby place providers.

Supported providers:

- In-memory provider
- OpenStreetMap provider

Planned providers:

- Google Places

The provider layer allows the same high-level API to work with different data sources.

Current provider foundation:

```python
from placekit.providers import BasePlaceProvider

provider = BasePlaceProvider()
```

`BasePlaceProvider` defines the expected structure for providers.

Provider implementations should define a `nearby()` method for finding places around a location.

## OpenStreetMap Provider

`placekit-py` includes an `OpenStreetMapProvider` for nearby place search using Overpass API support.

```python
from placekit import Location, PlaceCategory, PlaceKitClient
from placekit.providers import OpenStreetMapProvider

provider = OpenStreetMapProvider()
client = PlaceKitClient(provider=provider)

places = client.nearby(
    location=Location(latitude=6.9147, longitude=79.9729),
    categories=[PlaceCategory.UNIVERSITY],
    radius_km=2,
    limit=5,
)

for place in places:
    print(place.name)
```

You can also customize the Overpass endpoint, timeout, and User-Agent:

```python
from placekit.providers import OpenStreetMapProvider

provider = OpenStreetMapProvider(
    endpoint="https://overpass-api.de/api/interpreter",
    timeout=25,
    user_agent="my-app/1.0",
)
```

Default usage still works:

```python
provider = OpenStreetMapProvider()
```

The OpenStreetMap provider uses:

- OpenStreetMap tag mappings
- Overpass query building
- Overpass HTTP requests
- Overpass response parsing
- `Place` object results

> Note: OpenStreetMap provider requests depend on Overpass API availability and OpenStreetMap data coverage for the selected location and category.

## OpenStreetMap Tag Mapping

`placekit-py` includes an internal mapping layer for converting `PlaceCategory` values into OpenStreetMap tags.

This mapping is used by the OpenStreetMap provider implementation.

Example mappings:

```python
from placekit import PlaceCategory
from placekit.providers.osm_tags import get_osm_tags

print(get_osm_tags(PlaceCategory.UNIVERSITY))
print(get_osm_tags(PlaceCategory.SUPERMARKET))
print(get_osm_tags("gym"))
```

Example output:

```text
{'amenity': 'university'}
{'shop': 'supermarket'}
None
```

Unsupported or custom categories return `None` because they may not have a known OpenStreetMap tag mapping yet.

## Google Places Type Mapping

`placekit-py` includes a Google Places type mapping helper for future Google Places provider support.

This helper converts supported `PlaceCategory` values into Google Places API place types.

```python
from placekit import PlaceCategory
from placekit.providers.google_types import get_google_place_type

print(get_google_place_type(PlaceCategory.RESTAURANT))
print(get_google_place_type(PlaceCategory.HOSPITAL))
print(get_google_place_type("gym"))
```

Example output:

```text
restaurant
hospital
None
```

Unsupported or custom categories return `None` because they may not have a known Google Places type mapping yet.

## Google Places Response Parser

`placekit-py` includes a Google Places response parser for future Google Places provider support.

This helper converts Google Places API response data into `Place` objects.

```python
from placekit.providers.google_places import parse_google_places_response

data = {
    "results": [
        {
            "name": "ABC Restaurant",
            "geometry": {
                "location": {
                    "lat": 6.9147,
                    "lng": 79.9729,
                }
            },
        }
    ]
}

places = parse_google_places_response(
    data=data,
    category="restaurant",
)

print(places)
```

Example output:

```text
[Place(name='ABC Restaurant', category='restaurant', location=Location(latitude=6.9147, longitude=79.9729))]
```

The parser supports:

- Reading place names from Google Places results
- Reading latitude and longitude from `geometry.location`
- Skipping results without a name
- Skipping results without usable coordinates

This parser does not make real HTTP requests. It only converts response data into `Place` objects.

## Overpass Query Builder

`placekit-py` includes an Overpass query builder for OpenStreetMap provider support.

This helper builds Overpass API query strings from a location, radius, and OpenStreetMap tags.

```python
from placekit.providers.overpass import build_overpass_query

query = build_overpass_query(
    latitude=6.9147,
    longitude=79.9729,
    radius_meters=2000,
    tags={"amenity": "university"},
)

print(query)
```

Example output:

```text
[out:json][timeout:25];
(
  node["amenity"="university"](around:2000,6.9147,79.9729);
  way["amenity"="university"](around:2000,6.9147,79.9729);
  relation["amenity"="university"](around:2000,6.9147,79.9729);
);
out center;
```

## Overpass Response Parser

`placekit-py` includes an Overpass response parser for OpenStreetMap provider support.

This helper converts Overpass API JSON response data into `Place` objects.

```python
from placekit.providers.overpass import parse_overpass_response

data = {
    "elements": [
        {
            "type": "node",
            "id": 1,
            "lat": 6.9147,
            "lon": 79.9729,
            "tags": {
                "name": "ABC University",
                "amenity": "university",
            },
        }
    ]
}

places = parse_overpass_response(
    data=data,
    category="university",
)

print(places)
```

Example output:

```text
[Place(name='ABC University', category='university', location=Location(latitude=6.9147, longitude=79.9729))]
```

The parser supports:

- `node` elements with `lat` and `lon`
- `way` elements with `center.lat` and `center.lon`
- `relation` elements with `center.lat` and `center.lon`
- Skipping elements without a name
- Skipping elements without usable coordinates

## Overpass HTTP Client

`placekit-py` includes a small Overpass HTTP client helper for OpenStreetMap provider support.

This helper sends an Overpass query to an Overpass API endpoint and returns JSON response data.

```python
from placekit.providers.overpass import fetch_overpass_data

data = fetch_overpass_data(
    query="[out:json];node(around:1000,6.9147,79.9729);out;",
)

print(data)
```

The helper uses:

- A default Overpass API endpoint
- A custom User-Agent header
- Request timeout handling
- Custom provider exceptions
- JSON response parsing

You can also override the endpoint, timeout, and User-Agent:

```python
from placekit.providers.overpass import fetch_overpass_data

data = fetch_overpass_data(
    query="[out:json];node(around:1000,6.9147,79.9729);out;",
    endpoint="https://overpass-api.de/api/interpreter",
    timeout=10,
    user_agent="my-app/1.0",
)
```

> Note: This helper performs an HTTP request. Unit tests for this helper use mocked HTTP responses and do not call the real Overpass API.

## Client Interface

`placekit-py` provides a `PlaceKitClient` class as the main entry point for provider-based features.

The client accepts a place provider instance.

```python
from placekit import PlaceKitClient
from placekit.providers import BasePlaceProvider

provider = BasePlaceProvider()
client = PlaceKitClient(provider=provider)

print(client.provider)
```

`BasePlaceProvider` is only a base class. Real providers such as `InMemoryPlaceProvider` and `OpenStreetMapProvider` should be used for actual nearby searches.

The client can delegate nearby place searches to the configured provider:

```python
from placekit import Location, PlaceCategory, PlaceKitClient
from placekit.providers import OpenStreetMapProvider

provider = OpenStreetMapProvider()
client = PlaceKitClient(provider=provider)

places = client.nearby(
    location=Location(latitude=6.9147, longitude=79.9729),
    categories=[PlaceCategory.UNIVERSITY],
    radius_km=2,
    limit=10,
)
```

> Note: Calling `nearby()` on `BasePlaceProvider` directly will raise `NotImplementedError`.

## In-Memory Provider

`placekit-py` includes an `InMemoryPlaceProvider` for testing, demos, and local development.

This provider searches from a list of `Place` objects without calling an external API.

```python
from placekit import Location, Place, PlaceCategory, PlaceKitClient
from placekit.providers import InMemoryPlaceProvider

base_location = Location(latitude=6.9147, longitude=79.9729)

places = [
    Place(
        name="ABC University",
        category=PlaceCategory.UNIVERSITY,
        location=Location(latitude=6.9150, longitude=79.9730),
    ),
    Place(
        name="Sample Hospital",
        category=PlaceCategory.HOSPITAL,
        location=Location(latitude=6.9160, longitude=79.9740),
    ),
]

provider = InMemoryPlaceProvider(places=places)
client = PlaceKitClient(provider=provider)

nearby_places = client.nearby(
    location=base_location,
    categories=[PlaceCategory.UNIVERSITY],
    radius_km=1,
    limit=5,
)

for place in nearby_places:
    print(place.name)
```

Example output:

```text
ABC University
```

The in-memory provider supports:

- Category filtering
- Radius filtering
- Nearest-first sorting
- Result limiting

## Error Handling

`placekit-py` provides custom exceptions for package and provider errors.

```python
from placekit import (
    InvalidCoordinateError,
    OverpassRequestError,
    OverpassResponseError,
    PlaceKitError,
    ProviderError,
    UnsupportedCategoryError,
)
```

Provider-related errors inherit from `ProviderError`, which inherits from `PlaceKitError`.

Overpass HTTP request failures raise `OverpassRequestError`.

Invalid or unusable Overpass JSON responses raise `OverpassResponseError`.

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

### `PlaceKitClient`

Main client interface for provider-based features.

```python
from placekit import PlaceKitClient
from placekit.providers import InMemoryPlaceProvider

provider = InMemoryPlaceProvider(places=[])
client = PlaceKitClient(provider=provider)
```

### `BasePlaceProvider`

Base class for implementing nearby place providers.

```python
from placekit.providers import BasePlaceProvider
```

Provider implementations should define a `nearby()` method.

### `InMemoryPlaceProvider`

Provider implementation that searches from an in-memory list of places.

```python
from placekit import Location, Place, PlaceCategory
from placekit.providers import InMemoryPlaceProvider

location = Location(latitude=6.9147, longitude=79.9729)

provider = InMemoryPlaceProvider(
    places=[
        Place(
            name="ABC University",
            category=PlaceCategory.UNIVERSITY,
            location=location,
        )
    ]
)
```

### `OpenStreetMapProvider`

Provider implementation for OpenStreetMap-based nearby place search using Overpass API support.

```python
from placekit.providers import OpenStreetMapProvider

provider = OpenStreetMapProvider()
```

Custom configuration:

```python
provider = OpenStreetMapProvider(
    endpoint="https://overpass-api.de/api/interpreter",
    timeout=25,
    user_agent="my-app/1.0",
)
```

### `get_osm_tags(category)`

Returns OpenStreetMap tags for a supported place category.

```python
from placekit import PlaceCategory
from placekit.providers.osm_tags import get_osm_tags

tags = get_osm_tags(PlaceCategory.UNIVERSITY)
```

Returns:

```python
{"amenity": "university"}
```

Unsupported categories return `None`.

### `get_google_place_type(category)`

Returns the Google Places API place type for a supported place category.

```python
from placekit import PlaceCategory
from placekit.providers.google_types import get_google_place_type

place_type = get_google_place_type(PlaceCategory.RESTAURANT)
```

Returns:

```python
"restaurant"
```

Unsupported categories return `None`.

### `parse_google_places_response(data, category)`

Parses Google Places API response data into `Place` objects.

```python
from placekit.providers.google_places import parse_google_places_response

places = parse_google_places_response(
    data=response_data,
    category="restaurant",
)
```

Returns a list of `Place` objects.

Results without a name or usable coordinates are skipped.

### `build_overpass_query(...)`

Builds an Overpass API query string for nearby OpenStreetMap features.

```python
from placekit.providers.overpass import build_overpass_query

query = build_overpass_query(
    latitude=6.9147,
    longitude=79.9729,
    radius_meters=2000,
    tags={"amenity": "university"},
)
```

Returns an Overpass query string.

The query includes `node`, `way`, and `relation` searches and outputs center coordinates for area-based results.

### `parse_overpass_response(data, category)`

Parses Overpass API response data into `Place` objects.

```python
from placekit.providers.overpass import parse_overpass_response

places = parse_overpass_response(
    data=response_data,
    category="university",
)
```

Returns a list of `Place` objects.

Elements without a name or usable coordinates are skipped.

### `fetch_overpass_data(query, endpoint, timeout, user_agent)`

Sends an Overpass query to an Overpass API endpoint and returns JSON response data.

```python
from placekit.providers.overpass import fetch_overpass_data

data = fetch_overpass_data(query=query)
```

Optional values can be used to override the endpoint, timeout, and User-Agent.

```python
data = fetch_overpass_data(
    query=query,
    endpoint="https://overpass-api.de/api/interpreter",
    timeout=10,
    user_agent="my-app/1.0",
)
```

Raises:

- `OverpassRequestError` for request or HTTP failures
- `OverpassResponseError` for JSON parsing failures

### CLI `placekit distance`

Calculates distance between two coordinates from the terminal.

```bash
placekit distance 6.9147 79.9729 6.9271 79.8612
```

JSON output:

```bash
placekit distance 6.9147 79.9729 6.9271 79.8612 --format json
```

### CLI `placekit nearby`

Searches nearby places from the terminal using OpenStreetMap.

```bash
placekit nearby --lat 6.9147 --lon 79.9729 --category university --radius 2 --limit 3
```

JSON output:

```bash
placekit nearby --lat 6.9147 --lon 79.9729 --category university --radius 2 --limit 3 --format json
```

### `Distance`

Represents a distance value in multiple units.

```python
from placekit import Distance

distance = Distance(km=1.0, meters=1000.0, miles=0.621)
```

### `PlaceKitError`

Base exception for all `placekit-py` errors.

```python
from placekit import PlaceKitError
```

### `InvalidCoordinateError`

Raised when latitude or longitude values are outside the valid coordinate range.

```python
from placekit import InvalidCoordinateError
```

### `ProviderError`

Base exception for provider-related errors.

```python
from placekit import ProviderError
```

### `OverpassRequestError`

Raised when an Overpass API request fails.

```python
from placekit import OverpassRequestError
```

### `OverpassResponseError`

Raised when an Overpass API response cannot be parsed or used.

```python
from placekit import OverpassResponseError
```

### `UnsupportedCategoryError`

Raised when a category is not supported by a provider.

```python
from placekit import UnsupportedCategoryError
```

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
- [x] Add client nearby delegation
- [x] Add in-memory place provider
- [x] Add code quality tooling
- [x] Add GitHub Actions CI
- [x] Add OpenStreetMap provider skeleton
- [x] Add OSM tag mapping for place categories
- [x] Add Overpass query builder
- [x] Add Overpass response parser
- [x] Add Overpass HTTP client
- [x] Implement OpenStreetMap provider with Overpass API
- [x] Add custom provider exceptions
- [x] Add CLI support
- [x] Add nearby search CLI command
- [x] Add JSON output support for CLI commands
- [x] Add OpenStreetMapProvider configuration options
- [x] Add Google Places type mapping
- [x] Add Google Places response parser
- [ ] Add Google Places HTTP client helper
- [ ] Add Google Places provider
- [ ] Publish to PyPI

## Project Status

`placekit-py` is currently in early development.

The `v0.1.0` release focuses on the core foundation:

- Distance calculation
- Location and place models
- Place categories
- Provider architecture
- In-memory nearby place search
- Test and code quality tooling

The `v0.2.0` release adds OpenStreetMap provider support using the Overpass API.

The `v0.2.1` release improves provider error handling.

The `v0.3.0` release adds the CLI distance command.

The `v0.4.0` release adds the CLI nearby search command.

The `v0.5.0` release adds JSON output support for CLI commands.

The `v0.6.0` release adds OpenStreetMap provider configuration options.

The `v0.7.0` release adds Google Places type mapping support.

The next feature release focuses on Google Places response parsing.

Google Places provider implementation is planned for a future release.

## Contributing

Contributions are welcome.

For now, please open an issue before adding large features or changing the public API.

Before opening a pull request, run:

```bash
ruff check .
ruff format --check .
pytest
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history.

## License

This project is licensed under the [MIT License](LICENSE).