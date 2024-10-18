#!/usr/bin/env python3
"""
Module to execute multiple asyncio tasks using task_wait_random.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes multiple asyncio tasks using task_wait_random and
    returns a list of delays in the order they are completed.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        List[float]: List of delays in the order of completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_tasks = [await task for task in asyncio.as_completed(tasks)]
    return completed_tasks
