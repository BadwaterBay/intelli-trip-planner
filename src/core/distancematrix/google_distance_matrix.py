#!/usr/bin/env python

"""
# Get distance matrices from Google Maps API and process the response
"""

import os
from typing import List, Tuple
from dotenv import load_dotenv
import googlemaps


async def get_distancematrix_from_google(origins: List[str]) -> dict:
    """
    # Get a distance matrix from Google Maps API
    """
    load_dotenv()
    api_key = os.environ.get("API_KEY_GOOGLE")
    gmaps = googlemaps.Client(key=api_key)
    dm_response = gmaps.distance_matrix(origins, origins)
    return dm_response


async def convert_distancematrix_to_tuple(
    dm_response: dict, measurement: str
) -> Tuple[Tuple[int]]:
    """
    # Convert a distance matrix dictionary to a 2D tuple
    - "measurement" is either "distance" or "duration"
    """
    len_1d: int = len(dm_response["rows"])
    len_2d: int = len(dm_response["rows"][0]["elements"])
    output: [] = [None] * len_1d
    for i in range(len_1d):
        inner_list: [] = [None] * len_2d
        for j in range(len_2d):
            inner_list[j] = dm_response["rows"][i]["elements"][j][measurement]["value"]
        output[i] = tuple(inner_list)
    return tuple(output)


async def parse_distancematrix_response(dm_response: dict) -> dict:
    """
    # Parse a distance matrix response from Google to a dictionary of two 2D tuples
    """
    return {
        "distance": await convert_distancematrix_to_tuple(dm_response, "distance"),
        "duration": await convert_distancematrix_to_tuple(dm_response, "duration"),
    }
