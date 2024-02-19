#!/usr/bin/env python3
"""Async func"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random number of seconds"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
