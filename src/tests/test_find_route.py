#!/usr/bin/env python

"""
Test find_route.py
"""

import unittest
from unittest.mock import patch
from io import StringIO
import asyncio
from core.find_route import (
    construct_premise_for_solving_for_optimal_route,
    print_optimal_route,
    solve_for_optimal_route,
    main,
)
from tests.load_answer_key import load_parsed_distance_matrix_tuple


class TestFindRoute(unittest.TestCase):
    def test_construct_premise_for_solving_for_optimal_route_1(self):
        output = asyncio.run(construct_premise_for_solving_for_optimal_route())
        answer_key = None
        self.assertEqual(output, answer_key)

    def test_construct_premise_for_solving_for_optimal_route_2(self):
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()
        output = asyncio.run(
            construct_premise_for_solving_for_optimal_route(
                parsed_distance_matrix["distance"],
                parsed_distance_matrix["duration"],
            )
        )
        answer_key = {
            "distance_matrix": parsed_distance_matrix["distance"],
            "duration_matrix": parsed_distance_matrix["duration"],
            "num_vehicles": 1,
            "depot": 0,
        }
        self.assertEqual(output, answer_key)

    def test_solve_for_optimal_route_distance_without_quota_1(self):
        """
        # Test solving for simple traveling salesman problem without quota
        ## Parameters:
        - Use distance for calculation
        - Test solve_for_optimal_route() with missing `quota` argument
        """
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()

        async def get_output():
            """
            Output
            """
            data = await construct_premise_for_solving_for_optimal_route(
                parsed_distance_matrix["distance"],
                parsed_distance_matrix["duration"],
            )
            return await solve_for_optimal_route(data, "distance_matrix")

        output = asyncio.run(get_output())
        answer_key = {
            "waypoints": [0, 6, 7, 8, 9, 3, 4, 1, 5, 2, 0],
            "objective_value": 3076045,
            "true_value": 3076045,
            "quota": None,
        }
        self.assertEqual(output, answer_key)

    def test_solve_for_optimal_route_distance_without_quota_2(self):
        """
        # Test solving for simple traveling salesman problem without quota
        ## Parameters:
        - Use distance for calculation
        - Test solve_for_optimal_route() with `quota` set to 0
        """
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()

        async def get_output():
            """
            Output
            """
            data = await construct_premise_for_solving_for_optimal_route(
                parsed_distance_matrix["distance"],
                parsed_distance_matrix["duration"],
            )
            return await solve_for_optimal_route(data, "distance_matrix", 0)

        output = asyncio.run(get_output())
        answer_key = {
            "waypoints": [0, 6, 7, 8, 9, 3, 4, 1, 5, 2, 0],
            "objective_value": 3076045,
            "true_value": 3076045,
            "quota": None,
        }
        self.assertEqual(output, answer_key)

    def test_solve_for_optimal_route_duration_without_quota_1(self):
        """
        # Test solving for simple traveling salesman problem without quota
        ## Parameters:
        - Use duration for calculation
        - Test solve_for_optimal_route() with missing `quota` argument
        """
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()

        async def get_output():
            """
            Output
            """
            data = await construct_premise_for_solving_for_optimal_route(
                parsed_distance_matrix["distance"],
                parsed_distance_matrix["duration"],
            )
            return await solve_for_optimal_route(data, "duration_matrix")

        output = asyncio.run(get_output())
        answer_key = {
            "waypoints": [0, 6, 7, 8, 9, 3, 4, 1, 5, 2, 0],
            "objective_value": 120524,
            "true_value": 120524,
            "quota": None,
        }
        self.assertEqual(output, answer_key)

    def test_solve_for_optimal_route_duration_without_quota_2(self):
        """
        # Test solving for simple traveling salesman problem without quota
        ## Parameters:
        - Use duration for calculation
        - Test solve_for_optimal_route() with `quota` set to 0
        """
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()

        async def get_output():
            data = await construct_premise_for_solving_for_optimal_route(
                parsed_distance_matrix["distance"],
                parsed_distance_matrix["duration"],
            )
            return await solve_for_optimal_route(data, "duration_matrix", 0)

        output = asyncio.run(get_output())
        answer_key = {
            "waypoints": [0, 6, 7, 8, 9, 3, 4, 1, 5, 2, 0],
            "objective_value": 120524,
            "true_value": 120524,
            "quota": None,
        }
        self.assertEqual(output, answer_key)

    def test_solve_for_optimal_route_distance_with_quota(self):
        """
        # Test solving for simple traveling salesman problem with quota
        ## Parameters:
        - Use distance for calculation
        - `quota` has a nonzero value
        """
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()
        quota = int(2000000)  # Unit: meters

        async def get_output():
            data = await construct_premise_for_solving_for_optimal_route(
                parsed_distance_matrix["distance"],
                parsed_distance_matrix["duration"],
            )
            return await solve_for_optimal_route(data, "distance_matrix", quota)

        output = asyncio.run(get_output())
        answer_key = {
            "waypoints": [0, 2, 5, 1, 4, 3, 0],
            "objective_value": 14751175,
            "true_value": 1583927,
            "quota": quota,
        }
        self.assertEqual(output, answer_key)

    def test_solve_for_optimal_route_duration_with_quota(self):
        """
        # Test solving for simple traveling salesman problem with quota
        ## Parameters:
        - Use duration for calculation
        - `quota` has a nonzero value
        """
        parsed_distance_matrix = load_parsed_distance_matrix_tuple()
        quota = int(3600 * 8)  # Set quota to be 8 hours

        async def get_output():
            data = await construct_premise_for_solving_for_optimal_route(
                parsed_distance_matrix["distance"],
                parsed_distance_matrix["duration"],
            )
            return await solve_for_optimal_route(data, "duration_matrix", quota)

        output = asyncio.run(get_output())
        answer_key = {
            "waypoints": [0, 2, 3, 0],
            "objective_value": 857423,
            "true_value": 21602,
            "quota": quota,
        }
        self.assertEqual(output, answer_key)

    def test_print_optimal_route_with_valid_solution(self):
        plan = {
            "waypoints": [0, 6, 7, 8, 9, 3, 4, 1, 5, 2, 0],
            "objective_value": 3076045,
            "true_value": 3076045,
            "quota": None,
        }
        answer_key = (
            "Objective: 3076045 units\n"
            "True: 3076045 units\n"
            "Quota: None units\n"
            "0 -> 6 -> 7 -> 8 -> 9 -> 3 -> 4 -> 1 -> 5 -> 2 -> 0\n"
        )
        with patch("sys.stdout", new=StringIO()) as fake_out:
            asyncio.run(print_optimal_route(plan))
            self.assertEqual(fake_out.getvalue(), answer_key)

    def test_print_optimal_route_with_no_solution(self):
        plan = None
        answer_key = "No solution found.\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            asyncio.run(print_optimal_route(plan))
            self.assertEqual(fake_out.getvalue(), answer_key)

    def test_main(self):
        output = asyncio.run(main())
        answer_key = True
        self.assertEqual(output, answer_key)


if __name__ == "__main__":
    unittest.main()
