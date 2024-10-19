#!/usr/bin/env python3
"""
A module to measure the runtime of running async_comprehension
four times in parallel.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension
    four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()

    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    total_runtime = time.perf_counter() - start_time
    return total_runtime
