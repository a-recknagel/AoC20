from itertools import product


def get_neighbors(pos):
    factors = [[dim-1, dim, dim+1] for dim in pos]
    neighbors = set(product(*factors))
    neighbors.remove(pos)

    return neighbors


def solve(active, rounds):
    for i in range(rounds):
        new = set()
        for state in active:
            neighbors = get_neighbors(state)
            if len(neighbors & active) in [2, 3]:
                new.add(state)

            for neighbor in neighbors - active:
                if len(get_neighbors(neighbor) & active) == 3:
                    new.add(neighbor)
        active = new
    return len(active)


def get_active_states(inp, dim):
    active_states = set()
    for x, rows in enumerate(inp):
        for y, elem in enumerate(rows):
            if elem == "#":
                active_states.add((x, y, *([0] * (dim - 2))))

    return active_states


example_data = """\
.#.
..#
###\
""".splitlines(keepends=False)

data = """\
.###..#.
##.##...
....#.#.
#..#.###
...#...#
##.#...#
#..##.##
#.......\
""".splitlines(keepends=False)
