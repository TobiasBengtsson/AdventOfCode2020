import sys

seat_ids = []
for l in sys.stdin:
    l = l.rstrip('\n')
    hmin = 0
    hmax = 127
    for c in l[:7]:
        if c == 'F':
            hmax = hmax - ((hmax - hmin + 1) // 2)
        elif c == 'B':
            hmin = hmin + ((hmax - hmin + 1) // 2)
    
    vmin = 0
    vmax = 7
    for c in l[-3:]:
        if c == 'L':
            vmax = vmax - ((vmax - vmin + 1) // 2)
        elif c == 'R':
            vmin = vmin + ((vmax - vmin + 1) // 2)
            
    seat_ids.append(hmax * 8 + vmax)
    
prev_sid = -99
for s in sorted(seat_ids):
    if s - prev_sid == 2:
        print(s - 1)
    prev_sid = s
