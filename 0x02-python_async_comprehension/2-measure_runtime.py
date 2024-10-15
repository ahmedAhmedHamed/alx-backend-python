#!/usr/bin/env python3
""" async generator tutorial """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ execute async_comprehension four
    times in parallel using asyncio.gather """
    before = time.time()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    after = time.time()
    return after - before
