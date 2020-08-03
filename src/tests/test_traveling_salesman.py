#!/usr/bin/env python

"""
Main script for unit testing
"""

import unittest
from unittest.mock import patch
from io import StringIO
import asyncio
from core.traveling_salesman import create_data_model, print_plan, solve_for_plan
from tests.load_answer_key import load_parsed_distance_matrix


class TestTravelingSalesman(unittest.TestCase):
    """
    Test traveling_salesman.py
    """

    def test_create_data_model(self):
        """
        Test create_data_model
        """
        # Input:
        parsed_distance_matrix = load_parsed_distance_matrix()
        distance_matrix = parsed_distance_matrix
        # Output:
        output = asyncio.run(create_data_model(distance_matrix["distance"]))
        # Answer key:
        answer_key = {
            "distance_matrix": parsed_distance_matrix["distance"],
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
        parsed_distance_matrix = load_parsed_distance_matrix()
        distance_matrix = parsed_distance_matrix
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
