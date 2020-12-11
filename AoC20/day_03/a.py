from AoC20.day_3 import trees, data as data


print(sum(trees([line.strip() for line in data.splitlines()], (1, 3))))
