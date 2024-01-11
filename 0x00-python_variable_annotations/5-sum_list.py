#!/usr/bin/env python3
"""
function for sum of a list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums a list of floats.

    Args:
        input_list (List[float]): a list of floats.

    Returns:
        float: the sum of the input_list.

    """
    return sum(input_list)
