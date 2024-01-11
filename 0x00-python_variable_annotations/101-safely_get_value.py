#!/usr/bin/env python3
"""
Module for safely getting a value from a dictionary
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value from a dictionary safely
    """
    if key in dct:
        return dct[key]
    else:
        return default
