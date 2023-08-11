#!/usr/bin/env python3
"""
4-tasks module
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates task returns List of floats
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = [await task for task in asyncio.as_completed(tasks)]

    return delays
