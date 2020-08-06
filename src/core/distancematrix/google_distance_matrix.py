#!/usr/bin/env python

"""
# Get distance matrices from Google Maps API and process the response
"""

import sys
import os
from typing import List, Tuple
import googlemaps
from dotenv import load_dotenv


async def get_dm_from_google_api(origins: List[str]) -> dict:
    """
    # Get a distance matrix from Google Maps API
    """
    load_dotenv()
    api_key = os.environ.get("API_KEY_GOOGLE")
    gmaps = googlemaps.Client(key=api_key)
    dm_response = gmaps.distance_matrix(origins, origins)
    return dm_response


async def dm_dict_to_2d_tuple(dm_response: dict, measurement: str) -> Tuple[Tuple[int]]:
    """
    # Convert a distance matrix dictionary to a 2D tuple
    - "measurement" is either "distance" or "duration"
    """
    len_1d: int = len(dm_response["rows"])
    len_2d: int = len(dm_response["rows"][0]["elements"])
    output: [] = [None] * len_1d
    for i in range(0, len_1d):
        inner_list: [] = [None] * len_2d
        for j in range(0, len_2d):
            inner_list[j] = dm_response["rows"][i]["elements"][j][measurement]["value"]
        output[i] = tuple(inner_list)
    return tuple(output)


async def parse_dm_response(dm_response: dict) -> dict:
    """
    # Convert a distance matrix response to a dictionary of two 2D tuples
    """
    return {
        "distance": await dm_dict_to_2d_tuple(dm_response, "distance"),
        "duration": await dm_dict_to_2d_tuple(dm_response, "duration"),
    }
