#!/usr/bin/env python3
""" More involved type annotations  """
from typing import Mapping, TypeVar, Any, Union, Optional


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None
                     ) -> Union[Any, T]:
    """
    Safely retrieves value associated with the given key from the dictionary.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to retrieve the value for.
        default (Optional[T]):default value to return if key is not present.

    Returns:
        Union[Any, T]
    """
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == "__main__":
    annotations = safely_get_value.__annotations__
    print("Here's what the mappings should look like")
    for k, v in annotations.items():
        print("{}: {}".format(k, v))
