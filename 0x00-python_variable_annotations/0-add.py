#!/usr/bin/env python3

def add(a: float, b: float) -> float:
    """
    Adds two floats and returns their sum.

    Args:
        a (float): The first float.
        b (float): The second float.

    Returns:
        float: The sum of the input floats.
    """
    return a + b

if __name__ == "__main__":
    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
