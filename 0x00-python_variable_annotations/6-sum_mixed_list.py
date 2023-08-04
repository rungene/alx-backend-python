#!/usr/bin/env python3
"""
6-sum_mixed_list module
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    takes a list mxd_lst of integers and floats and returns
    their sum as a float."""
    return sum(mxd_lst)
