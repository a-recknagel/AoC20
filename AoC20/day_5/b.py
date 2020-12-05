from AoC20.day_5 import parse, data as data


def empty_seat(seats):
    seats = set(seats)
    all_seats = set(range(min(seats), max(seats)))
    return (all_seats - seats).pop()


print(empty_seat(parse(data)))
