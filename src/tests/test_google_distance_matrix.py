#!/usr/bin/env python

"""
Test google_distance_matrix.py
"""

import os
import asyncio
import unittest
from tempfile import mkstemp
from unittest.mock import patch
import json
import pickle
from core.distancematrix.google_distance_matrix import (
    get_dm_from_google_api,
    save_dm_dict_to_json,
    dm_dict_to_2d_tuple,
    parse_dm_response,
    load_dm_json_to_dict,
    save_dm_tuple_to_pickle,
)
from tests.load_answer_key import (
    load_parsed_distance_matrix_tuple,
    load_parsed_distance_matrix_list,
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
        origins = [
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
        # Output
        distance_matrix_output = asyncio.run(get_dm_from_google_api(origins))
        # Answer key
        answer_key = "OK"
        # Assert
        self.assertEqual(distance_matrix_output["status"], answer_key)

    def test_save_dm_dict_to_json(self):
        """
        # Test save_dm_dict_to_json
        """
        # Input
        data = load_parsed_distance_matrix_list()
        # Output
        file_path = mkstemp()[1]
        output = asyncio.run(save_dm_dict_to_json(data, file_path))
        with open(file_path, "r") as f_read:
            contents = json.load(f_read)
        # Clean up
        os.remove(file_path)
        # Answer key
        answer_key = True
        # Assert
        self.assertEqual(contents, data)
        self.assertEqual(output, answer_key)

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

    def test_load_dm_json_to_dict(self):
        """
        # Test load_dm_json_to_dict
        """
        # Input:
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        file_path: str = os.path.join(
            current_dir, "mock_data", "parsed_distance_matrix.json"
        )
        # Output:
        output = asyncio.run(load_dm_json_to_dict(file_path))
        # Answer key:
        answer_key = load_parsed_distance_matrix_list()
        # Asssert
        self.assertEqual(output, answer_key)

    def test_save_dm_tuple_to_pickle(self):
        """
        # Test save_dm_tuple_to_pickle
        """
        # Input & answer key
        data = load_parsed_distance_matrix_tuple
        # Output
        file_path = mkstemp()[1]
        asyncio.run(save_dm_tuple_to_pickle(data, file_path))
        with open(file_path, "rb") as f_read:
            output = pickle.load(f_read)
        # Clean up
        os.remove(file_path)
        # Assert
        self.assertEqual(output, data)


if __name__ == "__main__":
    unittest.main()
