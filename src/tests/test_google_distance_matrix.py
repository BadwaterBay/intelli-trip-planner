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
    get_distancematrix_from_google,
    convert_distancematrix_to_tuple,
    parse_distancematrix_response,
)
from tests.load_answer_key import (
    load_distance_matrix_response,
    load_distance_matrix_origins_list,
    load_parsed_distance_matrix_tuple,
)


class TestGoogleDistanceMatrix(unittest.TestCase):
    @patch("core.distancematrix.google_distance_matrix.googlemaps")
    def test_get_distancematrix_from_google(self, mock_googlemaps):
        mock_gmaps = mock_googlemaps.Client()
        mock_gmaps.distance_matrix.return_value = load_distance_matrix_response()
        origins = load_distance_matrix_origins_list()

        distance_matrix_output = asyncio.run(get_distancematrix_from_google(origins))

        answer_key = "OK"

        self.assertEqual(distance_matrix_output["status"], answer_key)

    def test_convert_distancematrix_to_tuple_distance(self):
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        file_path_to_distancematrix: str = os.path.join(
            current_dir, "test_data", "distance_matrix.json"
        )
        with open(file_path_to_distancematrix, "r") as read_file:
            distance_matrix: dict = json.load(read_file)

        parsed_distance_matrix = load_parsed_distance_matrix_tuple()
        answer_key = parsed_distance_matrix["distance"]

        output = asyncio.run(
            convert_distancematrix_to_tuple(distance_matrix, "distance")
        )

        self.assertEqual(output, answer_key)

    def test_convert_distancematrix_to_tuple_duration(self):
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        file_path_to_distancematrix: str = os.path.join(
            current_dir, "test_data", "distance_matrix.json"
        )
        with open(file_path_to_distancematrix, "r") as read_file:
            distance_matrix = json.load(read_file)

        parsed_distance_matrix = load_parsed_distance_matrix_tuple()
        answer_key = parsed_distance_matrix["duration"]

        output = asyncio.run(
            convert_distancematrix_to_tuple(distance_matrix, "duration")
        )

        self.assertEqual(output, answer_key)

    def test_parse_distancematrix_response(self):
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        file_path_to_distancematrix: str = os.path.join(
            current_dir, "test_data", "distance_matrix.json"
        )
        with open(file_path_to_distancematrix, "r") as read_file:
            distance_matrix = json.load(read_file)

        answer_key = load_parsed_distance_matrix_tuple()

        output = asyncio.run(parse_distancematrix_response(distance_matrix))

        self.assertEqual(output, answer_key)


if __name__ == "__main__":
    unittest.main()
