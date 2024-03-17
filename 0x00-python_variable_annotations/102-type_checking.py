#!/usr/bin/env python3
"""
Use mypy to fix errors
"""
from typing import Tuple, Any


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """
    Task: Annotate the given function
    and fix errors
    """
    zoomed_in: Tuple = tuple([
        item for item in lst
        for i in range(factor)
    ])
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x: Tuple = zoom_array(array)

zoom_3x: Tuple = zoom_array(array, 3)
