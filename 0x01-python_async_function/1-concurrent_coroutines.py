#!/usr/bin/env python3
# Basics of async

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
        
    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
    return results
