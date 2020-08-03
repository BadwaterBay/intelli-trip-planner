#!/usr/bin/env python

"""
Main script for unit testing
"""

# pylint: disable=wrong-import-position

import os
import unittest
import asyncio
import pickle
from core.traveling_salesman import create_data_model, solve_for_plan
from core.distancematrix.google_distance_matrix import get_dm_from_google_api


class TestTravelingSalesman(unittest.TestCase):
    """
    Test traveling_salesman.py
    """

    def test_create_data_model(self):
        """
        Test create_data_model
        """
        # Input argument values
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        file_path: str = os.path.join(
            current_dir, "mock_data", "parsed_distance_matrix_distance.pkl"
        )
        with open(file_path, "rb") as file:
            distance_matrix = pickle.load(file)

        # Get output
        output = create_data_model(distance_matrix)

        # Get answerkey
        answerkey = {
            "distance_matrix": [
                [
                    0,
                    452812,
                    192690,
                    144369,
                    311478,
                    604974,
                    275096,
                    436980,
                    443998,
                    447211,
                ],
                [
                    451120,
                    0,
                    437724,
                    366440,
                    229587,
                    338302,
                    715338,
                    877222,
                    884240,
                    816997,
                ],
                [
                    191247,
                    435684,
                    0,
                    238990,
                    405904,
                    515548,
                    469067,
                    630950,
                    637969,
                    632564,
                ],
                [
                    141782,
                    365989,
                    238765,
                    0,
                    167110,
                    518151,
                    406001,
                    567884,
                    574902,
                    496696,
                ],
                [
                    309744,
                    227774,
                    406532,
                    167962,
                    0,
                    494157,
                    573962,
                    735846,
                    742864,
                    612885,
                ],
                [
                    603285,
                    336174,
                    517201,
                    518604,
                    494781,
                    0,
                    867503,
                    1029387,
                    1036405,
                    969162,
                ],
                [
                    268459,
                    714826,
                    468458,
                    406383,
                    573492,
                    866987,
                    0,
                    136765,
                    196587,
                    541398,
                ],
                [
                    430493,
                    876859,
                    630491,
                    568416,
                    735526,
                    1029021,
                    137043,
                    0,
                    254873,
                    599684,
                ],
                [
                    437353,
                    883719,
                    637351,
                    575276,
                    742386,
                    1035881,
                    196616,
                    254531,
                    0,
                    477064,
                ],
                [
                    445127,
                    816114,
                    632336,
                    496453,
                    598039,
                    968276,
                    536307,
                    594223,
                    477601,
                    0,
                ],
            ],
            "num_vehicles": 1,
            "depot": 0,
        }

        # Assert
        self.assertEqual(output, answerkey)

    def test_solve_for_plan(self):
        """
        Test solving for simple traveling salesman problem
        """

        # Input argument values
        current_dir: str = os.path.dirname(os.path.abspath(__file__))
        file_path: str = os.path.join(
            current_dir, "mock_data", "parsed_distance_matrix_distance.pkl"
        )

        # Get output
        output = solve_for_plan(file_path)

        # Get answerkey
        answerkey = {
            "waypoints": [0, 2, 5, 1, 4, 3, 9, 8, 7, 6, 0],
            "objective_value": 3076291,
            "true_value": 3076291,
        }

        # Assert
        self.assertEqual(output, answerkey)


class TestGoogleDistanceMatrix(unittest.TestCase):
    """
    Test google_distance_matrix.py
    """

    def test_get_dm_from_google_api(self):
        """
        Test get_dm_from_google_api
        """
        origins = [
            "Denver, CO",
            "Austin, TX",
        ]

        loop = asyncio.get_event_loop()
        distance_matrix = loop.run_until_complete(get_dm_from_google_api(origins))
        loop.close()
        self.assertEqual(distance_matrix["status"], "OK")


if __name__ == "__main__":
    unittest.main()
