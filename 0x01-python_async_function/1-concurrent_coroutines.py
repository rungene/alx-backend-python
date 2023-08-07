#!/usr/bin/env python3
"""
1-concurrent_coroutines module
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    execute multiple coroutines at the same time with async
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]

    done, _ = await asyncio.wait(coroutines, return_when=asyncio.ALL_COMPLETED)

    # sort extract delays from task completed
    sorted_delays = sorted(task_done.result() for task_done in done)

    return sorted_delays
