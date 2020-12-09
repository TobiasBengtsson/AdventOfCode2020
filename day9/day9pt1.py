import sys

preamble = []
ls = []
for i, line in enumerate(sys.stdin):
    line = line.rstrip('\n')
    n = int(line)
    if i < 25:
        preamble.append(n)
    else:
        ls.append(n)

for l in ls:
    preamble_s = sorted(preamble)
    i = 0
    j = len(preamble_s) - 1
    found = False
    while j > i:
        sum = preamble_s[i] + preamble_s[j]
        if l == sum or l == preamble_s[i] or l == preamble_s[j]:
            found = True
            break
        elif l < sum:
            j -= 1
        else:
            i += 1
    if not found:
        print(l)

    preamble = preamble[1:]
    preamble.append(l)
