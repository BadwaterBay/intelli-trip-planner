#!/usr/bin/env python

"""
Test helpers.py
"""

import unittest
from core.helpers.helper import seconds_in_x_hours


class TestHelpersHelper(unittest.TestCase):
    """
    # Test helper.py
    """

    def test_seconds_in_x_hours_1(self):
        """
        # Test seconds_in_x_hours with no argument
        """
        # Input:
        # No argument
        # Ouput:
        output: int = seconds_in_x_hours()
        # Answer key:
        answer_key = 0
        # Assert:
        self.assertEqual(output, answer_key)

    def test_seconds_in_x_hours_2(self):
        """
        # Test seconds_in_x_hours with a variety of arguments
        """
        # Input:
        input_hours = [
            0,
            1,
            3,
            24,
            177,
            2147483647,
            1.3,
            2.67832,
            round(3.1416),
            -16,
            int,
            "abc",
            "",
            True,
            False,
            None,
            [],
            (),
        ]
        # Ouput:
        output = []
        for x_hours in input_hours:
            output.append(seconds_in_x_hours(x_hours))
        # Answer key:
        answer_key = [
            0,
            3600,
            10800,
            86400,
            637200,
            7730941129200,
            4680,
            9642,
            10800,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ]
        # Assert:
        self.assertEqual(output, answer_key)


if __name__ == "__main__":
    unittest.main()
