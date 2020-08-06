#!/usr/bin/env python

"""
Decorators
"""

import functools
from typing import List, Tuple, Union, Callable


def convert_to_tuple(func) -> Callable[..., Tuple]:
    """
    # Decorator for converting the return value to a N-dimensional tuple, \
    whether from a list, a tuple, a nested list, a nested tuple or a combination
    """

    @functools.wraps(func)
    def convert_return_to_tuple(*args, **kwargs) -> Callable[..., Tuple]:
        """
        # Convert return value to tuple
        """

        def list_to_tuple(input_list: Union[List, Tuple]) -> Tuple:
            """
            # Recursively convert an N-dimensional list to an N-dimensional tuple
            - :param input_list: Input N-dimensional list
            - :type input_list: list
            - :return: N-dimensional tuple
            - :rtype: tuple
            """
            if isinstance(input_list, (list, tuple)):
                return tuple(map(list_to_tuple, input_list))
            return input_list

        return list_to_tuple(func(*args, **kwargs))

    return convert_return_to_tuple


def convert_to_list(func) -> Callable[..., List]:
    """
    # Decorator for converting the return value to a N-dimensional list, \
    whether from a list, a tuple, a nested list, a nested tuple or a combination
    """

    @functools.wraps(func)
    def convert_return_to_list(*args, **kwargs) -> Callable[..., List]:
        """
        # Convert return value to list
        """

        def tuple_to_list(input_tuple: Tuple) -> List:
            """
            # Recursively convert an N-dimensional tuple to an N-dimensional list
            - :param input_tuple: Input N-dimensional tuple
            - :type input_tuple: tuple
            - :return: N-dimensional tuple
            - :rtype: list
            """
            if isinstance(input_tuple, (tuple, list)):
                return list(map(tuple_to_list, input_tuple))
            return input_tuple

        return tuple_to_list(func(*args, **kwargs))

    return convert_return_to_list
