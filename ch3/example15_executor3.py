import time
import asyncio
from concurrent.futures import ThreadPoolExecutor as Executor


async def make_coro(future):
    try:
        return await future
    except asyncio.CancelledError:
        return await future


async def main():
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, blocking)
    # wrap the future produced by executer inside a new task object
    asyncio.create_task(make_coro(future))
    print(f"{time.ctime()} hello")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} good bye")


def blocking():
    time.sleep(2.0)
    print(f"{time.ctime()} helo from a thread")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bye!")
