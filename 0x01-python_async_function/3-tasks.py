#!/usr/bin/env python3
"""
Function to create an asyncio.Task for wait_random.
"""

import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for wait_random.

    :param max_delay: The maximum delay in seconds.
    :return: An asyncio.Task for wait_random.
    """
    wait_random = __import__('0-basic_async_syntax').wait_random

    return asyncio.create_task(wait_random(max_delay))


if __name__ == "__main__":
    # Example usage in an async function
    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
