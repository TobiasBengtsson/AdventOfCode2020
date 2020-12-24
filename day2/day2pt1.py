import sys

g_count = 0

for line in sys.stdin:
    line = line.rstrip('\n')
    split = line.split(' ')
    min = int(split[0].split('-')[0])
    max = int(split[0].split('-')[1])
    letter = split[1].rstrip(':')
    
    passw = split[2]
    count = 0
    for c in passw:
        if c == letter:
            count += 1
    
    if count <= max and count >= min:
        g_count += 1

print(g_count)
