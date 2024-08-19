#!/usr/bin/env python3
""" 3_tasks """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Returning async function """
    return asyncio.create_task(wait_random(max_delay))
