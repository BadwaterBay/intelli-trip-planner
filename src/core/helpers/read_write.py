#!/usr/bin/env python

"""
# Helper functions for reading and writing files
"""

import sys
import json
import pickle
from typing import Union


async def load_pickle(file_path: str) -> Union[dict, None]:
    try:
        with open(file_path, "rb") as f_read:
            return pickle.load(f_read)
    except FileNotFoundError:
        print("Invalid pickle file in " + file_path, file=sys.stderr)
        return None


async def load_json_to_dict(file_path: str) -> Union[dict, None]:
    try:
        with open(file_path, "r") as f_read:
            return json.load(f_read)
    except FileNotFoundError:
        print("Invalid JSON file in " + file_path, file=sys.stderr)
        return None


async def save_to_pickle(data, file_path: str) -> bool:
    with open(file_path, "wb") as f_write:
        pickle.dump(data, f_write)
    return True


async def save_dict_to_json(dict_data: dict, file_path: str) -> bool:
    try:
        with open(file_path, "w") as f_write:
            json.dump(dict_data, f_write, indent=2)
        return True
    except TypeError:
        print("Unable to serialize the object.", file=sys.stderr)
        return False
