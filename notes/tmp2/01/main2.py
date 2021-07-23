from time import sleep, time
from threading import Thread


def foo():
    print("START")
    sleep(10)
    print("FINISH")


start = time()
th1 = Thread(target=foo)
th2 = Thread(target=foo)

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Time: {time() - start}')
# Завершится основной Поток программы,
# а потом Треды
#
# START
# START
# Time: 0.0002651214599609375
# FINISH
# FINISH

# th1.join()
# th2.join()
#
# START
# START
# FINISH
# FINISH
# Time: 10.005265235900879
