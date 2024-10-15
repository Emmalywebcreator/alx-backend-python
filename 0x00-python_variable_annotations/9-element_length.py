#!/usr/bin/env python3
"""
This module provides a function that returns a list of
tuples with elements and their corresponding lengths.
"""


from typing import List, Tuple, Interable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A type-annotated function that takes a list of strings and returns
    a list of tuples where each tuple contains an element and its length.

    Args:
        lst (Sequence[Any]): A sequence of strings.

    Returns:
        List[Tuple[Any, int]]: A list of tuples, each containing
        a string and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
