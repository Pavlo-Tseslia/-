import asyncio
import functools

def async_wrap(func):
    """
    Декоратор, який виконує звичайну функцію асинхронно за допомогою asyncio.
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, func, *args, **kwargs)
    return wrapper
