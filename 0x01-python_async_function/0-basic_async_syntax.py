#!/usr/bin/env python3
"""
Function for the basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    returns time of random delay between 0 and max_delay seconds using asyncio
    """
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
