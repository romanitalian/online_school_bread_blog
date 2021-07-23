import django
import requests
from time import time, sleep
import concurrent.futures
from multiprocessing import cpu_count, Pool
from django.core.management.base import BaseCommand

from main.models import Author


def do(val):
    return val


def foo(address, timeout=10):
    print(address)
    res = requests.get(url=address, timeout=timeout).status_code

    cnt = Author.objects.count()
    print(f"authors count: {cnt}")

    return res


def subprocess_setup():
    django.setup()
    print(12312313)
    # Could do other things here


def run(val):
    urls = [f"https://www.google.com/search?q=1usd+to+{str(i)}+euro" for i in range(1)]

    with concurrent.futures.ProcessPoolExecutor(max_workers=2, initializer=subprocess_setup) as ex:
        res = []
        for url in urls:
            res.append(ex.submit(foo, address=url))
        for r in concurrent.futures.as_completed(res):
            print(f"res: {r.result()}")

        for res in ex.map(foo, urls, timeout=20, chunksize=2):
            print(f"result: {res}")
    return val


class Command(BaseCommand):
    help = 'generate some Authors in multiprocessing'  # noqa

    def handle(self, *args, **options):
        run(1)
