#!/usr/bin/env python3
"""
Annotated function to_kv
that takes in a string k and an int OR float v as arguments
and returns a tuple of the form (k, v)
The second element of the tuple is the square of the argument
and should be annotated as a float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Function to_kv that takes in a string k and an int OR float v
    as arguments and returns a tuple of the form (k, v)
    The second element of the tuple is the square of the argument
    and should be annotated as a float"""
    return (k, v ** 2)
