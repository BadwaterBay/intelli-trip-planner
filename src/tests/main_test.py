#!/usr/bin/env python

"""
Main script for unit testing
"""

import os
import unittest
from unittest.mock import patch
from io import StringIO
import asyncio
import pickle
import json
from core.traveling_salesman import create_data_model, print_plan, solve_for_plan
from core.distancematrix.google_distance_matrix import (
    # get_dm_from_google_api,
    dm_dict_to_2d_tuple,
    parse_dm_response,
)
from core.helpers.read_write import load_dm_pickle


class TestHelpersReadWrite(unittest.TestCase):
    """
    Test helper functions: read_write.py
    """

    def test_load_dm_pickle(self):
        """
        Test load_dm_pickle
        """
        # Input:
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        pickle_file: str = os.path.join(
            current_dir, "mock_data", "parsed_distance_matrix.pkl"
        )
        # Output:
        output = asyncio.run(load_dm_pickle(pickle_file))
        # Answer key:
        with open(pickle_file, "rb") as file:
            answer_key = pickle.load(file)
        # Assert:
        self.assertEqual(output, answer_key)


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
        parsed_file: str = os.path.join(
            current_dir, "mock_data", "parsed_distance_matrix.pkl"
        )

        # Answer key:
        with open(parsed_file, "rb") as file:
            answer_key = pickle.load(file)["distance"]

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
        parsed_file: str = os.path.join(
            current_dir, "mock_data", "parsed_distance_matrix.pkl"
        )
        # Answer key:
        with open(parsed_file, "rb") as file:
            answer_key = pickle.load(file)["duration"]
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
        parsed_file: str = os.path.join(
            current_dir, "mock_data", "parsed_distance_matrix.pkl"
        )
        # Answer key:
        with open(parsed_file, "rb") as file:
            answer_key = pickle.load(file)
        # Output:
        output = asyncio.run(parse_dm_response(distance_matrix))
        # Assert:
        self.assertEqual(output, answer_key)


class TestTravelingSalesman(unittest.TestCase):
    """
    Test traveling_salesman.py
    """

    def test_create_data_model(self):
        """
        Test create_data_model
        """
        # Input:
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        file_path: str = os.path.join(
            current_dir, "mock_data", "parsed_distance_matrix.pkl"
        )
        with open(file_path, "rb") as file:
            distance_matrix = pickle.load(file)
        # Output:
        output = asyncio.run(create_data_model(distance_matrix["distance"]))
        # Answer key:
        answer_key = {
            "distance_matrix": (
                (
                    0,
                    452812,
                    192690,
                    144369,
                    311544,
                    604974,
                    269142,
                    431026,
                    438044,
                    447211,
                ),
                (
                    451120,
                    0,
                    437724,
                    366440,
                    229653,
                    338302,
                    715338,
                    877222,
                    884240,
                    816997,
                ),
                (
                    191247,
                    435684,
                    0,
                    238990,
                    405970,
                    515548,
                    469067,
                    630950,
                    637969,
                    632563,
                ),
                (
                    141782,
                    365989,
                    238765,
                    0,
                    167175,
                    518151,
                    406001,
                    567884,
                    574902,
                    496696,
                ),
                (
                    309863,
                    227823,
                    406651,
                    168080,
                    0,
                    494206,
                    574081,
                    735965,
                    742983,
                    613004,
                ),
                (
                    603285,
                    336174,
                    517201,
                    518604,
                    494847,
                    0,
                    867503,
                    1029387,
                    1036405,
                    969162,
                ),
                (
                    268459,
                    714826,
                    468458,
                    406383,
                    573558,
                    866987,
                    0,
                    136765,
                    196587,
                    541398,
                ),
                (
                    430493,
                    876860,
                    630491,
                    568416,
                    735592,
                    1029021,
                    137043,
                    0,
                    254873,
                    599684,
                ),
                (
                    437353,
                    883719,
                    637351,
                    575276,
                    742451,
                    1035881,
                    196616,
                    254531,
                    0,
                    477064,
                ),
                (
                    445127,
                    816114,
                    632335,
                    496453,
                    598105,
                    968276,
                    536307,
                    594223,
                    477601,
                    0,
                ),
            ),
            "num_vehicles": 1,
            "depot": 0,
        }
        # Assert:
        self.assertEqual(output, answer_key)

    def test_solve_for_plan(self):
        """
        Test solving for simple traveling salesman problem
        """
        # Input:
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        file_path: str = os.path.join(
            current_dir, "mock_data", "parsed_distance_matrix.pkl"
        )
        with open(file_path, "rb") as file:
            distance_matrix = pickle.load(file)
        # Output:
        async def get_output():
            """
            Output
            """
            data = await create_data_model(distance_matrix["distance"])
            return await solve_for_plan(data)

        output = asyncio.run(get_output())
        # Answer key:
        answer_key = {
            "waypoints": [0, 6, 7, 8, 9, 3, 4, 1, 5, 2, 0],
            "objective_value": 3076045,
            "true_value": 3076045,
        }
        # Assert:
        self.assertEqual(output, answer_key)

    def test_print_plan(self):
        """
        Test printing the solution in stdout
        """
        # Input:
        plan = {
            "waypoints": [0, 6, 7, 8, 9, 3, 4, 1, 5, 2, 0],
            "objective_value": 3076045,
            "true_value": 3076045,
        }
        # Answer key:
        answer_key = (
            "Objective: 3076045 meters\n"
            "True: 3076045 meters\n"
            "0 -> 6 -> 7 -> 8 -> 9 -> 3 -> 4 -> 1 -> 5 -> 2 -> 0\n"
        )
        # Assert:
        with patch("sys.stdout", new=StringIO()) as fake_out:
            asyncio.run(print_plan(plan))
            self.assertEqual(fake_out.getvalue(), answer_key)


if __name__ == "__main__":
    unittest.main()
