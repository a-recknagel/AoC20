from functools import reduce, lru_cache

from AoC20.day_10 import data as data


@lru_cache(maxsize=None)
def weird_fib(n):
    if n == 0:
        return 1  # makes sense?
    if n == 1:
        return 1
    if n == 2:
        return 2
    return weird_fib(n-1) + weird_fib(n-2) + weird_fib(n-3)


def group_singles(inp):
    group_size = 0
    for distance in (b-a for a, b in zip(inp, inp[1:])):
        if distance == 3:
            yield group_size
            group_size = 0
        if distance == 1:
            group_size += 1


data = sorted(map(int, data))
data = [0, *data, data[-1]+3]

print(reduce(int.__mul__, map(weird_fib, group_singles(data))))
