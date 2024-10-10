#!/usr/bin/env python3
"""
module for the make_multiplier function with type annotation
"""
from typing import Callable, Tuple, List, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ a tuple of number, number """
    return [(i, len(i)) for i in lst]
