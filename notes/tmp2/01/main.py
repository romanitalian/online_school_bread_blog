from time import sleep, time


def foo():
    print("START")
    sleep(10)
    print("FINISH")


start = time()
foo()
# foo()

print(f'Time: {time() - start}')
