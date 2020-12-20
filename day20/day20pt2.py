import sys

class Tile:
    def __init__(self, id, rows):
        self.id = id
        self.rows = rows

    def top_side(self):
        return tuple(self.rows[0])

    def rev_top_side(self):
        return tuple(self.rows[0][::-1])

    def bottom_side(self):
        return tuple(self.rows[-1])

    def rev_bottom_side(self):
        return tuple(self.rows[-1][::-1])
    
    def left_side(self):
        col = []
        for row in self.rows:
            col.append(row[0])

        return tuple(col)

    def rev_left_side(self):
        col = []
        for row in self.rows:
            col.append(row[0])

        col.reverse()
        return tuple(col)

    def right_side(self):
        col = []
        for row in self.rows:
            col.append(row[-1])

        return tuple(col)

    def rev_right_side(self):
        col = []
        for row in self.rows:
            col.append(row[-1])

        col.reverse()
        return tuple(col)

    def get_edges(self):
        ret = []
        ret.append(self.top_side())
        ret.append(self.rev_top_side())
        ret.append(self.bottom_side())
        ret.append(self.rev_bottom_side())
        ret.append(self.left_side())
        ret.append(self.rev_left_side())
        ret.append(self.right_side())
        ret.append(self.rev_right_side())
        return ret

    def flip_vert(self):
        return Tile(self.id, self.rows[::-1])

    def flip_horiz(self):
        rows = []
        for row in self.rows:
            rows.append(row[::-1])
        return Tile(self.id, rows)

    def rotate(self):
        new_rows = []
        for i in range(len(self.rows)):
            new_row = []
            for j in range(len(self.rows)):
                new_row.append(0)
            new_rows.append(new_row)

        for i, row in enumerate(self.rows):
            for j, col in enumerate(row):
                new_rows[j][len(self.rows) - i - 1] = col

        return Tile(self.id, new_rows)

    def get_all_transforms(self):
        tile = self
        for _ in range(2):
            for _ in range(2):
                for _ in range(4):
                    yield tile
                    tile = tile.rotate()
                tile = tile.flip_vert()
            tile = tile.flip_horiz()

    def print(self):
        print(f'Tile {self.id}:')
        for r in self.rows:
            rs = ''
            for c in r:
                rs += c
            print(rs)

    def find_pattern(self, pattern):
        count = 0
        for i in range(len(self.rows) - len(pattern)):
            for j in range(len(self.rows[0]) - len(pattern[0])):
                if self._find_pattern(pattern, i, j):
                    count += 1
        return count
    
    def _find_pattern(self, pattern, i, j):
        for k in range(len(pattern)):
            for l in range(len(pattern[0])):
                if pattern[k][l] == '#' and self.rows[i + k][j + l] != '#':
                    return False
        return True

    def count_char(self, char):
        count = 0
        for row in self.rows:
            for c in row:
                if c == char:
                    count += 1
        return count

tiles = {}
tile_id = 0
reading = False
reading_rows = []
for line in sys.stdin:
    line = line.rstrip('\n')
    if not line:
        tiles[tile_id] = Tile(tile_id, reading_rows)
        reading = False
        reading_rows = []
    elif reading:
        reading_rows.append(line)
    else:
        reading = True
        tile_id = int(line.split()[1].rstrip(':'))

edges = {}
for t in tiles:
    t = tiles[t]
    for e in t.get_edges():
        if e not in edges:
            edges[e] = []
        edges[e].append(t)

for e in edges:
    s = ''
    for t in edges[e]:
        s += ' ' + str(t.id)

corner_tiles = []
for t in tiles:
    t = tiles[t]
    c = 0
    for e in t.get_edges():
        if len(edges[e]) == 1 and edges[e][0] == t:
            c += 1

    if c == 4:
        corner_tiles.append(t)

origin = corner_tiles[0]

tile_grid = []
for i in range(12):
    tile_grid_row = []
    for j in range(12):
        tile_grid_row.append(None)
    tile_grid.append(tile_grid_row)

for i in range(12):
    for j in range(12):
        if i == 0 and j == 0:
            for t in origin.get_all_transforms():
                if len(edges[t.top_side()]) == 1 and len(edges[t.left_side()]) == 1:
                    tile_grid[0][0] = t
                    break
        elif j == 0:
            upper_tile = tile_grid[i - 1][j]
            upper_tile_br = upper_tile.bottom_side()
            match_ids = set([match.id for match in edges[upper_tile_br]])
            match_ids.remove(upper_tile.id)
            assert len(match_ids) == 1
            match_id = match_ids.pop()
            match_tile = tiles[match_id]
            for t in match_tile.get_all_transforms():
                if t.top_side() == upper_tile_br:
                    tile_grid[i][j] = t
                    break
        else:
            left_tile = tile_grid[i][j - 1]
            left_tile_rr = left_tile.right_side()
            match_ids = set([match.id for match in edges[left_tile_rr]])
            match_ids.remove(left_tile.id)
            assert len(match_ids) == 1
            match_id = match_ids.pop()
            match_tile = tiles[match_id]
            for t in match_tile.get_all_transforms():
                if t.left_side() == left_tile_rr:
                    tile_grid[i][j] = t
                    break
        assert tile_grid[i][j]
        
grid = []
for i in range(12*8):
    grid_row = []
    for j in range(12*8):
        grid_row.append(0)
    grid.append(grid_row)

for i, tile_grid_row in enumerate(tile_grid):
    for j, tile in enumerate(tile_grid_row):
        for tile_i, tile_row in enumerate(tile.rows[1:-1]):
            for tile_j, val in enumerate(tile_row[1:-1]):
                grid[i * 8 + tile_i][j * 8 + tile_j] = val

g = Tile(0, grid)
pattern = []
pattern.append('                  # ')
pattern.append('#    ##    ##    ###')
pattern.append(' #  #  #  #  #  #   ')

for g1 in g.get_all_transforms():
    # Assume no overlaps
    c = g1.find_pattern(pattern)
    if c > 0:
        print(g1.count_char('#') - c * 15)
