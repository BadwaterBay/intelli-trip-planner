#!/usr/bin/env python

"""
Main script for unit testing
"""

import os
import sys
import unittest

cur_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(cur_dir, "..", "..")
sys.path.insert(1, src_dir)

# pylint: disable=wrong-import-position
from core.traveling_salesman import solve_for_plan

# pylint: enable=wrong-import-position


class TestSolveForPlan(unittest.TestCase):
    """
    Main testing class
    """

    def test_list_int(self):
        """
        Test solving for simple traveling salesman problem
        """

        # Input argument values
        filepath = os.path.join(cur_dir, "mock_data/distance_matrix_list.pkl")

        # Get output
        output = solve_for_plan(filepath)

        # Get answerkey
        answerkey = {
            "waypoints": [0, 2, 5, 1, 4, 3, 9, 8, 7, 6, 0],
            "objective_value": 3076291,
            "true_value": 3076291,
        }

        # Assert
        self.assertEqual(output, answerkey)


if __name__ == "__main__":
    unittest.main()
