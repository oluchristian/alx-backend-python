#!/usr/bin/env python3
# Basics of async

import asyncio
import random

async def wait_random(max_delay = 10):
    """Coroutin that generates a random float
    and returns it
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
