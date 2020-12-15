import sys

n_strs = sys.stdin.readline().rstrip('\n').split(',')
ns = [int(n) for n in n_strs]

def series():
    i = 0
    last_seen = {}
    while True:
        if i < len(ns):
            yield ns[i]
        else:
            prev = ns[i - 1]
            if prev in last_seen:
                diff = i - last_seen[prev] - 1
                ns.append(diff)
            else:
                ns.append(0)

            yield ns[i]

        if i > 0:
            last_seen[ns[i-1]] = i-1
        i += 1

for i, s in enumerate(series()):
    if i == 30000000 - 1:
        print(s)
        break
