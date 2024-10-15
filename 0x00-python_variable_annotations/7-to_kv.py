#!/usr/bin/env python3
"""
This module provides a function that returns a tuple with a string and the square of a number.
"""


from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """
    A type-annotated function that takes a string k and an int or float v,
    and returns a tuple. The first element is the string k, and the second
    element is the square of v, annotated as a float.

    Args:
        k (str): A string.
        v (int | float): A number (int or float) whose square will be calculated.

    Returns:
        Tuple[str, float]: A tuple with the string and the square of the number.
    """
    return (k, float(v**2))
