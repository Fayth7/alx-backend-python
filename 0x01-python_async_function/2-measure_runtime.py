#!/usr/bin/env python3
"""
Measure the total execution time for wait_n(n, max_delay).
"""

import asyncio
from typing import List
import time


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure execution time for wait_n(n, max_delay) & return total_time / n.

    :param n: The number of times to spawn wait_random.
    :param max_delay: The maximum delay in seconds.
    :return: The average time taken for each execution.
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    average_time = total_time / n
    return average_time


if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
