import sys

passports = []
req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for l in sys.stdin:
    l = l.rstrip('\n')
    spl = l.split()
    passport = {}
    for field in spl:
        f_spl = field.split(':')
        passport[f_spl[0]] = f_spl[1]
    passports.append(passport)

answer = 0
for p in passports:
    valid = True
    for req_field in req_fields:
        if req_field not in p.keys():
            valid = False
    if valid:
        answer += 1

print(answer)
