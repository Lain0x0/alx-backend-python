#!/usr/bin/env python3
""" 11_more annotation types """
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """ A function that retrieves a value from a dict using a given key """
    if key in dct:
        return dct[key]
    else:
        return default
