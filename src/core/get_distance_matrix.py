#!/usr/bin/env python

"""
# Get distance matrices from Google Maps API for development
"""

import sys
import os
import asyncio
from typing import List

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.distancematrix.google_distance_matrix import (
    get_distancematrix_from_google,
    parse_distancematrix_response,
)
from core.helpers.read_write import save_dict_to_json


async def process_distancematrix_response(
    origins: List[str], dir_for_data: str
) -> bool:
    dm_response: dict = await get_distancematrix_from_google(origins)

    dm_json: str = os.path.join(dir_for_data, "distance_matrix.json")
    raw_response = await save_dict_to_json(dm_response, dm_json)

    parsed_dm: dict = await parse_distancematrix_response(dm_response)

    json_file: str = os.path.join(dir_for_data, "parsed_distance_matrix.json")
    parsed_response = await save_dict_to_json(parsed_dm, json_file)

    return raw_response and parsed_response


async def create_distancematrix_for_dev(origins: List[str]) -> bool:
    current_dir: str = os.path.dirname(os.path.abspath(__file__))
    dir_for_data: str = os.path.join(current_dir, "data")
    return await process_distancematrix_response(origins, dir_for_data)


if __name__ == "__main__":
    origins_for_dev = [
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
    asyncio.run(create_distancematrix_for_dev(origins_for_dev))
