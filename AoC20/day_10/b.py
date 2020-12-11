from AoC20.day_10 import example_data_b as data


def weird_fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 4
    return weird_fib(n-1) + weird_fib(n-2) + weird_fib(n-3)


def edge_distances(inp):
    for a, b in zip(inp, inp[1:]):
        yield b-a


def group_singles(distances):
    ...


data = sorted(map(int, data))
data = [0, *data, data[-1]+3]
