#!/usr/bin/env python3
""" concurrency tutorial """
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measure the average time of wait_n """
    result: List[float] = asyncio.run(wait_n(n, max_delay))
    return result[-1] / n
