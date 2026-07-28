"""Overpass API query building utilities."""


def build_overpass_query(
    latitude: float,
    longitude: float,
    radius_meters: int,
    tags: dict[str, str],
    timeout: int = 25,
) -> str:
    """Build an Overpass API query for nearby OSM features."""
    tag_filters = "".join(f'["{key}"="{value}"]' for key, value in tags.items())

    return f"""[out:json][timeout:{timeout}];
            (
              node{tag_filters}(around:{radius_meters},{latitude},{longitude});
              way{tag_filters}(around:{radius_meters},{latitude},{longitude});
              relation{tag_filters}(around:{radius_meters},{latitude},{longitude});
            );
            out center;"""
