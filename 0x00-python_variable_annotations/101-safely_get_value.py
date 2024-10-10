#!/usr/bin/env python3
""" annotation exercise 2 """
from typing import Any, Union, TypeVar, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ clone of the map.get() function """
    if key in dct:
        return dct[key]
    else:
        return default
