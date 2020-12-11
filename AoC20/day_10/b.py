from functools import reduce, lru_cache

from AoC20.day_10 import example_data_b as data


@lru_cache(maxsize=None)
def weird_fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4
    return weird_fib(n-1) + weird_fib(n-2) + weird_fib(n-3)


def group_singles(inp):
    edge_distances = (b-a for a, b in zip(inp, inp[1:]))
    current = 0
    while foo := next(edge_distances, False):
        if foo == 3:
            if current:
                yield current
                current = 0
        if foo == 1:
            current += 1


data = sorted(map(int, data))
data = [0, *data, data[-1]+3]

print(reduce(int.__mul__, group_singles(data)))
