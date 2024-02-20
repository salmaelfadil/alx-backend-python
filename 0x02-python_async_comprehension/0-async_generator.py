#!/usr/bin/env python3
"""Async Function"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async function that produces random numbers after waiting 1 sec"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
