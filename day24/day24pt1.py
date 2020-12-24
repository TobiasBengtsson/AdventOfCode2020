import sys

all_directions = []
for line in sys.stdin:
    line = line.rstrip('\n')
    directions = []
    i = 0
    while i < len(line):
        if i + 1 == len(line):
            directions.append(line[i])
            break
        if line[i] in ('s','n') and line[i + 1] in ('w', 'e'):
            directions.append(line[i:i+2])
            i += 2
            continue
        directions.append(line[i])
        i += 1
    all_directions.append(directions)

grid = {}
for directions in all_directions:
    row = 0
    col = 0
    for step in directions:
        if step == 'n':
            row += 2
        elif step == 's':
            row -= 2
        elif step == 'w':
            col -= 2
        elif step == 'e':
            col += 2
        elif step == 'nw':
            row += 1
            col -= 1
        elif step == 'ne':
            row += 1
            col += 1
        elif step == 'sw':
            row -= 1
            col -= 1
        elif step == 'se':
            row -= 1
            col += 1
    
    if (row, col) not in grid:
        grid[(row, col)] = 'W'
    
    if grid[(row, col)] == 'W':
        grid[(row, col)] = 'B'
    else:
        grid[(row, col)] = 'W'

count = 0
for tile in grid:
    if grid[tile] == 'B':
        count += 1

print(count)
