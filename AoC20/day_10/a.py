from AoC20.day_10 import data as data


def diff_counter(inp):
    diff_1 = diff_3 = 0
    for i in range(1, len(inp)):
        diff = inp[i] - inp[i-1]
        diff_1 += diff == 1
        diff_3 += diff == 3
    return diff_1 * diff_3


data = sorted(map(int, data))
data = [0, *data, data[-1]+3]
print(diff_counter(data))
