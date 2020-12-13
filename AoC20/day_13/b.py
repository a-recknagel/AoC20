from AoC20.day_13 import data as data


def solve(busses):
    offset = 0
    earliest = step = busses[0]
    for bus in busses[1:]:
        offset += 1
        if bus is None:
            continue
        while True:
            if (earliest + offset) % bus == 0:
                step *= bus
                break
            earliest += step
    return earliest


data = [int(elem) if elem != "x" else None for elem in data[1].split(',')]
print(solve(data))
