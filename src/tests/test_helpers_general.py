#!/usr/bin/env python

"""
Test helpers.py
"""

import unittest
from core.helpers.general import get_seconds_in_x_hours


class TestHelpersGeneral(unittest.TestCase):
    def test_seconds_in_x_hours_1(self):
        output: int = get_seconds_in_x_hours()

        answer_key = 0

        self.assertEqual(output, answer_key)

    def test_seconds_in_x_hours_2(self):
        test_cases = [
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

        output = []
        for x_hours in test_cases:
            output.append(get_seconds_in_x_hours(x_hours))

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

        self.assertEqual(output, answer_key)


if __name__ == "__main__":
    unittest.main()
