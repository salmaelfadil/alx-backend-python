#!/usr/bin/env python3
"""async func"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """runs task n number of times"""
    tasks = [task_wait_random(max_delay) for _ in range(n)];
    return sorted(await asyncio.gather(*tasks))
