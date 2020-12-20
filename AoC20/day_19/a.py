from AoC20.day_19 import data as data, solve, parse_rules


rule_inp, content = data.split("\n\n")
rules = parse_rules(rule_inp)

print(sum(solve(content, rules)))
