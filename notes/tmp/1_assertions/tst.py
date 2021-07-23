def add(x, y):
    return x + y


def div(x, y):
    assert y != 0, "you can nod divide by zero. Fix it!"
    return x / y


def avg(rates):
    assert len(rates) != 0
    return sum(rates) / len(rates)


assert add(1, 2) == 3
assert add(2, 2) == 4
assert add(2, 3) == 5

assert add(0, 0) == 0
assert add(2, -2) == 0
assert add(-12, -20) == -32
assert add(-12.1, -1) == -13.1

if __name__ == '__main__':
    div(7, 2)
    div(7, 0)

    avg([2, 3, 15, 4, 7])
    avg([])
