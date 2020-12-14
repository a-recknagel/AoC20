from itertools import product

from AoC20.day_14 import data as data, PCS


def solve(pcs: PCS):
    mem = {}
    trans = {
        "0": lambda x: x,
        "1": lambda x: "1",
        "X": lambda x: "{}",
    }
    for mask, instructions in pcs.blocks():
        for address, value in instructions:
            address_base = "".join([
                trans[m](a) for
                a, m in
                zip(address, mask)
            ])
            for perm in product("01", repeat=mask.count("X")):
                mem[int(address_base.format(*perm), 2)] = value

    return sum(mem.values())


print(solve(PCS(data)))
