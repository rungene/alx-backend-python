#!/usr/bin/env python3
"""
0-basic_async_syntax module
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that returns generated random value
    """
    # random floating point generated
    delay: float = random.uniform(0, max_delay)
    # Wait for specified amount of time asyncronusly
    await asyncio.sleep(delay)
    return delay
