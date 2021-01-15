import asyncio
from aioredis import create_redis


async def main():
    redis = await create_redis(("localhost", 6379))
    keys = ["america", "africa", "europe", "asia"]

    async for value in OneAtATime(redis, keys):
        await do_something_with(value)


class OneAtATime:
    def __init__(self, redis, keys):
        self.redis = redis
        self.keys = keys

    def __aiter__(self):
        self.ikeys = iter(self.keys)
        return self

    async def __anext__(self):
        try:
            k = next(self.ikeys)
        except StopIteration:
            raise StopAsyncIteration
        value = await self.redis.get(k)
        return value


if __name__ == "__main__":
    asyncio.run(main())
