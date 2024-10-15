#!/usr/bin/env python3
""" async generator tutorial """
import asyncio
import random


async def async_generator() -> float:
    """ yields a random number between 0 and 10 every second for 10 seconds """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
