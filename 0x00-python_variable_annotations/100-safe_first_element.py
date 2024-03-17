#!/usr/bin/env python3
"""
Task: Annotate the given function
"""


from typing import Iterable, List, Tuple, Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Task: Annotate the given function
    """
    if lst:
        return lst[0]
    else:
        return None
