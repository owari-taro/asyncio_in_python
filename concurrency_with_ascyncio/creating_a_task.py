import asyncio
from util  import delay
import time
async def main():
    result=await delay(4)
    ##sleep_for_three=asyncio.create_task(delay(4))
    ##print(type(sleep_for_three))
    ##print("hogehoge")
    #result=await sleep_for_three
    print(result)

if __name__=="__main__":
    asyncio.run(main())