#!/usr/bin/env python3
"""Duck Type annotation"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return the first element of a sequence."""
    if lst:
        return lst[0]
    else:
        return None
