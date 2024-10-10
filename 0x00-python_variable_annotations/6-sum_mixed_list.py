#!/usr/bin/env python3
"""
module for the sum_mixed_list function with type annotation
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float | int]]) -> float:
    """
    returns the sum of a list of floats and integers only.
    """
    return sum(mxd_lst)
