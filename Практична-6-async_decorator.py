import asyncio
from functools import wraps

def async_run(func):
    """Декоратор для асинхронного виконання синхронної функції."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        async def run():
            return func(*args, **kwargs)
        return asyncio.run(run())
    return wrapper
