#!/usr/bin/env python3

"""
Import wait_random from 0-basic_async_syntax
and write a function wait_n that takes in 2 int arguments
(max_delay: int and n: int) and returns a list of n floats.

"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(max_delay: int, n: int) -> List[float]:
    """Asynchronous coroutine that takes in 2 int arguments"""
    list_of_delays: List[float] = [await wait_random
                                   (max_delay) for _ in range(n)]
    return sorted(list_of_delays)
