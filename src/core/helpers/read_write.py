#!/usr/bin/env python

"""
Helper functions for reading and writing files
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# pylint: disable=wrong-import-position
import json
import pickle


async def load_dm_pickle(file_path: str) -> dict:
    """
    Load distance matrix from pickle to dictionary
    """
    with open(file_path, "rb") as file:
        return pickle.load(file)


async def load_json_to_dict(json_file: str) -> dict:
    """
    Load a JSON file to a dictionary
    """
    with open(json_file, "r") as read_file:
        return json.load(read_file)


async def save_dict_to_json(dict_data: dict, to_file: str) -> None:
    """
    Save a dictionary to a json file
    """
    with open(to_file, "w") as file:
        json.dump(dict_data, file, indent=2)
    return


async def save_data_to_pickle(data, to_file: str) -> None:
    """
    Save data to pickle file
    """
    with open(to_file, "wb") as file:
        pickle.dump(data, file)
    return
