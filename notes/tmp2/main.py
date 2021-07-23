from time import sleep, time
from threading import Thread, current_thread
from multiprocessing import Process
import concurrent.futures
import requests

import asyncio


async def foo(msg):
    await asyncio.sleep(2)
    print(msg)

async def main():
    print("START 11111111")
    await asyncio.sleep(3)
    await foo("hello")
    await foo("world")
    print("FINISH 222222")


if __name__ == '__main__':
    asyncio.run(main())
