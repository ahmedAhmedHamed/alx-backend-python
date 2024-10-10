#!/usr/bin/env python3
"""
module for the sum_mixed_list function with type annotation
"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[float | int]]) -> float:
    """
    returns the sum of a list of floats and integers only.
    """
    return float(sum(mxd_lst))
