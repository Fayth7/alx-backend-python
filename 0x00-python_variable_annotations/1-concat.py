#!/usr/bin/env python3
""" Basic annotations concat """


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string of str1 and str2.
    """
    return str1 + str2


if __name__ == "__main__":
    str1 = "egg"
    str2 = "shell"
    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)
