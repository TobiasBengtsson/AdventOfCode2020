import sys

ns = []
for line in sys.stdin:
    line = line.rstrip('\n')
    ns.append(int(line))

ns = sorted(ns)
ns.append(ns[-1] + 3)
ns.insert(0, 0)

def get_possible_successors(i):
    j = i + 1
    while j < len(ns) and ns[j] - ns[i] <= 3:
        yield j
        j += 1

possible_paths_to_index = {}
for i, n in enumerate(ns):
    if i == 0:
        possible_paths_to_index[0] = 1
    for succ in get_possible_successors(i):
        if succ not in possible_paths_to_index:
            possible_paths_to_index[succ] = 0
        possible_paths_to_index[succ] += possible_paths_to_index[i]

print(possible_paths_to_index[len(ns) - 1])
