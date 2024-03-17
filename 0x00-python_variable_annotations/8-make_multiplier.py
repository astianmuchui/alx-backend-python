#!/usr/bin/env python3
"""
Type annotated function make_multiplier
that takes a float multiplier as an argument
and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Function that takes a float multiplier as an argument
    and returns a function that multiplies a float by multiplier"""

    def multiplier_func(x: float) -> float:
        """ Function that multiplies a float by multiplier"""
        return x * multiplier

    return multiplier_func
