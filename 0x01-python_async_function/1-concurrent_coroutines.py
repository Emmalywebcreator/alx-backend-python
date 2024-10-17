#!/usr/bin/env python3
"""
This module executes multiples coroutines concurrently
using asyncio. It contains a coroutin (wait_n) that spawns
several instances of anothe corountin, (wait_random) and
returns a list of delays in the order that the coroutines finish.
"""


import asyncio
from typing import List
import random

"""
Used _import_ to import wait_random from 0-basic_async_syntax
"""
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchonous coroutine that spawns wait_random n times with
    max_delay and returns a list of delays in the order they
    are completed.

    Args:
        n (int): Number of coroutines to spawn
        max_delay (int): Maximum delay foor wait_random

    Returns:
        List [flat]: List of all delays in ascending order
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    completed_delays = [await task for task in asyncio.as_completed(tasks)]
    return completed_delays
