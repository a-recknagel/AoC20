from AoC20.day_12 import data as data, solve


print(solve([(row[0], int(row[1:])) for row in data], 0+1j, move="boat"))
