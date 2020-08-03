#!/usr/bin/env python

"""
Test helper functions: read_write.py
"""

import os
import unittest
import asyncio
from core.helpers.read_write import load_dm_pickle
from tests.load_answer_key import load_parsed_distance_matrix


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
        answer_key = load_parsed_distance_matrix()
        # Assert:
        self.assertEqual(output, answer_key)


if __name__ == "__main__":
    unittest.main()
