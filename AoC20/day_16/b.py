from AoC20.day_16 import data as data, parse


rules, my_ticket, other_tickets = parse(data)
other_tickets = [ticket for ticket in other_tickets if rules.ticket_violation(ticket) is None]
fields = rules.field_deduction(other_tickets)
print()
print()
