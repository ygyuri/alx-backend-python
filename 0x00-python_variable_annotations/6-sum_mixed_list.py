#!/usr/bin/env python3
"""
function for sum of a mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums a list of integers and floats.

    Args:
        mxd_lst: a list of integers and/or floats.

    Returns:
        The sum of the mixed list as a float.

    """
    return sum(mxd_lst)
