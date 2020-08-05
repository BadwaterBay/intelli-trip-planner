#!/usr/bin/env python

"""
Helper functions for reading and writing files
"""

import sys
import json
import pickle
from typing import Union


async def load_dm_pickle(file_path: str) -> Union[dict, None]:
    """
    # Load distance matrix from pickle to dictionary
    - :param file_path: Path to pickle file.
    - :type file_path: str
    - :return: A dictionary.
    - :rtype: dict
    """
    try:
        with open(file_path, "rb") as f_read:
            return pickle.load(f_read)
    except ValueError:
        print("Invalid pickle file in " + file_path, file=sys.stderr)
        return None


async def load_json_to_dict(file_path: str) -> Union[dict, None]:
    """
    # Load a JSON file to a dictionary
    - :param file_path: Path to JSON file
    - :type file_path: str
    - :return: A dictionary
    - :rtype: dict
    """
    try:
        with open(file_path, "r") as f_read:
            return json.load(f_read)
    except ValueError:
        print("Invalid JSON file in " + file_path, file=sys.stderr)
        return None


async def save_dict_to_json(dict_data: dict, to_file: str) -> bool:
    """
    # Save a dictionary to a json file
    - :param dict_data: Dictionary to be written to a JSON file
    - :param to_file: Path to file to be written
    - :type file_path: dict
    - :type to_file: str
    - :return: True if succeeds. False if fails.
    - :rtype: bool
    """
    try:
        with open(to_file, "w") as f_write:
            json.dump(dict_data, f_write, indent=2)
            return True
    except TypeError as err:
        print("Unable to serialize the object.\n" + err, file=sys.stderr)
        return False


async def save_data_to_pickle(data, to_file: str) -> bool:
    """
    # Save data to pickle file
    - :param dict_data: Dictionary to be written to a pickle file
    - :param to_file: Path to file to be written
    - :type file_path: dict
    - :type to_file: str
    - :return: True if succeeds. False if fails.
    - :rtype: bool
    """
    try:
        with open(to_file, "wb") as f_write:
            pickle.dump(data, f_write)
            return True
    except TypeError as err:
        print("Unable to serialize the object.\n" + err, file=sys.stderr)
        return False
