from AoC20.day_3 import trees, data as data


data = [line.strip() for line in data.splitlines()]
print(
    sum(trees(data, (1, 1))) *
    sum(trees(data, (1, 3))) *
    sum(trees(data, (1, 5))) *
    sum(trees(data, (1, 7))) *
    sum(trees(data, (2, 1)))
)
