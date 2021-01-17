import time
import asyncio
from concurrent.futures import ThreadPoolExecutor as Executor


async def main():
    print(f"{time.ctime()} hello!")
    await async.sleep(1.0)
    print(f"{time.ctime()} closed")
    loop.stop()


def blocking():
    time.sleep(2.0)
    print(f"{time.ctime()} hello from a thread!")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    executor = Executor()
    loop.set_default_executor(executor)
    loop.create_task(main())
    future = loop.run_in_executor(None, blocking)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print("cancelled")
    tasks = asyncio.all_tasks(loop=loop)
    for t in tansks:
        t, cancel()
    group = asyncio.gather(*tasks, return_exceptions=True)
    loop.run_until_complete(group)
    executor.shutdown(wait=True)
    loop.close()
