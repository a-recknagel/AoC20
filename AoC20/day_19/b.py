from AoC20.day_19 import example_data_c as data, solve, parse_rules


rule_inp, content = data.split("\n\n")
rules = parse_rules(rule_inp)
# rules[8] = [[42], [42, 8]]
# rules[11] = [[42, 31], [42, 11, 31]]

print(sum(solve(content, rules)))
