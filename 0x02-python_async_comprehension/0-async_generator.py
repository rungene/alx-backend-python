#!/usr/bin/env python3
"""
0-async_generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async generators that takes no arguments."""
    count = 0
    while count < 10:
        await asyncio.sleep(random.uniform(0, 1))
        yield random.uniform(0, 10)
        count += 1
