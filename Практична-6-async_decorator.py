import asyncio
from functools import wraps

def async_run(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        async def run():
            return func(*args, **kwargs)
        return asyncio.run(run())
    return wrapper
