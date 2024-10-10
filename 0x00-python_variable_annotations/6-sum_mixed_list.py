#!/usr/bin/env python3

""" module for the sum_mixed_list function with type annotation """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns sum as a float. """
    return float(sum(mxd_lst))
