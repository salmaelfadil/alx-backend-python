#!/usr/bin/env python3
"""Async func"""
wait_n = __import__('1-concurrent_coroutines').wait_n
import asyncio
import time


def measure_time(n, max_delay):
    """measures execution time"""
    start = time.time()

    asyncio.run(wait_n(n, max_delay))

    end = time.time()

    return (end - start) / n
