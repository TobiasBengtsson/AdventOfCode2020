import sys

inp = [4, 6, 3, 5, 2, 8, 1, 7, 9]
nexts = [0] * 1000001

for i, label in enumerate(inp[:-1]):
    nexts[label] = inp[i + 1]

nexts[9] = 10

for i in range(10, 1000001):
    nexts[i] = i + 1

nexts[-1] = inp[0]

current_label = inp[0]
for i in range(10000000):

    next1 = nexts[current_label]
    next2 = nexts[next1]
    next3 = nexts[next2]
    next4 = nexts[next3]
    
    nexts[current_label] = next4

    target = current_label - 1
    if target < 1:
        target = 1000000
    while target in (next1, next2, next3):
        target -= 1
        if target < 1:
            target = 1000000

    nexts[next3] = nexts[target]
    nexts[target] = next1

    current_label = next4

print(nexts[1] * nexts[nexts[1]])
