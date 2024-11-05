#!/usr/bin/env python3
"""
Module to implement an asynchronous generator.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    A coroutine that loops 10 times and asynchronously waits for
    1 seconds before yielding a random float number between 0 and 10.

    Yields:
        float: Random numbet between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
