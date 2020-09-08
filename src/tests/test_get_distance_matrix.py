#!/usr/bin/env python

"""
Test get_distance_matrix
"""

import os
import asyncio
from unittest import TestCase
from unittest.mock import patch
from tempfile import TemporaryDirectory
import json
import pickle
from core.get_distance_matrix import process_distancematrix_response
from tests.load_answer_key import (
    load_distance_matrix_response,
    load_parsed_distance_matrix_tuple,
    load_parsed_distance_matrix_list,
)


class TestGetDistanceMatrix(TestCase):
    @patch("core.distancematrix.google_distance_matrix.googlemaps")
    def test_process_distancematrix_response(self, mock_googlemaps):
        dm_response = load_distance_matrix_response()
        mock_gmaps = mock_googlemaps.Client()
        mock_gmaps.distance_matrix.return_value = dm_response
        temp_dir = TemporaryDirectory()

        output = asyncio.run(process_distancematrix_response([], temp_dir.name))

        with open(os.path.join(temp_dir.name, "distance_matrix.json"), "r") as f_read:
            loaded_json_response = json.load(f_read)

        with open(
            os.path.join(temp_dir.name, "parsed_distance_matrix.pkl"), "rb"
        ) as f_read:
            loaded_pickle = pickle.load(f_read)

        with open(
            os.path.join(temp_dir.name, "parsed_distance_matrix.json"), "r"
        ) as f_read:
            loaded_json_parsed = json.load(f_read)

        temp_dir.cleanup()

        self.assertEqual(loaded_json_response, dm_response)
        self.assertEqual(loaded_pickle, load_parsed_distance_matrix_tuple())
        self.assertEqual(loaded_json_parsed, load_parsed_distance_matrix_list())
        self.assertEqual(output, True)
