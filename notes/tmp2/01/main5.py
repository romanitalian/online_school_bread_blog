from time import time, sleep
import requests
import concurrent.futures

from faker import Faker

from main.models import Author


def foo(address, timeout=10):
    print(address)
    res = requests.get(url=address, timeout=timeout).status_code
    sleep(3)
    faker = Faker()
    Author(name=faker.name(), email=faker.email()).save()

    return res


def run():
    urls = [f"https://www.google.com/search?q=1usd+to+{str(i)}+euro" for i in range(10)]

    start = time()
    # max_workers - max threads count
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as ex:
        res = []
        for url in urls:
            res.append(ex.submit(foo, address=url))
        for r in concurrent.futures.as_completed(res):
            print(f"res: {r.result()}")

        for res in ex.map(foo, urls, timeout=20, chunksize=2):
            print(f"result: {res}")

    # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    #     result = executor.map(foo, range(10))
    #     print(result)

    print(f'Time: {time() - start}')


if __name__ == '__main__':
    run()
