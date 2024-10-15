#!/usr/bin/env python3
"""
This module provides a function to zoom into an array by repeating it
elements.
"""


from typing import List, Tuple, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List[int]:
    """
    Zoom into an array by repeating each element a specified number of times.

    Args:
        lst (Tuple[int, ...]): A tuple of integers.
        factor (int): The number of times to repeat each element.

    Returns:
        List[int]: A list with the zoomed-in array elements.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
