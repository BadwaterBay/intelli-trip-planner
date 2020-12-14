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
from core.helpers.read_write import (
    load_json_to_dict,
    save_dict_to_json,
)


class TestHelpersReadWrite(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
