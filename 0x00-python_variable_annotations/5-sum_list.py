#!/usr/bin/env python3
""" Complex types - list of floats """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats and returns their sum.

    Args:
        input_list (List[float]): The input list of floats.

    Returns:
        float: The sum of the input list of floats.
    """
    return sum(input_list)


if __name__ == "__main__":
    floats = [3.14, 1.11, 2.22]
    floats_sum = sum_list(floats)
    print(floats_sum == sum(floats))
    print(sum_list.__annotations__)
    print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))
