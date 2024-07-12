#!/usr/bin/env python3
"""Basics of async"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Wait n"""
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(task_wait_random(max_delay))
        tasks.append(task)
    results = []
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
    return results
