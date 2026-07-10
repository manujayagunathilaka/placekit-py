"""Example usage of the distance calculator."""

from placekit import distance_between


distance = distance_between(
    (6.9147, 79.9729),
    (6.9271, 79.8612),
)

print(f"Distance in kilometers: {distance.km} km")
print(f"Distance in meters: {distance.meters} m")
print(f"Distance in miles: {distance.miles} mi")