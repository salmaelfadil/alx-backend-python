#!/usr/bin/env python3
"""Async function"""
import asyncio
async_generator = __import__('0-async_generator').async_generator
from typing import List

async def async_comprehension() -> List[float]:
    """async func"""
    random_numbers = [number async for number in async_generator()]
    return random_numbers
