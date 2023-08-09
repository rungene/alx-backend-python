#!/usr/bin/env python3
"""
0-async_generator
"""
import asyncio
import random


async def async_generator() -> Generators[float, None, None]:
    """
    Async generators that takes no arguments."""
    count = 0
    while count < 10:
        await asyncio.sleep(random.uniform(0, 1))
        yield random.uniform(0, 10)
        count += 1
