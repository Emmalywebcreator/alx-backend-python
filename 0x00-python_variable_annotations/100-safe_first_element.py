#!/usr/bin/env python3
"""
Duck type a function's parameter and return value
with appropriate annotations.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the sequence if it's not empty,
    otherwise returns None.

    Args:
        lst (Sequence[Any]): A sequence of elements of any type.

    Returns:
        Union[Any, None]: The first element of the sequence or None if
        empty.
    """
    if lst:
        return lst[0]
    else:
        return None
