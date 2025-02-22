#!/usr/bin/env python3

"""This module provides a function to take
    a string and float to return a tuple.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A function that takes a string k and an int OR float v
        as arguments and returns a tuple.
    """
    elementSquare = float(v * v)
    return (k, elementSquare)
