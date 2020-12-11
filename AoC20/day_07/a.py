from typing import Dict, Iterable, Set

from AoC20.day_7 import Bag, parse, data as data


def count_parents(bag: str, bags: Dict[str, Bag]) -> Iterable[Set[Bag]]:
    yield (parents := bags[bag].parents)
    for parent in parents:
        yield from count_parents(parent.name, bags)


print(len(set.union(*count_parents("shiny gold", parse(data)))))
