#!/usr/bin/env python

"""
Decorators
"""

import functools
from typing import List, Tuple, Union, Callable


def convert_list_to_tuple(func) -> Callable[..., Tuple]:
    """
    # Decorator for converting the return value to a N-dimensional tuple, \
    whether from a list, a tuple, a nested list, a nested tuple or a combination
    """

    @functools.wraps(func)
    def convert_nd_list_to_tuple(*args, **kwargs) -> Callable[..., Tuple]:
        def recurs_convert_nd_list_to_tuple(input_list: Union[List, Tuple]) -> Tuple:
            if isinstance(input_list, (list, tuple)):
                return tuple(map(recurs_convert_nd_list_to_tuple, input_list))
            return input_list

        return recurs_convert_nd_list_to_tuple(func(*args, **kwargs))

    return convert_nd_list_to_tuple


def convert_tuple_to_list(func) -> Callable[..., List]:
    """
    # Decorator for converting the return value to a N-dimensional list, \
    whether from a list, a tuple, a nested list, a nested tuple or a combination
    """

    @functools.wraps(func)
    def convert_nd_tuple_to_list(*args, **kwargs) -> Callable[..., List]:
        def recurs_convert_nd_tuple_to_list(input_tuple: Tuple) -> List:
            if isinstance(input_tuple, (tuple, list)):
                return list(map(recurs_convert_nd_tuple_to_list, input_tuple))
            return input_tuple

        return recurs_convert_nd_tuple_to_list(func(*args, **kwargs))

    return convert_nd_tuple_to_list
