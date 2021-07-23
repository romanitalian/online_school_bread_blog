import asyncio


@asyncio.coroutine
def foo():
    n = 1
    while True:
        print(n)
        n += 1
        yield from asyncio.sleep(1)


@asyncio.coroutine
def bar():
    count = 0
    while True:
        if count % 10 == 0:
            print(f"count: {count}")
        count += 1
        yield from asyncio.sleep(1)


@asyncio.coroutine
def main():
    task1 = asyncio.ensure_future(foo())
    task2 = asyncio.ensure_future(bar())
    yield from asyncio.gather(task1, task2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
