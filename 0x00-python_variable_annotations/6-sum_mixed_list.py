#!/usr/bin/env python3

"""This module provides a function to sum a list of ints and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A function that takes a list mxd_lst of integers
        and floats and returns their sum as a float.
    """
    return float(sum(mxd_lst))
