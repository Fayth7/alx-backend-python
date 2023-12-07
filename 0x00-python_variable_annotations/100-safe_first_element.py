#!/usr/bin/env python3
""" Duck typing - first element of a sequence """
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely returns the first element of the input sequence 'lst'.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]
    """
    if lst:
        return lst[0]
    else:
        return None


if __name__ == "__main__":
    print(safe_first_element.__annotations__)
