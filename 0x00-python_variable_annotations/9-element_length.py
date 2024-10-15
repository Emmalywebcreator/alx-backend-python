#!/usr/bin/env python3
"""
Duck type iterable object
Annotate a function's parameter and return values
with appropriate types
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples, where
    each tuple contains a sequence and its corresponding length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a
        sequence and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
