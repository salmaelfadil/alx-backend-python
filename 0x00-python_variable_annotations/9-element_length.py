#!/usr/bin/env python3
"""iterable module"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns list of tuple of sequence and length"""
    return [(i, len(i)) for i in lst]
