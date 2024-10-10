#!/usr/bin/env python3
"""
module for the to_kv function with type annotation
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    adds a and b, meant for floats and integers only.
    """
    return k, v ** 2
