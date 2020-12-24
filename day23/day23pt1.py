import sys

labels = [4, 6, 3, 5, 2, 8, 1, 7, 9]

def rotate(l):
    fst = l[0]
    l = l[1:]
    l.append(fst)
    return l

current_i = 0
for i in range(100):
    label = labels[current_i]
    picked = []
    pick_i = (current_i + 1) % len(labels)

    for j in range(3):
        if pick_i >= len(labels):
            pick_i = 0
        picked.insert(0, labels[pick_i])
        del labels[pick_i]

    min_val = min(labels)
    target = label - 1
    if target < min_val:
        target = max(labels)

    found = False
    while not found:
        try:
            target_i = labels.index(target)
            found = True
        except Exception:
            target -= 1
    
    for j in picked:
        labels.insert(target_i + 1, j)

    while labels.index(label) != current_i:
        labels = rotate(labels)

    current_i = (current_i + 1) % len(labels)

while labels[0] != 1:
    labels = rotate(labels)

s = ''
for label in labels[1:]:
    s += str(label)

print(s)
