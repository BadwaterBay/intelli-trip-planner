#!/usr/bin/env python

"""
Get distance matrix from Google Maps API and process the response
"""

import os
import json
import pickle
import googlemaps
from dotenv import load_dotenv

def get_distance_matrix(origins: []) -> dict:
    """
    Get distance matrix from Google Maps API
    """

    load_dotenv()
    api_key = os.environ.get("api_key_GOOGLE")

    gmaps = googlemaps.Client(key=api_key)

    destinations = origins

    # Get distance matrix
    distance_matrix = gmaps.distance_matrix(origins, destinations)

    return distance_matrix


def save_distance_matrix_to_json(distance_matrix: dict, to_file: str) -> None:
    """
    Save distance matrix to json file
    """

    with open(to_file, "w") as file:
        json.dump(distance_matrix, file, indent=2)


def convert_json_to_list(json_file: str, measurement: str) -> [[int]]:
    """
    Convert distance matrix JSON to 2D list for OR-Tools

    "measurement" can be either "distance" or "duration"
    """

    with open(json_file, "r") as read_file:
        data = json.load(read_file)

    len_1d: int = len(data["rows"])
    len_2d: int = len(data["rows"][0]["elements"])

    distance_matrix_list: [] = [None] * len_1d

    for i in range(0, len_1d):
        inner_list: [] = [None] * len_2d

        for j in range(0, len_2d):
            inner_list[j] = data["rows"][i]["elements"][j][measurement]["value"]

        distance_matrix_list[i] = inner_list

    return distance_matrix_list


def save_distance_matrix_list_to_txt(distance_list: [[int]], to_file: str) -> None:
    """
    Save distance list to txt file
    """

    with open(to_file, "w") as file:
        file.write("%s\n" % distance_list)


def save_to_pickle(data, to_file: str) -> None:
    """
    Save distance list to pickle file
    """

    with open(to_file, "wb") as file:
        pickle.dump(data, file)
