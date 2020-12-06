from AoC20.day_6 import solve, data as data


inp = [line.splitlines() for line in data.split("\n\n")]
print(sum(solve(inp, set.union)))
