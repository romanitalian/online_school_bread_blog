import asyncio


async def main():
    print('1111')
    await asyncio.sleep(1)
    print('2222')

if __name__ == '__main__':
    asyncio.run(main())
