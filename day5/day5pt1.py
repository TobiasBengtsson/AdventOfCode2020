import sys

h_gmax = 0
v_gmax = 0
for l in sys.stdin:
    l = l.rstrip('\n')
    hmin = 0
    hmax = 127
    for c in l[:7]:
        if c == 'F':
            hmax = hmax - ((hmax - hmin + 1) // 2)
        elif c == 'B':
            hmin = hmin + ((hmax - hmin + 1) // 2)
    h_gmax = max(h_gmax, hmax)
    
    vmin = 0
    vmax = 7
    for c in l[-3:]:
        if c == 'L':
            vmax = vmax - ((vmax - vmin + 1) // 2)
        elif c == 'R':
            vmin = vmin + ((vmax - vmin + 1) // 2)
    h_vmax = max(v_gmax, vmax)
    
print(str(h_gmax * 8 + v_gmax))
