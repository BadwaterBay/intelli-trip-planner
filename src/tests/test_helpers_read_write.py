#!/usr/bin/env python

"""
# Test helper function read_write.py
"""

# pylint: disable=duplicate-code

import os
import asyncio
import unittest
from tempfile import NamedTemporaryFile
import json
import pickle
from core.helpers.read_write import (
    load_pickle,
    load_json_to_dict,
    save_dict_to_json,
    save_data_to_pickle,
)
from tests.load_answer_key import load_parsed_distance_matrix_tuple


class TestHelpersReadWrite(unittest.TestCase):
    """
    # Test helper functions: read_write.py
    """

    def test_load_pickle_1(self):
        """
        # Test load_dm_pickle with nonexistence file
        """
        # Input:
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        file_path: str = os.path.join(current_dir, "test_data", "nonexistence_file.pkl")
        # Output:
        output = asyncio.run(load_pickle(file_path))
        # Answer key:
        answer_key = None
        # Assert:
        self.assertEqual(output, answer_key)

    def test_load_pickle_2(self):
        """
        # Test load_dm_pickle with a valid file
        """
        # Input:
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        file_path: str = os.path.join(
            current_dir, "test_data", "parsed_distance_matrix.pkl"
        )
        # Output:
        output = asyncio.run(load_pickle(file_path))
        # Answer key:
        answer_key = load_parsed_distance_matrix_tuple()
        # Assert:
        self.assertEqual(output, answer_key)

    def test_load_json_to_dict_1(self):
        """
        # Test load_json_to_dict with nonexistence file
        """
        # Input:
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        file_path: str = os.path.join(
            current_dir, "test_data", "nonexistence_file.json"
        )
        # Output:
        output = asyncio.run(load_json_to_dict(file_path))
        # Answer key:
        answer_key = None
        # Assert:
        self.assertEqual(output, answer_key)

    def test_load_json_to_dict_2(self):
        """
        # Test load_json_to_dict with a valid file
        """
        # Input & answer key:
        data = {"a": 1, "b": 2, "c": 3}
        # Setup:
        file_path = NamedTemporaryFile()
        with open(file_path.name, "w") as f_write:
            json.dump(data, f_write, indent=2)
        # Output:
        output = asyncio.run(load_json_to_dict(file_path.name))
        # Assert:
        self.assertEqual(output, data)

    def test_save_dict_to_json_1(self):
        """
        # Test save_dict_to_json
        """
        # Input
        data = {"a": 1, "b": 2, "c": 3}
        # Output
        file_path = NamedTemporaryFile()
        output = asyncio.run(save_dict_to_json(data, file_path.name))
        with open(file_path.name, "r") as f_read:
            contents = json.load(f_read)
        # Answer key
        answer_key = True
        # Assert
        self.assertEqual(contents, data)
        self.assertEqual(output, answer_key)

    def test_save_dict_to_json_2(self):
        """
        # Test save_dict_to_json on unserialized objects
        """
        # Input & answer key
        data = int
        # Output
        file_path = NamedTemporaryFile()
        output = asyncio.run(save_dict_to_json(data, file_path.name))
        # Answer key
        answer_key = False
        # Assert
        self.assertEqual(output, answer_key)

    def test_save_data_to_pickle(self):
        """
        # Test save_data_to_pickle
        """
        # Input & answer key
        data = {"a": 1, "b": 2, "c": 3}
        # Output
        file_path = NamedTemporaryFile()
        asyncio.run(save_data_to_pickle(data, file_path.name))
        with open(file_path.name, "rb") as f_read:
            output = pickle.load(f_read)
        # Assert
        self.assertEqual(output, data)


if __name__ == "__main__":
    unittest.main()
