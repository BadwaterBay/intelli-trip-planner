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
    save_to_pickle,
)
from tests.load_answer_key import load_parsed_distance_matrix_tuple


class TestHelpersReadWrite(unittest.TestCase):
    def test_load_pickle_1(self):
        current_dir: str = os.path.dirname(os.path.abspath(__file__))

        temp_file_path: str = os.path.join(
            current_dir, "test_data", "nonexistence_file.pkl"
        )
        output = asyncio.run(load_pickle(temp_file_path))

        answer_key = None

        self.assertEqual(output, answer_key)

    def test_load_pickle_2(self):
        current_dir: str = os.path.dirname(os.path.abspath(__file__))

        temp_file_path: str = os.path.join(
            current_dir, "test_data", "parsed_distance_matrix.pkl"
        )
        output = asyncio.run(load_pickle(temp_file_path))

        answer_key = load_parsed_distance_matrix_tuple()

        self.assertEqual(output, answer_key)

    def test_load_json_to_dict_1(self):
        current_dir: str = os.path.dirname(os.path.abspath(__file__))

        temp_file_path: str = os.path.join(
            current_dir, "test_data", "nonexistence_file.json"
        )
        output = asyncio.run(load_json_to_dict(temp_file_path))

        answer_key = None

        self.assertEqual(output, answer_key)

    def test_load_json_to_dict_2(self):
        test_case = {"a": 1, "b": 2, "c": 3}

        temp_file_path = NamedTemporaryFile()
        with open(temp_file_path.name, "w") as f_write:
            json.dump(test_case, f_write, indent=2)
        output = asyncio.run(load_json_to_dict(temp_file_path.name))

        self.assertEqual(output, test_case)

    def test_save_dict_to_json_1(self):
        test_case = {"a": 1, "b": 2, "c": 3}

        temp_file_path = NamedTemporaryFile()
        output = asyncio.run(save_dict_to_json(test_case, temp_file_path.name))
        with open(temp_file_path.name, "r") as f_read:
            contents = json.load(f_read)

        answer_key = True

        self.assertEqual(contents, test_case)
        self.assertEqual(output, answer_key)

    def test_save_dict_to_json_2(self):
        test_case = int

        temp_file_path = NamedTemporaryFile()
        output = asyncio.run(save_dict_to_json(test_case, temp_file_path.name))

        answer_key = False

        self.assertEqual(output, answer_key)

    def test_save_to_pickle(self):
        test_case = {"a": 1, "b": 2, "c": 3}

        temp_file_path = NamedTemporaryFile()
        asyncio.run(save_to_pickle(test_case, temp_file_path.name))
        with open(temp_file_path.name, "rb") as f_read:
            output = pickle.load(f_read)

        self.assertEqual(output, test_case)


if __name__ == "__main__":
    unittest.main()
