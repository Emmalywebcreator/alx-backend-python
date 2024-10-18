#!/usr/bin/env python3
"""
This module measure the average runtime of wait_n coroutine
"""


import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total time ti takes to execute wait_n coroutine
    and returns the average time.

    args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay for each wait_random

    Returns:
        float: Average runtime for each execution of wait_n
    """

    start_time = time.perf_counter()
    asyncio.run( wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
