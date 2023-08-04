#!/usr/bin/env python3
"""
8-make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ takes a float multiplier as argument and
    returns a function"""
    def multiply(value: float) -> float:
        """
        returns a function that multiplies a float
        by multiplier."""
        return value * multiplier
    return multiply
