#!/usr/bin/env python

"""
Create distance matrices for development
"""


def main():
    import os

    CUR_DIR = os.path.dirname(os.path.abspath(__file__))
    LIB_DIR = os.path.join(CUR_DIR, "../lib")

    import sys

    sys.path.insert(1, LIB_DIR)

    import get_distance_matrix as dm

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

    # Get distance matrix from Google Maps API
    # distance_matrix = dm.get_distance_matrix(origins)

    # Save distance matrix response from Google Maps API to JSON
    dm_json: str = "./src/data/distance_matrix.json"
    # dm.save_distance_matrix_to_json(distance_matrix, dm_json)

    # Convert JSON to 2D list
    distance_matrix_list = dm.convert_json_to_list(dm_json, "distance")
    duration_matrix_list = dm.convert_json_to_list(dm_json, "duration")

    # Save 2D list to txt
    distance_txt: str = "./src/data/distance_matrix_list.txt"
    dm.save_distance_matrix_list_to_txt(distance_matrix_list, distance_txt)

    duration_txt: str = "./src/data/duration_matrix_list.txt"
    dm.save_distance_matrix_list_to_txt(duration_matrix_list, duration_txt)

    # Save 2D list to pickle
    distance_pickle: str = "./src/data/distance_matrix_list.pkl"
    dm.pickle(distance_matrix_list, distance_pickle)
    duration_pickle: str = "./src/data/duration_matrix_list.pkl"
    dm.pickle(duration_matrix_list, duration_pickle)


if __name__ == "__main__":
    main()
