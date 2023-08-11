#!/usr/bin/env python3
"""
2-measure_runtime module
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time of wai_n"""
    # record start time
    start_time = time.perf_counter()

    # execute the function
    asyncio.run(wait_n(n, max_delay))

    # record end time
    end_time = time.perf_counter()

    total_time = end_time - start_time

    return total_time / n
