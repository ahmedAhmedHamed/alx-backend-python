#!/usr/bin/env python3
""" final annotation exercise """
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ zooms in an array by duplicating its members """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
