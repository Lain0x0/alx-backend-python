#!/usr/bin/env python3
""" 4_tasks """
import asyncio
from typing import List
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ waiting a random delay between 0 and defined variable """
    listdelay = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*listdelay)
    return sorted(delays)
