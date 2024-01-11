#!/usr/bin/env python3
"""
Function to anntoniate the arguments to get right results
"""

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Given a list `lst`, returns a list of tuples containing each element
    of `lst` along with its length.
    """
    return [(i, len(i)) for i in lst]
