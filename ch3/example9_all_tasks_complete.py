import asyncio

# p@
# ;


async def f(delay):
    await asyncio.sleep(1/delay)
    return delay

loop = asyncio.get_event_loop()
for i in range(10):
    loop.create_task(f(i))
pending = asyncio.all_tasks(loop=loop)
print(type(pending))  # execute pending tasks
# with return_exceptions=True,exception is returns as a value
group = asyncio.gather(*pending, return_exceptions=True)
results = loop.run_until_complete(group)
print(f"{results=}")
loop.close()
