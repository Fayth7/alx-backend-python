#!/usr/bin/env python3
"""
Async routine that spawns wait_random n times with the specified max_delay.
"""

import asyncio
from typing import List

# Importing wait_random from the previous file
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns wait_random n times with the specified max_delay.

    :param n: The number of times to spawn wait_random.
    :param max_delay: The maximum delay in seconds.
    :return: The list of delays in ascending order.
    """
    # Using gather to concurrently run multiple wait_random coroutines
    tasks = [wait_random(max_delay) for _ in range(n)]
    # Waiting for all tasks to complete
    results = await asyncio.gather(*tasks)
    # Sorting the results in ascending order
    sorted_results = sorted(results)
    return sorted_results


if __name__ == "__main__":
    # Example usage
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
