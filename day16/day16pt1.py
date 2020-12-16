import sys

int_meanings = {}
section = 0
ticket_error_rate = 0
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
                    int_meanings[i] = []
                int_meanings[i].append(text)
    
    elif section == 1:
        pass
    elif section == 2 and line != 'nearby tickets:':
        codes = line.split(',')
        valid = True
        for code in codes:
            intcode = int(code)
            if intcode not in int_meanings:
                valid = False
                ticket_error_rate += intcode

print(ticket_error_rate)
