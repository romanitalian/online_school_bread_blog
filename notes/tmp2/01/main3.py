from time import sleep, time
from threading import Thread, current_thread


def foo():
    print(f"START thread: {current_thread()}")
    sleep(10)
    print("FINISH")


def foo2(val):
    print(f"START val: {val} thread: {current_thread()}")
    sleep(10)
    print(f"FINISH {current_thread()}")


start = time()

ths = []  # список тредов

# for _ in range(5):
#     th = Thread(target=foo)
#     th.start()
#     ths.append(th)

for i in range(5):
    # th = Thread(target=foo, args=[i, ])  # foo2(i)
    th = Thread(target=foo2, kwargs={'val': i})  # foo2(val=i)
    th.start()
    ths.append(th)

for th in ths:
    th.join()

print(f'Time: {time() - start}')
