#!/usr/bin/env python3
"""
Function to execute multiple coroutines
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Generate wait_random n times with the
    specified max_delay and return all delays
    """
    delays = []
    all_delays = []

    for i in range(n):
        delays.append(wait_random(max_delay))

    for delay in asyncio.as_completed(delays):
        all_delays.append(await delay)

    return all_delays
