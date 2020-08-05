#!/usr/bin/env python

"""
Test find_route.py
"""

import unittest
from unittest.mock import patch
from io import StringIO
import asyncio
from core.find_route import create_data_model, print_plan, solve_for_plan, main
from tests.load_answer_key import load_parsed_distance_matrix_tuple


class TestFindRoute(unittest.TestCase):
    """
    Test find_route.py
    """

    def test_create_data_model_1(self):
        """
        Test create_data_model
        """
        # Input:
        # No argument
        # Output:
        output = asyncio.run(create_data_model())
        # Answer key:
        answer_key = None
        # Assert:
        self.assertEqual(output, answer_key)

    def test_create_data_model_2(self):
        """
        Test create_data_model
        """
        # Input:
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()
        # Output:
        output = asyncio.run(
            create_data_model(
                parsed_distance_matrix["distance"], parsed_distance_matrix["duration"],
            )
        )
        # Answer key:
        answer_key = {
            "distance_matrix": parsed_distance_matrix["distance"],
            "duration_matrix": parsed_distance_matrix["duration"],
            "num_vehicles": 1,
            "depot": 0,
        }
        # Assert:
        self.assertEqual(output, answer_key)

    def test_solve_for_plan_distance_without_quota_1(self):
        """
        # Test solving for simple traveling salesman problem without quota
        ## Parameters:
        - Use distance for calculation
        - Test solve_for_plan() with missing `quota` argument
        """
        # Input:
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()
        # Output:
        async def get_output():
            """
            Output
            """
            data = await create_data_model(
                parsed_distance_matrix["distance"], parsed_distance_matrix["duration"],
            )
            return await solve_for_plan(data, "distance_matrix")

        output = asyncio.run(get_output())
        # Answer key:
        answer_key = {
            "waypoints": [0, 6, 7, 8, 9, 3, 4, 1, 5, 2, 0],
            "objective_value": 3076045,
            "true_value": 3076045,
            "quota": None,
        }
        # Assert:
        self.assertEqual(output, answer_key)

    def test_solve_for_plan_distance_without_quota_2(self):
        """
        # Test solving for simple traveling salesman problem without quota
        ## Parameters:
        - Use distance for calculation
        - Test solve_for_plan() with `quota` set to 0
        """
        # Input:
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()
        # Output:
        async def get_output():
            """
            Output
            """
            data = await create_data_model(
                parsed_distance_matrix["distance"], parsed_distance_matrix["duration"],
            )
            return await solve_for_plan(data, "distance_matrix", 0)

        output = asyncio.run(get_output())
        # Answer key:
        answer_key = {
            "waypoints": [0, 6, 7, 8, 9, 3, 4, 1, 5, 2, 0],
            "objective_value": 3076045,
            "true_value": 3076045,
            "quota": None,
        }
        # Assert:
        self.assertEqual(output, answer_key)

    def test_solve_for_plan_duration_without_quota_1(self):
        """
        # Test solving for simple traveling salesman problem without quota
        ## Parameters:
        - Use duration for calculation
        - Test solve_for_plan() with missing `quota` argument
        """
        # Input:
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()
        # Output:
        async def get_output():
            """
            Output
            """
            data = await create_data_model(
                parsed_distance_matrix["distance"], parsed_distance_matrix["duration"],
            )
            return await solve_for_plan(data, "duration_matrix")

        output = asyncio.run(get_output())
        # Answer key:
        answer_key = {
            "waypoints": [0, 6, 7, 8, 9, 3, 4, 1, 5, 2, 0],
            "objective_value": 120524,
            "true_value": 120524,
            "quota": None,
        }
        # Assert:
        self.assertEqual(output, answer_key)

    def test_solve_for_plan_duration_without_quota_2(self):
        """
        # Test solving for simple traveling salesman problem without quota
        ## Parameters:
        - Use duration for calculation
        - Test solve_for_plan() with `quota` set to 0
        """
        # Input:
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()
        # Output:
        async def get_output():
            """
            Output
            """
            data = await create_data_model(
                parsed_distance_matrix["distance"], parsed_distance_matrix["duration"],
            )
            return await solve_for_plan(data, "duration_matrix", 0)

        output = asyncio.run(get_output())
        # Answer key:
        answer_key = {
            "waypoints": [0, 6, 7, 8, 9, 3, 4, 1, 5, 2, 0],
            "objective_value": 120524,
            "true_value": 120524,
            "quota": None,
        }
        # Assert:
        self.assertEqual(output, answer_key)

    def test_solve_for_plan_distance_with_quota(self):
        """
        # Test solving for simple traveling salesman problem with quota
        ## Parameters:
        - Use distance for calculation
        - `quota` has a nonzero value
        """
        # Input:
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()
        quota = int(2000000)  # Set quota to be 2 million meters

        # Output:
        async def get_output():
            """
            Output
            """
            data = await create_data_model(
                parsed_distance_matrix["distance"], parsed_distance_matrix["duration"],
            )
            return await solve_for_plan(data, "distance_matrix", quota)

        output = asyncio.run(get_output())
        # Answer key:
        answer_key = {
            "waypoints": [0, 2, 5, 1, 4, 3, 0],
            "objective_value": 14751175,
            "true_value": 1583927,
            "quota": quota,
        }
        # Assert:
        self.assertEqual(output, answer_key)

    def test_solve_for_plan_duration_with_quota(self):
        """
        # Test solving for simple traveling salesman problem with quota
        ## Parameters:
        - Use duration for calculation
        - `quota` has a nonzero value
        """
        # Input:
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()
        quota = int(3600 * 8)  # Set quota to be 8 hours

        # Output:
        async def get_output():
            """
            Output
            """
            data = await create_data_model(
                parsed_distance_matrix["distance"], parsed_distance_matrix["duration"],
            )
            return await solve_for_plan(data, "duration_matrix", quota)

        output = asyncio.run(get_output())
        # Answer key:
        answer_key = {
            "waypoints": [0, 2, 3, 0],
            "objective_value": 857423,
            "true_value": 21602,
            "quota": quota,
        }
        # Assert:
        self.assertEqual(output, answer_key)

    def test_print_plan_with_valid_solution(self):
        """
        Test printing the solution in stdout with a valid solution
        """
        # Input:
        plan = {
            "waypoints": [0, 6, 7, 8, 9, 3, 4, 1, 5, 2, 0],
            "objective_value": 3076045,
            "true_value": 3076045,
            "quota": None,
        }
        # Answer key:
        answer_key = (
            "Objective: 3076045 units\n"
            "True: 3076045 units\n"
            "Quota: None units\n"
            "0 -> 6 -> 7 -> 8 -> 9 -> 3 -> 4 -> 1 -> 5 -> 2 -> 0\n"
        )
        # Assert:
        with patch("sys.stdout", new=StringIO()) as fake_out:
            asyncio.run(print_plan(plan))
            self.assertEqual(fake_out.getvalue(), answer_key)

    def test_print_plan_with_no_solution(self):
        """
        Test printing the solution in stdout with no solution
        """
        # Input:
        plan = None
        # Answer key:
        answer_key = "No solution found.\n"
        # Assert:
        with patch("sys.stdout", new=StringIO()) as fake_out:
            asyncio.run(print_plan(plan))
            self.assertEqual(fake_out.getvalue(), answer_key)

    def test_main(self):
        """
        # Test main function
        It is mainly a driver function for development purposes.
        It should return True if everything runs fine.
        """
        # Input:
        # No input argument
        # Output:
        output = asyncio.run(main())
        # Answer key:
        answer_key = True
        # Assert:
        self.assertEqual(output, answer_key)


if __name__ == "__main__":
    unittest.main()
