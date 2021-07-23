from time import sleep, time
from threading import Thread, current_thread
from multiprocessing.pool import ThreadPool


def foo(val):
    print(f"START val: {val} thread: {current_thread()}")
    sleep(10)
    print("FINISH")


start = time()

total = 4
proc_count = 3
chunk_size = 2

pool = ThreadPool(proc_count)
pool.map(foo, range(total), chunk_size)

print(f'Time: {time() - start}')

