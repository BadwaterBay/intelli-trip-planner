#!/usr/bin/env python

"""
Test google_distance_matrix.py
"""

import os
import unittest
import asyncio
import json
from core.distancematrix.google_distance_matrix import (
    # get_dm_from_google_api,
    dm_dict_to_2d_tuple,
    parse_dm_response,
)
from tests.load_answer_key import load_parsed_distance_matrix


class TestGoogleDistanceMatrix(unittest.TestCase):
    """
    Test google_distance_matrix.py
    """

    # def test_get_dm_from_google_api(self):
    #     """
    #     Test get_dm_from_google_api
    #     - It's too costly to call the real Google Maps API for routine testing
    #     """
    #     origins = [
    #         "Denver, CO",
    #         "Austin, TX",
    #     ]
    #     loop = asyncio.get_event_loop()
    #     distance_matrix = loop.run_until_complete(get_dm_from_google_api(origins))
    #     loop.close()
    #     self.assertEqual(distance_matrix["status"], "OK")

    def test_dm_dict_to_2d_tuple_distance(self):
        """
        Test dm_dict_to_2d_tuple with "distance" argument
        """
        # Input:
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        json_file: str = os.path.join(current_dir, "mock_data", "distance_matrix.json")
        with open(json_file, "r") as read_file:
            distance_matrix: dict = json.load(read_file)
        # Answer key:
        parsed_distance_matrix = load_parsed_distance_matrix()
        answer_key = parsed_distance_matrix["distance"]
        # Output:
        output = asyncio.run(dm_dict_to_2d_tuple(distance_matrix, "distance"))
        # Asssert
        self.assertEqual(output, answer_key)

    def test_dm_dict_to_2d_tuple_duration(self):
        """
        Test dm_dict_to_2d_tuple with "duration" argument
        """
        # Input:
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        json_file: str = os.path.join(current_dir, "mock_data", "distance_matrix.json")
        with open(json_file, "r") as read_file:
            distance_matrix = json.load(read_file)
        # Answer key:
        parsed_distance_matrix = load_parsed_distance_matrix()
        answer_key = parsed_distance_matrix["duration"]
        # Output:
        output = asyncio.run(dm_dict_to_2d_tuple(distance_matrix, "duration"))
        # Assert:
        self.assertEqual(output, answer_key)

    def test_parse_dm_response(self):
        """
        Test parse_dm_response
        """
        # Input:
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        json_file: str = os.path.join(current_dir, "mock_data", "distance_matrix.json")
        with open(json_file, "r") as read_file:
            distance_matrix = json.load(read_file)
        # Answer key:
        parsed_distance_matrix = load_parsed_distance_matrix()
        answer_key = parsed_distance_matrix
        # Output:
        output = asyncio.run(parse_dm_response(distance_matrix))
        # Assert:
        self.assertEqual(output, answer_key)


if __name__ == "__main__":
    unittest.main()
