#!/usr/bin/env python3
"""
This module provides a function that safely gets a value from
a dictionary.
"""
from typing import Mapping, Any, TypeVar, Union


# Define a type variable that can be of any type
T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely get the value of a given key from the dictionary.
    If the key is not present, return the default value.

    Args:
        dct (Mapping[Any, Any]): A dictionary to search.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None]): A default value to return
        if the key is not found.

    Returns:
        Union[Any, T]: The value associated with the key, or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
