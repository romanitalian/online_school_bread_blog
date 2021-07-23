import time
from multiprocessing import Process

COUNT = 150_000_000


def cpu_bound_calc(n):
    while n > 0:
        n -= 1


def run():
    start = time.time()

    # Без тредов
    # cpu_bound_calc(COUNT)
    # end = time.time()
    # print('Exec time without threads:', end - start)

    t1 = Process(target=cpu_bound_calc, args=(COUNT // 2,))
    t2 = Process(target=cpu_bound_calc, args=(COUNT // 2,))
    # t3 = Process(target=cpu_bound_calc, args=(COUNT // 4,))
    # t4 = Process(target=cpu_bound_calc, args=(COUNT // 4,))

    t1.start()
    t2.start()
    # t3.start()
    # t4.start()

    t1.join()
    t2.join()
    # t3.join()
    # t4.join()

    end = time.time()

    print('Exec time with threads:', end - start)


if __name__ == '__main__':
    run()
