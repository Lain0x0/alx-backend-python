#!/usr/bin/env python3
""" 1-Async_Comprehensions """
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ Importing the previous code and return a list
    of number from async_generator """
    return [nmb_list async for nmb_list in async_generator()]
