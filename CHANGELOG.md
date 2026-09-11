# Changelog

All notable changes to this project will be documented in this file.

This project follows semantic versioning where possible.

## [0.2.1] - Unreleased

### Added

- Added provider-related custom exceptions.
- Added `ProviderError` as the base exception for provider-related errors.
- Added `OverpassRequestError` for Overpass request and HTTP failures.
- Added `OverpassResponseError` for Overpass response parsing failures.
- Added `UnsupportedCategoryError` for unsupported provider categories.
- Added tests for provider exception inheritance.

### Changed

- Updated Overpass HTTP client error handling to raise `placekit-py` custom exceptions instead of exposing raw request or parsing errors directly.

### Documentation

- Added README documentation for provider and Overpass error handling.

## [0.2.0] - 2026-09-10

### Added

- Added initial `OpenStreetMapProvider` skeleton.
- Exported `OpenStreetMapProvider` from `placekit.providers`.
- Added tests for the OpenStreetMap provider skeleton.
- Added OpenStreetMap tag mappings for existing `PlaceCategory` values.
- Added `get_osm_tags()` helper for retrieving OSM tags by category.
- Added tests for supported and unsupported OSM tag mappings.
- Added Overpass query builder for OpenStreetMap provider support.
- Added tests for generated Overpass query strings.
- Added support for custom Overpass timeout values.
- Added Overpass response parser for converting response data into `Place` objects.
- Added parsing support for node coordinates and center coordinates from ways and relations.
- Added tests for Overpass response parsing behavior.
- Added Overpass HTTP client helper for sending Overpass API requests.
- Added default Overpass endpoint and User-Agent constants.
- Added timeout, endpoint, and User-Agent override support.
- Added mocked tests for Overpass HTTP behavior without real network calls.
- Integrated `OpenStreetMapProvider.nearby()` with Overpass helpers.
- Added radius conversion from kilometers to meters.
- Added support for category-based OpenStreetMap nearby search using mapped `PlaceCategory` values.
- Added mocked tests for OpenStreetMap provider integration behavior.
- Added `requests` as a runtime dependency.

### Documentation

- Updated README documentation for OpenStreetMap provider usage.
- Updated README documentation for Overpass query building, response parsing, and HTTP client helpers.
- Updated project roadmap for OpenStreetMap provider support.

### Notes

`OpenStreetMapProvider` now supports nearby place search for mapped categories using the Overpass API.

Unit tests use mocked HTTP responses and do not call the real Overpass API.

## [0.1.0] - 2026-07-19

### Added

- Added distance calculation between two geographic coordinates.
- Added `Distance` model with kilometer, meter, and mile values.
- Added `Location` model for latitude and longitude values.
- Added `Place` model for representing real-world places.
- Added coordinate validation for latitude and longitude values.
- Added custom exceptions, including `InvalidCoordinateError`.
- Added `PlaceCategory` constants for common place categories.
- Added `PlaceCategory.all()` helper method.
- Added provider base structure with `BasePlaceProvider`.
- Added `PlaceKitClient` as the main client interface.
- Added client nearby delegation to configured providers.
- Added `InMemoryPlaceProvider` for local demos and tests.
- Added automated tests with `pytest`.
- Added Ruff linting and formatting setup.
- Added GitHub Actions CI workflow.
- Added community health files:
  - `CONTRIBUTING.md`
  - `SECURITY.md`
  - `CODE_OF_CONDUCT.md`

### Documentation

- Added README documentation for installation, development setup, code quality, examples, provider architecture, and API usage.
- Added CI badge to the README.
- Added project status and release scope notes.
- Added linked MIT License reference in the README.

### Notes

This release focuses on the core foundation of `placekit-py`.

External providers such as OpenStreetMap and Google Places are planned for future releases.