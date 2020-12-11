import sys

seat_grid = []
for line in sys.stdin:
    line = line.rstrip('\n')
    seat_row = []
    for c in line:
        seat_row.append(c)
    seat_grid.append(seat_row)

def get_first_in_direction(seat_grid, start_i, start_j, dir_i, dir_j):
    # directions either -1, 0 or 1.
    if dir_i == 0 and dir_j == 0:
        # To prevent potential infinite loop
        return seat_grid[start_i][start_j]

    current_i = start_i
    current_j = start_j
    next_i = current_i + dir_i
    next_j = current_j + dir_j
    while next_i < len(seat_grid) and next_i >= 0 and next_j < len(seat_grid[0]) and next_j >=0:
        current_i = next_i
        current_j = next_j
        next_i = current_i + dir_i
        next_j = current_j + dir_j
        if seat_grid[current_i][current_j] in ('L', '#'):
            return seat_grid[current_i][current_j]

        if next_i >= len(seat_grid) or next_i < 0 or next_j >= len(seat_grid[0]) or next_j < 0:
            return seat_grid[current_i][current_j]

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
                adj.append(get_first_in_direction(seat_grid, i, j, 0, 1))
                adj.append(get_first_in_direction(seat_grid, i, j, 0, -1))
                adj.append(get_first_in_direction(seat_grid, i, j, 1, 0))
                adj.append(get_first_in_direction(seat_grid, i, j, 1, -1))
                adj.append(get_first_in_direction(seat_grid, i, j, 1, 1))
                adj.append(get_first_in_direction(seat_grid, i, j, -1, 1))
                adj.append(get_first_in_direction(seat_grid, i, j, -1, 0))
                adj.append(get_first_in_direction(seat_grid, i, j, -1, -1))

                occ = sum(a == '#' for a in adj)

                if occ == 0 and seat == 'L':
                    new_seat_grid[i][j] = '#'
                elif occ >= 5 and seat == '#':
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
