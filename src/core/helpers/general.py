#!/usr/bin/env python

"""
Helper functions
"""

import sys
from typing import Union


def get_seconds_in_x_hours(x_hours: Union[int, float, None] = 0) -> int:
    if isinstance(x_hours, bool):
        return 0
    if isinstance(x_hours, (int, float)) and (x_hours >= 0):
        return round(3600 * x_hours)

    error_message = (
        "A negative x_hours or an invalid data type was given. Return default value 0."
    )
    print(
        error_message,
        file=sys.stderr,
    )
    return 0
