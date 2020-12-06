import sys

# Pre-processing of input:
# 1) Search and replace '\n' with ','
# 2) Search and replace ',,' with ';'
# 3) Remove the very last ','

ls = []
l = sys.stdin.readline()
groups = l.split(';')

g_dicts = []
ind_counts = []
for group in groups:
    letters = {}
    individuals = group.split(',')
    for individual in individuals:
        for c in individual:
            if not letters.get(c):
                letters[c] = 0
            letters[c] += 1
    ind_counts.append(len(individuals))
    g_dicts.append(letters)

answer = 0
for ic, d in zip(ind_counts, g_dicts):
    for val in d.values():
        if val == ic:
            answer += 1

print(answer)
