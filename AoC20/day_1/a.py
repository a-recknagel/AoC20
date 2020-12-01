from AoC20.day_1 import data


def solve(inp):
    for i in range(len(inp)):
        for j in range(len(inp)):
            if i == j:
                continue
            if inp[i] + inp[j] == 2020:
                return inp[i]*inp[j]
    return "No solution found =("


print(solve([*map(int, data.split("\n"))]))

