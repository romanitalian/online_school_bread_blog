from datetime import datetime


def counter_decorator(func):
    cnt = 0

    def wrapper():
        nonlocal cnt
        cnt += 1
        print(cnt)

        res = func()
        return res

    return wrapper


@counter_decorator
def foo():
    print(datetime.now())


foo()
foo()
foo()
