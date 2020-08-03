#!/usr/bin/env python

"""
Get distance matrices from Google Maps API and process the response
"""

import os
import json
import googlemaps
from dotenv import load_dotenv
from helpers.read_write import save_dict_to_json, save_data_to_pickle


async def get_dm_from_google_api(origins: []) -> dict:
    """
    Get a distance matrix from Google Maps API
    """
    load_dotenv()
    api_key = os.environ.get("API_KEY_GOOGLE")
    gmaps = googlemaps.Client(key=api_key)
    destinations = origins
    dm_response = gmaps.distance_matrix(origins, destinations)
    return dm_response


async def save_dm_dict_to_json(distance_matrix: dict, to_file: str) -> None:
    """
    Save a distance matrix response to a JSON file
    """
    await save_dict_to_json(distance_matrix, to_file)
    return


async def dm_dict_to_2d_tuple(dm_response: dict, measurement: str) -> ((int)):
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


async def load_dm_json_to_dict(json_file: str) -> dict:
    """
    Load distance matrix from a pickle file
    """
    with open(json_file, "r") as read_file:
        return json.load(read_file)


async def save_dm_tuple_to_txt(dm_tuple: ((int)), to_file: str) -> None:
    """
    Save a distance matrix tuple to a text file
    """
    with open(to_file, "w") as file:
        file.write("%s\n" % str(dm_tuple))
    return


async def save_dm_tuple_to_pickle(dm_tuple: ((int)), to_file: str) -> None:
    """
    Save a distance matrix tuple to a pickle file
    """
    await save_data_to_pickle(dm_tuple, to_file)
    return
