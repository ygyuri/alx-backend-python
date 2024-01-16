#!/usr/bin/env python3
"""
Function for Async Comprehensions
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects  numbers using async comprehensions
    and returns 10 random float numbers as a list
    """
    return [i async for i in async_generator()]
