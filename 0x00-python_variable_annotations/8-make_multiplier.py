#!/usr/bin/env python3
"""Multiplier module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies float"""
    def func(i: float) -> float:
        return i * multiplier
    return func
