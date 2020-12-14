from AoC20.day_14 import data as data


mem = {}
for line in data:
    if line.startswith("mask "):
        line = line[:7] + '"' + line[7:] + '"'
    else:
        line = line[:line.index("=")+2] + "int(''.join([v if m == 'X' else m for v, m in zip(f'{" + line[line.index("=")+2:] + ":036b}', mask)]), 2)"
    exec(line)
print(sum(mem.values()))
