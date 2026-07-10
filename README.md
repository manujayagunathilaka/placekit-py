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

Current planned features:

- Distance calculation between two coordinates
- Location and distance data models
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

## Quick Example

```python
from placekit import distance_between

distance = distance_between(
    (6.9147, 79.9729),
    (6.9271, 79.8612)
)

print(distance.km)
print(distance.meters)
```

## Roadmap

- [ ] Add distance calculator
- [ ] Add data models
- [ ] Add tests
- [ ] Add examples
- [ ] Add geocoding support
- [ ] Add nearby places finder
- [ ] Add OpenStreetMap provider
- [ ] Add Google Places provider
- [ ] Add CLI support

## Project Status

This project is in the initial development stage.

The first milestone is focused on building a simple and reliable distance calculation utility before adding external geolocation providers.

## Contributing

Contributions are welcome.

Since this project is still in early development, please open an issue before adding large features or changing the core API design.

## License

This project is licensed under the MIT License.