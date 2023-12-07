#!/usr/bin/env python3
""" Type Checking  """
from typing import List, Tuple, Union


def zoom_array(lst: List, factor: Union[int, float] = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


if __name__ == "__main__":
    array = [12, 72, 91]

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3.0)
