import sys

class Tile:
    def __init__(self, id, rows):
        self.id = id
        self.rows = rows

    def top_row(self):
        return tuple(self.rows[0])

    def rev_top_row(self):
        return tuple(self.rows[0][::-1])

    def bottom_row(self):
        return tuple(self.rows[-1])

    def rev_bottom_row(self):
        return tuple(self.rows[-1][::-1])
    
    def left_row(self):
        col = []
        for row in self.rows:
            col.append(row[0])

        return tuple(col)

    def rev_left_row(self):
        col = []
        for row in self.rows:
            col.append(row[0])

        col.reverse()
        return tuple(col)

    def right_row(self):
        col = []
        for row in self.rows:
            col.append(row[-1])

        return tuple(col)

    def rev_right_row(self):
        col = []
        for row in self.rows:
            col.append(row[-1])

        col.reverse()
        return tuple(col)

    def get_edges(self):
        ret = []
        ret.append(self.top_row())
        ret.append(self.rev_top_row())
        ret.append(self.bottom_row())
        ret.append(self.rev_bottom_row())
        ret.append(self.left_row())
        ret.append(self.rev_left_row())
        ret.append(self.right_row())
        ret.append(self.rev_right_row())
        return ret

tiles = []
tile_id = 0
reading = False
reading_rows = []
for line in sys.stdin:
    line = line.rstrip('\n')
    if not line:
        tiles.append(Tile(tile_id, reading_rows))
        reading = False
        reading_rows = []
    elif reading:
        reading_rows.append(line)
    else:
        reading = True
        tile_id = int(line.split()[1].rstrip(':'))

edges = {}
for t in tiles:
    print(t.id)
    for e in t.get_edges():
        print(e)
        if e not in edges:
            edges[e] = []
        edges[e].append(t)

for e in edges:
    s = ''
    for t in edges[e]:
        s += ' ' + str(t.id)
    print(f'{e}: {s}')

ans = 1
for t in tiles:
    c = 0
    for e in t.get_edges():
        if len(edges[e]) == 1 and edges[e][0] == t:
            c += 1

    if c == 4:
        ans *= t.id

print(ans)
