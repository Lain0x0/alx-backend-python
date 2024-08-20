#!/usr/bin/env python3
""" 0-asyncio_generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Using asyncio and random to yield a random number looped
    between 0 and 10 """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 1)
