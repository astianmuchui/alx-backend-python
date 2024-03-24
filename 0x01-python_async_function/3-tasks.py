#!/usr/bin/env python3

"""
task wait random function that
takes in an integer and returns an
asyncio task
"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random: takes in an integer argument (max_delay)
    and returns an asyncio task
    """
    return asyncio.create_task(wait_random(max_delay))
