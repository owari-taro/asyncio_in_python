import time
import asyncio
from current.futures import ThreadPoolExecutor as Executor


def blocking():
    time.sleep(2.0)
    print(f"{time.ctime()} hello from a thread!")


async def main():
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, blocking)
    try:
        print(f"{time.ctime()} hello!")
        await asyncio.sleep(1.0)
        print(f"{time.ctime()} goodbye!")
    finally:
        await future

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bye!")
