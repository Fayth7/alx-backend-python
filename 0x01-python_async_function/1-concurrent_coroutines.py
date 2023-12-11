#!/usr/bin/env python3
"""
Async routine that spawns wait_random n times with the specified max_delay.
"""

import asyncio
from typing import List

from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns wait_random n times with the specified max_delay.

    :param n: The number of times to spawn wait_random.
    :param max_delay: The maximum delay in seconds.
    :return: The list of delays in ascending order.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random

    delay_list = []
    i = 0

    while i < n:
        delay_list.append(await wait_random(max_delay))
        i += 1

    return sorted(delay_list)


if __name__ == "__main__":
    # Example usage
    print(asyncio.run(wait_n(5, 2)))
    print(asyncio.run(wait_n(7, 4)))
    print(asyncio.run(wait_n(10, 0)))
