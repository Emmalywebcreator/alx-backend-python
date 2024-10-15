#!/usr/bin/env python3
"""
This module provides a function to sum a list of floats.
"""


def sum_list(input_list: list[float]) -> float:
    """
    A type-annotated function that takes a list of floats as an argument
    and returns their sum.

    Args:
        input_list (list[float]): A list of float numbers.

    Returns:
        float: The sum of the float numbers in the list.
    """
    return sum(input_list)
