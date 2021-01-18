import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://python.org")as response:
            print("stratus:", response.status)
            print("content-type:", response.headers["content-type"])
            html = await response.text()
            print("body,", html[:15], "...")
            print(html)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    #asyncio.run(main())
    #loop.close()