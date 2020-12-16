import sys

int_meanings = {}
section = 0
valid_tickets = []
my_ticket = []
for line in sys.stdin:
    line = line.rstrip('\n')
    if not line:
        section += 1
        continue
    if section == 0:
        text, ranges = line.split(':')
        ranges = ranges.split(' or ')
        for rng in ranges:
            rng = rng.strip()
            start, end = rng.split('-')
            start = int(start)
            end = int(end)
            for i in range(start, end + 1):
                if i not in int_meanings:
                    int_meanings[i] = set()
                int_meanings[i].add(text)
    
    elif section == 1 and line != 'your ticket:':
        codes = [int(i) for i in line.split(',')]
        my_ticket = codes
    elif section == 2 and line != 'nearby tickets:':
        codes = [int(i) for i in line.split(',')]
        valid = True
        for code in codes:
            if code not in int_meanings:
                valid = False
                break
        if valid:
            valid_tickets.append(codes)

possible_i_meanings = {}
for i in range(len(my_ticket)):
    for j, ticket in enumerate(valid_tickets):
        code = ticket[i]
        if i not in possible_i_meanings:
            possible_i_meanings[i] = int_meanings[code]
        else:
            possible_i_meanings[i] = possible_i_meanings[i] & int_meanings[code]

# A bit of a shortcut by introspecting possible_i_meanings at this point.
# Exactly one i has only one possible meaning.
# If this meaning is removed from all other possible_i_meanings, there
# will be yet again another i with one possible meaning left and so on.
any_left = True
while any_left:
    any_left = False
    for i in possible_i_meanings:
        m = possible_i_meanings[i]
        if len(m) == 1:
            for j in possible_i_meanings:
                if i == j:
                    continue
                for single_m in m:
                    if single_m in possible_i_meanings[j]:
                        possible_i_meanings[j].remove(single_m)
        else:
            any_left = True

answer = 1
for i in possible_i_meanings:
    for single_m in possible_i_meanings[i]:
        if single_m.startswith('departure'):
            answer *= my_ticket[i]

print(answer)
