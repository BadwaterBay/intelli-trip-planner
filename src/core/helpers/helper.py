#!/usr/bin/env python

"""
Helper functions
"""

import sys
from typing import Union


def seconds_in_x_hours(x_hours: Union[int, float, None] = 0) -> int:
    """
    # Calculate the number of seconds in x hours
    - :param x_hours: Nonnegative integer representing the number of hours.
    - :type x_hours: int | float | None
    - :return: the number of seconds in x hours. Default to 0 if error occurs.
    - :rtype: int
    """
    if isinstance(x_hours, (int, float)) and (x_hours >= 0):
        return round(3600 * x_hours)
    print(
        "A negative x_hours or an invalid data type was given. Return default value 0.",
        file=sys.stderr,
    )
    return 0
