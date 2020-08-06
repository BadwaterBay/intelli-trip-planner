#!/usr/bin/env python

"""
Get distance matrices from Google Maps API for development
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# pylint: disable=wrong-import-position
import asyncio
from typing import List
from core.distancematrix.google_distance_matrix import (
    get_dm_from_google_api,
    parse_dm_response,
)
from core.helpers.read_write import save_dict_to_json, save_data_to_pickle


async def dm_pipeline(origins: List[str], dir_for_data: str) -> bool:
    """
    Pipeline for getting and manipulating distance matrices
    """

    # Get distance matrix from Google Maps API
    dm_response: dict = await get_dm_from_google_api(origins)

    # # Save distance matrix response from Google Maps API to JSON
    dm_json: str = os.path.join(dir_for_data, "distance_matrix.json")
    response_0 = await save_dict_to_json(dm_response, dm_json)

    # # Parse distance matrix to a dictionary of two 2D tuples
    parsed_dm: dict = await parse_dm_response(dm_response)

    # # Save parsed distance matrix to a pickle file
    pickle_file: str = os.path.join(dir_for_data, "parsed_distance_matrix.pkl")
    response_1 = await save_data_to_pickle(parsed_dm, pickle_file)

    # # Save parsed distance matrix to a JSON file
    json_file: str = os.path.join(dir_for_data, "parsed_distance_matrix.json")
    response_2 = await save_dict_to_json(parsed_dm, json_file)

    return response_0 and response_1 and response_2


async def main() -> bool:
    """
    Main function for creating distance matrices for development
    """
    origins: List[str] = [
        "Las Vegas McCarran International Airport, NV",
        "Los Angeles International Airport, CA",
        "Death Valley Furnace Creek Visitor Center, Furnace Creek, CA",
        "Mojave Kelso Depot Visitor Center, CA",
        "Joshua Tree National Park Visitor Center, Park Boulevard, Joshua Tree, CA",
        "Sequoia National Park - Visitor Center, Generals Highway, Three Rivers, CA",
        "Zion National Park Visitor Center, Zion – Mount Carmel Highway, Hurricane, UT",
        "Bryce Canyon National Park Visitor Center, Utah 63, Bryce Canyon City, UT",
        "Grand Canyon North Rim Visitor Center, AZ-67, North Rim, AZ 86023",
        "Grand Canyon Visitor Center, South Entrance Road, Grand Canyon Village, AZ",
    ]

    # Set the directory where distance matrix data will be saved
    current_dir: str = os.path.dirname(os.path.abspath(__file__))
    dir_for_data: str = os.path.join(current_dir, "data")

    return await dm_pipeline(origins, dir_for_data)


if __name__ == "__main__":
    asyncio.run(main())
