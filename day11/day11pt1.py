import sys

seat_grid = []
for line in sys.stdin:
    line = line.rstrip('\n')
    seat_row = []
    for c in line:
        seat_row.append(c)
    seat_grid.append(seat_row)

def iterate(seat_grid):
    new_seat_grid = seat_grid.copy()
    for i, row in enumerate(seat_grid):
        new_seat_grid[i] = row.copy()

    for i, seat_row in enumerate(seat_grid):
        for j, seat in enumerate(seat_row):
            if seat == '.':
                continue
            else:
                adj = []
                if j + 1 < len(seat_row):
                    adj.append(seat_grid[i][j+1])
                if j > 0:
                    adj.append(seat_grid[i][j-1])
                if i > 0:
                    adj.append(seat_grid[i-1][j])
                if i > 0 and j > 0:
                    adj.append(seat_grid[i-1][j-1])
                if i > 0 and j + 1 < len(seat_row):
                    adj.append(seat_grid[i-1][j+1])
                if i + 1 < len(seat_grid):
                    adj.append(seat_grid[i+1][j])
                if i +1 < len(seat_grid) and j > 0:
                    adj.append(seat_grid[i+1][j-1])
                if i + 1 < len(seat_grid) and j + 1 < len(seat_row):
                    adj.append(seat_grid[i+1][j+1])

                occ = sum(a == '#' for a in adj)

                if occ == 0 and seat == 'L':
                    new_seat_grid[i][j] = '#'
                elif occ >= 4 and seat == '#':
                    new_seat_grid[i][j] = 'L'

    return new_seat_grid

def count_occ(seat_grid):
    count = 0
    for seat_row in seat_grid:
        count += sum(seat == '#' for seat in seat_row)
    return count

prev_count = -1
count = 0
while prev_count != count:
    prev_count = count
    seat_grid = iterate(seat_grid)
    count = count_occ(seat_grid)

print(count)
