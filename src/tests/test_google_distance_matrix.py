#!/usr/bin/env python

"""
Test google_distance_matrix.py
"""

import os
import asyncio
import unittest
from unittest.mock import patch
import json
from core.distancematrix.google_distance_matrix import (
    get_dm_from_google_api,
    dm_dict_to_2d_tuple,
    parse_dm_response,
)
from tests.load_answer_key import (
    load_distance_matrix_origins_list,
    load_parsed_distance_matrix_tuple,
)


class TestGoogleDistanceMatrix(unittest.TestCase):
    """
    # Test google_distance_matrix.py
    """

    @patch("core.distancematrix.google_distance_matrix.googlemaps")
    def test_get_dm_from_google_api(self, mock_googlemaps):
        """
        # Test get_dm_from_google_api
        - :param mock_googlemaps: Mock of googlemaps module
        - API key is omitted in the test
        """
        # Input & mock setup
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        file_path: str = os.path.join(current_dir, "mock_data", "distance_matrix.json")
        with open(file_path, "r") as f_read:
            distance_matrix_response = json.load(f_read)
        mock_gmaps = mock_googlemaps.Client()
        mock_gmaps.distance_matrix.return_value = distance_matrix_response
        origins = load_distance_matrix_origins_list()
        # Output
        distance_matrix_output = asyncio.run(get_dm_from_google_api(origins))
        # Answer key
        answer_key = "OK"
        # Assert
        self.assertEqual(distance_matrix_output["status"], answer_key)

    def test_dm_dict_to_2d_tuple_distance(self):
        """
        # Test dm_dict_to_2d_tuple with "distance" argument
        """
        # Input:
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        file_path: str = os.path.join(current_dir, "mock_data", "distance_matrix.json")
        with open(file_path, "r") as read_file:
            distance_matrix: dict = json.load(read_file)
        # Answer key:
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()
        answer_key = parsed_distance_matrix["distance"]
        # Output:
        output = asyncio.run(dm_dict_to_2d_tuple(distance_matrix, "distance"))
        # Asssert
        self.assertEqual(output, answer_key)

    def test_dm_dict_to_2d_tuple_duration(self):
        """
        # Test dm_dict_to_2d_tuple with "duration" argument
        """
        # Input:
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        file_path: str = os.path.join(current_dir, "mock_data", "distance_matrix.json")
        with open(file_path, "r") as read_file:
            distance_matrix = json.load(read_file)
        # Answer key:
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()
        answer_key = parsed_distance_matrix["duration"]
        # Output:
        output = asyncio.run(dm_dict_to_2d_tuple(distance_matrix, "duration"))
        # Assert:
        self.assertEqual(output, answer_key)

    def test_parse_dm_response(self):
        """
        # Test parse_dm_response
        """
        # Input:
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        file_path: str = os.path.join(current_dir, "mock_data", "distance_matrix.json")
        with open(file_path, "r") as read_file:
            distance_matrix = json.load(read_file)
        # Answer key:
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()
        answer_key = parsed_distance_matrix
        # Output:
        output = asyncio.run(parse_dm_response(distance_matrix))
        # Assert:
        self.assertEqual(output, answer_key)


if __name__ == "__main__":
    unittest.main()
