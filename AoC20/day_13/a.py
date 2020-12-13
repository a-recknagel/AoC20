from AoC20.day_13 import data as data


def solve(start, busses):
    best = 0
    earliest = float("inf")
    for bus in busses:
        if bus is None:
            continue

        departure = bus
        while True:
            if departure >= start:
                if departure < earliest:
                    best = bus
                    earliest = departure
                break
            departure += bus

    return (earliest - start) * best


data = int(data[0]), [int(elem) if elem != "x" else None for elem in data[1].split(',')]
print(solve(*data))
