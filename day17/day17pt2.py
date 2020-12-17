import sys

space = {}

x = 0
for line in sys.stdin:
    line = line.rstrip('\n')
    
    y = 0
    for c in line:
        space[(x, y, 0, 0)] = c
        y -= 1
    x += 1

def get_neighbors(x, y, z, w):
    for i in (x - 1, x, x + 1):
        for j in (y - 1, y, y + 1):
            for k in (z - 1, z, z + 1):
                for l in (w - 1, w, w + 1):
                    if i == x and j == y and k == z and l == w:
                        continue
                    if (i, j, k, l) not in space:
                        yield '.'
                    else:
                        yield space[(i, j, k, l)]

def simulate_one_turn(space):
    x_rng = [0,0]
    y_rng = [0,0]
    z_rng = [0,0]
    w_rng = [0,0]
    for (x, y, z, w) in space:
        x_rng[0] = min(x_rng[0], x - 1)
        x_rng[1] = max(x_rng[1], x + 1)
        y_rng[0] = min(y_rng[0], y - 1)
        y_rng[1] = max(y_rng[1], y + 1)
        z_rng[0] = min(z_rng[0], z - 1)
        z_rng[1] = max(z_rng[1], z + 1)
        w_rng[0] = min(w_rng[0], w - 1)
        w_rng[1] = max(w_rng[1], w + 1)

    new_space = space.copy()
    for i in range(x_rng[0], x_rng[1] + 1):
        for j in range(y_rng[0], y_rng[1] + 1):
            for k in range(z_rng[0], z_rng[1] + 1):
                for l in range(w_rng[0], w_rng[1] + 1):
                    this_state = ''
                    if (i, j, k, l) not in space:
                        this_state = '.'
                    else:
                        this_state = space[(i, j, k, l)]
                    active_count = 0
                    for neighbor in get_neighbors(i, j, k, l):
                        if neighbor == '#':
                            active_count += 1
                    if active_count == 3 and this_state == '.':
                        new_space[(i, j, k, l)] = '#'
                    elif active_count in (2,3) and this_state == '#':
                        new_space[(i, j, k, l)] = '#'
                    else:
                        new_space[(i, j, k, l)] = '.'
    return new_space

for i in range(6):
    space = simulate_one_turn(space)

count = 0
for (x, y, z, w) in space:
    if space[(x, y, z, w)] == '#':
        count += 1

print(count)
