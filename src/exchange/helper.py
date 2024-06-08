import asyncio
import functools

from src.redis import RedisData, get_by_key, set_redis_key


def cache(seconds):
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            key = f"{func.__name__}_{kwargs.get("base")}"

            redis_data = await get_by_key(key)
            if redis_data:
                return redis_data

            response: bytes = await func(*args, **kwargs)
            _bg_task = asyncio.create_task(
                set_redis_key(RedisData(key=key, value=response, ttl=seconds))
            )
            await asyncio.sleep(0)
            return response

        return wrapped

    return wrapper
