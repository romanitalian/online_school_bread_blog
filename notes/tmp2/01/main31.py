import asyncio
from time import time


async def foo(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    st = time()

    await foo(1, '11111')
    await foo(2, '2222')

    print(f'time execute: {time() - st}')


if __name__ == '__main__':
    asyncio.run(main())
