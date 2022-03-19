import asyncio
from email.message import EmailMessage
from util import delay


async def add_one(num: int) -> int:
    return num+1


async def hello_world_message() -> str:
    await delay(1)
    return "hell world"


async def main() -> None:
    message = await hello_world_message()
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)

if __name__ == "__main__":
    asyncio.run(main())
