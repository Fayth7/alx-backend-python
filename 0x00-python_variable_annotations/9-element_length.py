#!/usr/bin/env python3
""" Let's duck type an iterable object"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences 'lst' and returns a list of tuples.
    Each tuple contains an element from 'lst' and its corresponding length.

    Args:
        lst (Iterable[Sequence]): The input iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]
    """
    return [(i, len(i)) for i in lst]


if __name__ == "__main__":
    print(element_length.__annotations__)
