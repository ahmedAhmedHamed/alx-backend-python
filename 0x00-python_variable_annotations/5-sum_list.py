#!/usr/bin/env python3
"""
module for the sum_list function with type annotation
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    returns the sum of a list of floats.
    """
    return sum(input_list)
