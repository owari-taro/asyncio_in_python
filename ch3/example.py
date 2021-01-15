async def f():
    return 123

coro=f()
try:
    coro.send(None)
except StopIteration as e:
    print(f"the answer was:{e.value}")