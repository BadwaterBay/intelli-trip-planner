#!/usr/bin/env python

"""
Test helpers.py
"""

import unittest
from core.helpers.helper import seconds_in_x_hours


class TestHelpersHelper(unittest.TestCase):
    """
    Test helper.py
    """

    def test_seconds_in_x_hours(self):
        """
        Test seconds_in_x_hours
        """
        # Input:
        input_hours: [int] = [0, 1, 3, 8, 24, 97, 177]
        # Ouput:
        output = []
        for x_hours in input_hours:
            output.append(seconds_in_x_hours(x_hours))
        # Answer key:
        answer_key: [int] = [0, 3600, 10800, 28800, 86400, 349200, 637200]
        # Assert:
        self.assertEqual(output, answer_key)


if __name__ == "__main__":
    unittest.main()
