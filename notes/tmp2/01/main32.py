import asyncio
import aiohttp
import os


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        with open("file", 'wb') as f:
            f.write(data)
        return data


async def main():
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(100):
            task = asyncio.create_task(fetch_content(f"https://www.google.com/search?q={i}", session))
            tasks.append(task)

        # доздаться результата всех (gather - это генератор)
        return await asyncio.gather(*tasks)


asyncio.run(main())
