import time
import asyncio


def blocking():
    time.sleep(10)
    print(f"{time.ctime()} hello from a thread!")


async def main():
    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, blocking)
    print("########################################\n", type(tmp))
    print(f"{time.ctime()} hello")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} good bye")

if __name__ == "__main__":
    asyncio.run(main())
