#!/usr/bin/env python3
""" mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats and returns their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): input list of integers & floats.

    Returns:
        float: The sum of the input list of integers and floats.
    """
    return sum(mxd_lst)
