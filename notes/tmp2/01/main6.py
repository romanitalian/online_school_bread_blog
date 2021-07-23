import time
from threading import Thread

COUNT = 150_000_000


def cpu_bound_calc(n):
    while n > 0:
        n -= 1


start = time.time()

# Без тредов
# cpu_bound_calc(COUNT)
# end = time.time()
# print('Exec time without threads:', end - start)

t1 = Thread(target=cpu_bound_calc, args=(COUNT // 2,))
t2 = Thread(target=cpu_bound_calc, args=(COUNT // 2,))

t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Exec time with threads:', end - start)
