#!/usr/bin/env python3
"""
Function to create asyncio.Tasks for wait_random using task_wait_random.
"""

from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create asyncio.Tasks for wait_random using task_wait_random.

    :param n: The number of times to spawn wait_random.
    :param max_delay: The maximum delay in seconds.
    :return: The list of delays in ascending order.
    """
    modified_random = __import__('3-tasks').task_wait_random

    delay_list = []
    i = 0

    while i < n:
        delay_list.append(await modified_random(max_delay))
        i += 1

    return sorted(delay_list)


if __name__ == "__main__":
    # Example usage
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
