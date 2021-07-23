from time import time


def log(*args):
    print(f'log: {args}')


def log2(*args):
    print(time())
    print(f'log_2: {args}')


def foo(a, b, callback=None):
    res = a + b + 101
    if callback is not None:
        callback(a, b)

    return res


val = foo(11, 22)
print(f'00001 - {val}\n')

val = foo(10, 20, log)
print(f'00002 - {val}\n')

val = foo(10, 20, log2)
print(f'00003 - {val}\n')


val = foo(10, 20, lambda *args: print(f'lambda log: {args}'))
print(f'00004 - {val}\n')
