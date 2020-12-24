import sys

def validate_int_range(str, min, max):
    try:
        val = int(str)
        return val >= min and val <= max
    except ValueError:
        return False

def vaildate_passport(p):
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for req_field in req_fields:
        if req_field not in p.keys():
            return False
    if not validate_int_range(p['byr'], 1920, 2002):
        return False
    if not validate_int_range(p['iyr'], 2010, 2020):
        return False
    if not validate_int_range(p['eyr'], 2020, 2030):
        return False
    height_unit = p['hgt'][-2:]
    if not height_unit in ('cm', 'in'):
        return False
    if height_unit == 'cm' and not validate_int_range(p['hgt'][:-2], 150, 193):
        return False
    if height_unit == 'in' and not validate_int_range(p['hgt'][:-2], 59, 76):
        return False
    if p['hcl'][0] != '#':
        return False
    if len(p['hcl'][1:]) != 6:
        return False
    for digit in p['hcl'][1:]:
        if digit not in ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'):
            return False
    if p['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return False
    if len(p['pid']) != 9:
        return False
    for digit in p['pid']:
        if digit not in ('0','1','2','3','4','5','6','7','8','9'):
            return False
    return True

passports = []

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
    if vaildate_passport(p):
        answer += 1

print(answer)
