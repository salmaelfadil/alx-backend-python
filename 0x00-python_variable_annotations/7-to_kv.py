#!/usr/bin/env python3
"""Tuple module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple of the arguments"""
    return (k, float(v**2))
