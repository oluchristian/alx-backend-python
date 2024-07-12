#!/usr/bin/env python3
"""Basics of async"""

from asyncio import run
import time

wait_random = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure time"""
    start_time = time.time()
    delays = run(wait_random(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return (total_time / n)
    