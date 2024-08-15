#!/usr/bin/env python3
""" 8-make_multiplayer_tuple  """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ A function return a function multiplies a float by multiple it """
    def multiple(m: float) -> float:
        """ A function that multiplies a float by multiple it """
        return m * multiplier
    return multiple
