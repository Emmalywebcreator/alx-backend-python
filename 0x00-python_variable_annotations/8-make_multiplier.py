#!/usr/bin/env python3
"""
This module provides a function that returns a multiplier
function.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A type-annotated function that takes a float multiplier and
    returns a function that multiplies a float by the multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns a float after multiplying by the multiplier.
    """
    def multiply(value: float) -> float:
        """
        Multiplies a float value by the given multiplier.

        Args:
            value (float): The float value to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return value * multiplier

    return multiply
