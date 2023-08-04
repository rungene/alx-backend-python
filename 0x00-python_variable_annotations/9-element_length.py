#!/usr/bin/env python3
"""
9-element_length module
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable of Sequence(args), returns a List of Tuples with
    two elements. Where each Tuple contains a Sequence(any type) and int"""
    return [(i, len(i)) for i in lst]
