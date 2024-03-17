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


array = (12, 72, 91)  # Use parentheses to create a tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
