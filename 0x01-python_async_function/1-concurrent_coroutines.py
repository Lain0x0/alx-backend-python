#!/usr/bin/env python3
""" 1-concurent_coroutines """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Waiting delay within time effect defined as n """
    listdelay = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*listdelay)
    return sorted(delays)
