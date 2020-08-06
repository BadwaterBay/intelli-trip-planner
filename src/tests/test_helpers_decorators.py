#!/usr/bin/env python

"""
Test decorators.py
"""

import unittest
from core.helpers.decorators import convert_to_tuple, convert_to_list


class TestHelpersDecorators(unittest.TestCase):
    """
    # Test core.helpers.decorators
    """

    def test_convert_to_tuple(self):
        """
        # Test decorator convert_to_tuple
        """

        @convert_to_tuple
        def return_arg(test_case):
            return test_case

        test_cases = [
            [[1, 2], [3, 4]],
            [[[0, 0], [0, 0]], [[0, 0], [0, 0]]],
        ]
        output = []
        for test_case in test_cases:
            output.append(return_arg(test_case))
        answer_key = [
            ((1, 2), (3, 4)),
            (((0, 0), (0, 0)), ((0, 0), (0, 0))),
        ]
        self.assertEqual(output, answer_key)

    def test_convert_to_list(self):
        """
        # Test decorator convert_to_list
        """

        @convert_to_list
        def return_arg(test_case):
            return test_case

        test_cases = [
            ((1, 2), (3, 4)),
            (((0, 0), (0, 0)), ((0, 0), (0, 0))),
        ]
        output = []
        for test_case in test_cases:
            output.append(return_arg(test_case))
        answer_key = [
            [[1, 2], [3, 4]],
            [[[0, 0], [0, 0]], [[0, 0], [0, 0]]],
        ]
        self.assertEqual(output, answer_key)


if __name__ == "__main__":
    unittest.main()
