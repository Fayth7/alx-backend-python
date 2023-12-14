#!/usr/bin/env python3
''' Import async_comprehension from the previous file and write a
    measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.

    measure_runtime should measure the total runtime and return it.
'''


import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Runs async comprehension in parallel and returns the total time'''
    start_time = time()

    await asyncio.gather(
        *[async_comprehension() for _ in range(4)]
    )

    end_time = time()
    return end_time - start_time


# Example usage
async def main():
    return await measure_runtime()

if __name__ == "__main__":
    print(asyncio.run(main()))
