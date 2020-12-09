import sys

ls = []
for i, line in enumerate(sys.stdin):
    line = line.rstrip('\n')
    n = int(line)
    if i < 25:
        pass
    else:
        ls.append(n)

target = 177777905

for i, l in enumerate(ls):
    sum = 0
    j = i + 1
    if not j < len(ls):
        break
    sum = l + ls[j]
    while sum < target and j < len(ls):
        j += 1
        sum += ls[j]
    if sum == target:
        range = sorted(ls[i:j])
        print (min(range) + max(range))
        break
