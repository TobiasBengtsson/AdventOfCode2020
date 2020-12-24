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
        if step == 'e':
            col += 2
        elif step == 'w':
            col -= 2
        elif step == 'ne':
            row += 1
            col += 1
        elif step == 'nw':
            row += 1
            col -= 1
        elif step == 'se':
            row -= 1
            col += 1
        elif step == 'sw':
            row -= 1
            col -= 1
    
    if (row, col) not in grid:
        grid[(row, col)] = 'W'
    
    if grid[(row, col)] == 'W':
        grid[(row, col)] = 'B'
    else:
        grid[(row, col)] = 'W'

def get_color(coord, grid):
    if coord not in grid:
        return 'W'
    return grid[coord]

def get_adj(coord):
    (row, col) = coord
    yield (row, col + 2)
    yield (row, col - 2)
    yield (row + 1, col + 1)
    yield (row + 1, col - 1)
    yield (row - 1, col + 1)
    yield (row - 1, col - 1)

for i in range(100):

    tiles_to_consider = set()
    for tile in grid:
        tiles_to_consider.add(tile)
        for adj in get_adj(tile):
            tiles_to_consider.add(adj)

    new_grid = grid.copy()
    for tile in tiles_to_consider:
        adj_blacks = 0
        for adj in get_adj(tile):
            if get_color(adj, grid) == 'B':
                adj_blacks += 1

        if get_color(tile, grid) == 'B' and adj_blacks == 0 or adj_blacks > 2:
            new_grid[tile] = 'W'
        elif get_color(tile, grid) == 'W' and adj_blacks == 2:
            new_grid[tile] = 'B'

    grid = new_grid

count = 0
for tile in grid:
    if grid[tile] == 'B':
        count += 1

print(count)
