from AoC20.day_17 import data as data, solve, get_active_states


active_states = get_active_states(data, 3)
print(solve(active_states, 6))
