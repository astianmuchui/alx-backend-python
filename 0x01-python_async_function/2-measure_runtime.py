#!/usr/bin/env python3

"""
Measure runtime
"""

import asyncio
import time
import typing
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Asynchronous coroutine that takes in 2 int arguments"""
    start_time: float = time.time()
    await asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    return (end_time - start_time) / n
