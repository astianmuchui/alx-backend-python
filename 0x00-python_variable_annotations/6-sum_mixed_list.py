#!/usr/bin/env python3

"""
Annotated function sum_mixed_list that takes a list
mxd_lst of integers and floats
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Function that takes a list
    mxd_lst of integers and floats"""

    return sum(mxd_lst)
