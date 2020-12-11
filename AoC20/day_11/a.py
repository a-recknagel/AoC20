from AoC20.day_11 import data as data, solve, adjacent_seats

print(solve([[*row] for row in data], adjacent_seats, 4))
