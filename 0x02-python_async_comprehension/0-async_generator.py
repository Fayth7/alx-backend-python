#!/usr/bin/env python3
'''Write a coroutine called async_generator that takes no arguments.

    The coroutine will loop 10 times, each time asynchronously wait 1
    second, then yield a random number between 0 and 10. Use the
    random module.
'''


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Asynchronous generator that yields random floats between 0 and 10.

    Yields:float: Random float between 0 and 10.

    Raises:SomeException: If something goes wrong.

    Returns: None
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


# Example usage
async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

if __name__ == "__main__":
    asyncio.run(print_yielded_values())
