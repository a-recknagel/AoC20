import re

from AoC20.day_18 import data as data


class Int:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return Int(self.val + other.val)

    def __sub__(self, other):
        return Int(self.val * other.val)

    def __repr__(self):
        return str(self.val)


def solve(inp):
    solutions = []
    for line in inp:
        # replace * with -, so that the precedence is now equal
        line = line.replace("*", "-")
        # turn all ints (e.g. 3, 5, 8) into fake ints (e.g. Int(3), Int(5), Int(8))
        line = re.sub(r"(\d)", r"Int(\1)", line)
        solutions.append(int(str(eval(line))))
    return sum(solutions)


print(solve(data))
