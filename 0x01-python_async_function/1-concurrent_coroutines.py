#!/usr/bin/env python3
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio
"""async func"""


async def wait_n(n, max_delay):
    tasks = [wait_random(max_delay) for _ in range(n)];
    return sorted(await asyncio.gather(*tasks))

