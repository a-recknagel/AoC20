from typing import Dict, Iterable

from AoC20.day_7 import Bag, parse, data as data


def count_children(bag: str, bags: Dict[str, Bag]) -> Iterable[int]:
    yield 1
    for child, cost in bags[bag].children.items():
        for _ in range(cost):
            yield from count_children(child.name, bags)


print(sum(count_children("shiny gold", parse(data))) - 1)
