import sys

n_strs = sys.stdin.readline().rstrip('\n').split(',')
ns = [int(n) for n in n_strs]

def series():
    i = 0
    while True:
        if i < len(ns):
            yield ns[i]
        else:
            prev = ns[i-1]
            try:
                diff = ns[i-2::-1].index(prev) + 1
                ns.append(diff)
            except:
                ns.append(0)
            yield ns[i]
        i += 1

for i, s in enumerate(series()):
    if i == 2020 - 1:
        print(s)
        break
