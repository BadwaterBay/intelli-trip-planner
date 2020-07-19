#!/usr/bin/env python

"""
Get Distance Matrix from Google Maps
"""

import os
import json
from dotenv import load_dotenv
import googlemaps

load_dotenv()
API_KEY = os.environ.get("API_KEY_GOOGLE")

gmaps = googlemaps.Client(key=API_KEY)

origins = [
    "Las Vegas McCarran International Airport, NV",
    "Los Angeles International Airport",
    "Death Valley Furnace Creek Visitor Center, Furnace Creek, CA",
    "Mojave Kelso Depot Visitor Center, CA",
    "Joshua Tree National Park Visitor Center, Park Boulevard, Joshua Tree, California",
    "Sequoia National Park - Visitor Center, Generals Highway, Three Rivers, CA",
    "Zion National Park Visitor Center, Zion – Mount Carmel Highway, Hurricane, UT",
    "Bryce Canyon National Park Visitor Center, Utah 63, Bryce Canyon City, UT",
    "Grand Canyon North Rim Visitor Center, AZ-67, North Rim, AZ 86023",
    "Grand Canyon Visitor Center, South Entrance Road, Grand Canyon Village, AZ",
]

destinations = origins

# Get distance matrix
distance_matrix = gmaps.distance_matrix(origins, destinations)

# print(distance_matrix)

# Save distance matrix to file
with open("./src/data/distance_matrix.json", "w") as file:
    json.dump(distance_matrix, file, indent=2)
