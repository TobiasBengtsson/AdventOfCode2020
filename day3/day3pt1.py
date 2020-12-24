import sys

ls = []
for l in sys.stdin:
    l = l.rstrip('\n')
    ls.append(l)

c = 0
rc = 0
for g in range(len(ls)):
    if (ls[g][rc % len(ls[g])]) == '#':
        c += 1
    rc += 3

print(c)
