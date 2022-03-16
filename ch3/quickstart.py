import asyncio,time

async def main():
    print(f"{time.ctime()} hello!")
    await asyncio.sleep(2.0)
    print(f"{time.ctime()} good bye!")

asyncio.run(main())