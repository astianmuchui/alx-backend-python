#!/usr/bin/env python3
"""
Task 101
Annotate the given function
"""
from typing import TypeVar, Mapping, Any, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key:
                     Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Annotated function safely_get_value that takes a Mapping dct,
    a key, and a default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
