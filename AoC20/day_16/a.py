from AoC20.day_16 import data as data, parse


rules, _, tickets = parse(data)
print(sum(invalid for ticket in tickets if (invalid := rules.ticket_violation(ticket)) is not None))
