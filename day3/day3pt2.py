import sys

ls = []
for l in sys.stdin:
    l = l.rstrip('\n')
    ls.append(l)

c = 0
rc = 0
for g in range(0,len(ls),2):
    if (ls[g][rc % len(ls[g])]) == '#':
        c += 1
    rc += 1

print(c)
