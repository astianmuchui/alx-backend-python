#!/usr/bin/env python3
"""
Task: Annotate the given function
"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable) -> List[Tuple[Sequence, int]]:
    """
    Task: Annotate the given function
    """

    return [(i, len(i)) for i in lst]
