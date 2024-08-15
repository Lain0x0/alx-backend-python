#!/usr/bin/env python3
""" 7-complexe type float """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ A function that return a tuple """
    return (k, v ** 2)
