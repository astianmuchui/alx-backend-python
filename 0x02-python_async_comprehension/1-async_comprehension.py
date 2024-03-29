#!/usr/bin/env python3

"""
coroutine async_comprehension
that takes no arguments
collects the 10 random numbers and returns them

"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine async_comprehension
    that takes no arguments
    collects the 10 random numbers and returns them
    """

    ls: List[float] = [i async for i in async_generator()]
    return ls
