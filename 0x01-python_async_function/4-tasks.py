#!/usr/bin/env python3

"""
Import wait_random from 0-basic_async_syntax
and write a function wait_n that takes in 2 int arguments
(max_delay: int and n: int) and returns a list of n floats.

"""

import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that takes in 2 int arguments"""
    list_of_delays: List[float] = [await task_wait_random
                                   (max_delay) for i in range(n)]
    return sorted(list_of_delays)
