#!/usr/bin/env python3
"""
This file contains the function to_kv
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    Given a string k and an int OR float v as arguments,
    returns a tuple with k as first element and v squared as second element
    """
    return k, v ** 2
