#!/usr/bin/env python3
""" concurrency tutorial """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ waits for n instances of wait_random with delay max_delay """
    task_list = []
    ret = []
    for i in range(n):
        task_list.append(asyncio.create_task(wait_random(max_delay)))
    for t in asyncio.as_completed(task_list):
        ret.append(await t)
    return ret
