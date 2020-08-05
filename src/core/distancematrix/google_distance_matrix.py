#!/usr/bin/env python

"""
Get distance matrices from Google Maps API and process the response
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# pylint: disable=wrong-import-position
from typing import List, Tuple
import googlemaps
from dotenv import load_dotenv
from core.helpers.read_write import (
    load_json_to_dict,
    save_dict_to_json,
    save_data_to_pickle,
)


async def get_dm_from_google_api(origins: List[str]) -> dict:
    """
    Get a distance matrix from Google Maps API
    """
    load_dotenv()
    api_key = os.environ.get("API_KEY_GOOGLE")
    gmaps = googlemaps.Client(key=api_key)
    dm_response = gmaps.distance_matrix(origins, origins)
    return dm_response


async def save_dm_dict_to_json(distance_matrix: dict, to_file: str) -> bool:
    """
    Save a distance matrix response to a JSON file
    """
    return await save_dict_to_json(distance_matrix, to_file)


async def dm_dict_to_2d_tuple(dm_response: dict, measurement: str) -> Tuple[Tuple[int]]:
    """
    Convert a distance matrix dictionary to a 2D tuple
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
    Convert a distance matrix response to a dictionary of two 2D tuples
    """
    return {
        "distance": await dm_dict_to_2d_tuple(dm_response, "distance"),
        "duration": await dm_dict_to_2d_tuple(dm_response, "duration"),
    }


async def load_dm_json_to_dict(file_path: str) -> dict:
    """
    Load a JSON file to a dictionary
    """
    return await load_json_to_dict(file_path)


async def save_dm_tuple_to_pickle(dm_tuple: Tuple[Tuple[int]], to_file: str) -> bool:
    """
    Save a distance matrix tuple to a pickle file
    """
    return await save_data_to_pickle(dm_tuple, to_file)