#!/usr/bin/env python3
"""
Module that creates an asyncio Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that returns an asyncio Task for wait_random coroutine.

    Args:
        max_delay (int): Maximum delay for wait_random coroutine.

    Returns:
        asyncio.Task: The created asyncio Task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
