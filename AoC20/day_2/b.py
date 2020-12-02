from AoC20.day_2 import Rule, data


print(sum([Rule(line).check_2() for line in data.splitlines()]))
