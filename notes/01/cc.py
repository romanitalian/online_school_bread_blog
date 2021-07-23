from time import sleep

CACHE = {}


def foo(a, b, c):
    key = f'foo{a}_{b}_{c}'
    if key in CACHE:
        print("in cache")
        return CACHE[key]

    print("------ not in cache")
    sleep(2)
    res = (a + b + c) ** 2
    CACHE[key] = res

    return res


def bar(a, b, c):
    key = f'bar{a}_{b}_{c}'
    if key in CACHE:
        print("in cache")
        return CACHE[key]

    print("------ not in cache")
    sleep(2)
    res = (a * b * c) ** 2
    CACHE[key] = res

    return res



print(foo(1, 2, 10))
print(foo(1, 2, 10))

print(bar(1, 2, 10))
print(bar(1, 2, 10))
