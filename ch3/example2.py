import asyncio


async def f():
    try:
        while True:
            print("asyncio sleep")
            await asyncio.sleep(0)
    except asyncio.CancelledError:
        print("I was cancelled")

    else:
        return 111


coro = f()
coro.send(None)
coro.send(None)
try:
    coro.throw(asyncio.CancelledError)
except StopIteration as e:
    print("the ans was", e.value)

# educational ppurpose courutine,dont do this"\!


async def f():
    try:
        while True:
            print("asyncio sleep")
            await asyncio.sleep(0)
    except asyncio.CancelledError:
        print("nope")
        while True:
            print("inside exception")
            await asyncio.sleep(0)
    else:
        return 111

coro = f()
coro.send(None)
coro.throw(asyncio.CancelledError)
coro.send(None)
