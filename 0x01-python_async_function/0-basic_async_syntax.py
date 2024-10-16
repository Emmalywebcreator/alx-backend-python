#!/usr/bin/env python3
import asyncio
import random


"""
A module that produce a coroutine that wait for a random
delay
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that wait for random delay
    between 0 and max_delay seconds

    args:
        max_delay - int: Maximum delay in second
                        defaulted to 10
        returns:
            float: The random delay used
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
