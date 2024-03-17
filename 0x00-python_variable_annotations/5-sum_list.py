#!/usr/bin/env python3
"""
Annotated function sum_list
that takes in a list input_list of floats
and returns the sum of the list
as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """ Function that takes in a list input_list of floats
    and returns the sum of the list
    as a float."""

    sum: float = 0

    for i in input_list:
        sum += float(i)

    return sum
