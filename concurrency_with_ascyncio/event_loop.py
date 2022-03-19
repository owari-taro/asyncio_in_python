import asyncio


async def coroutnine_add_one(num: int) -> int:
    return num+1

result=asyncio.run(coroutnine_add_one(1))
print(result)