#!/usr/bin/env python

"""
Create distance matrices for development
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# pylint: disable=wrong-import-position
import asyncio
from core.distancematrix.google_distance_matrix import (
    get_dm_from_google_api,
    save_dm_dict_to_json,
    parse_dm_response,
    save_dm_tuple_to_pickle,
)
from core.helpers.read_write import save_dict_to_json


async def dm_pipeline(origins: []) -> None:
    """
    Pipeline for getting and manipulating distance matrices
    """

    # Set the directory where distance matrix data will be saved
    current_dir: str = os.path.dirname(os.path.abspath(__file__))
    dir_for_data: str = os.path.join(current_dir, "data")

    # Get distance matrix from Google Maps API
    dm_response: dict = await get_dm_from_google_api(origins)

    # Save distance matrix response from Google Maps API to JSON
    dm_json: str = os.path.join(dir_for_data, "distance_matrix.json")
    await save_dm_dict_to_json(dm_response, dm_json)

    # Parse distance matrix to a dictionary of two 2D tuples
    parsed_dm: dict = await parse_dm_response(dm_response)

    # Save parsed distance matrix to a pickle file
    pickle_file: str = os.path.join(dir_for_data, "parsed_distance_matrix.pkl")
    await save_dm_tuple_to_pickle(parsed_dm, pickle_file)

    # Save parsed distance matrix to a JSON file
    json_file: str = os.path.join(dir_for_data, "parsed_distance_matrix.json")
    await save_dict_to_json(parsed_dm, json_file)

    return


async def main():
    """
    Main function for creating distance matrices for development
    """
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

    await dm_pipeline(origins)


if __name__ == "__main__":
    asyncio.run(main())
