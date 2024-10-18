#!/usr/bin/env python3
"""
This module collects 10 random numbers using async comprehension
"""
from typing import List

"""Import async generator from 0-async_generator.py"""
async_generator = __import__('0-async_generator.py').async_generator


async def async_comprehension() -> List[float]:
    """
    Corontine that collect 10 random number from async_generator, using
    async comprehension

    Returns:
        List[loat]: A list of 10 random floating-point numbers.
    """

    return [num async for num in async_generator()]
