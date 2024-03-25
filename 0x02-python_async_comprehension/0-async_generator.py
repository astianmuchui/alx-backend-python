#!/usr/bin/env python3

"""
Async Generator Coroutine
that takes no arguments
It loops 10 times yielding
a random number between 1 and 10
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async Generator Coroutine
    that loops 10 times yielding
    a random number between 1 and 10
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(1, 10)
