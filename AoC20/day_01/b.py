from AoC20.day_1 import data


def solve(inp):
    for i in range(len(inp)):
        for j in range(len(inp)):
            if i == j:
                continue
            for k in range(len(inp)):
                if i == k or j == k:
                    continue
                if inp[i] + inp[j] + inp[k] == 2020:
                    return inp[i]*inp[j]*inp[k]
    return "No solution found =("


print(solve([*map(int, data.split("\n"))]))


