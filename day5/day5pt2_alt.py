import sys

seat_ids = []
for l in sys.stdin:
    l = l.rstrip('\n')
    bin_string = l.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
    seat_id = int(bin_string, 2)
    seat_ids.append(seat_id)

prev_sid = -99
for s in sorted(seat_ids):
    if s - prev_sid == 2:
        print(s - 1)
    prev_sid = s
