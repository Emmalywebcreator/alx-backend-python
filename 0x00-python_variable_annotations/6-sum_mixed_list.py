#!/usr/bin/env python3
"""
This module provides a function to sum a mixed list of integers
and floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    A type-annotated function that takes a mixed list of integers and
    floats as an argument and returns their sum.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers
        and floats.

    Returns:
        float: The sum of the numbers in the list as a float.
    """
    return float(sum(mxd_lst))
