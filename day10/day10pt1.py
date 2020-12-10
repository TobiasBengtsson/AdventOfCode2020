import sys

ns = []
for line in sys.stdin:
    line = line.rstrip('\n')
    ns.append(int(line))

ns = sorted(ns)
ns.append(ns[-1] + 3)
jolt_diffs = {}
prev = 0
for n in ns:
    if n not in jolt_diffs:
        jolt_diffs[n] = 0
    jolt_diffs[n - prev] += 1
    prev = n

print(jolt_diffs[1] * jolt_diffs[3])
