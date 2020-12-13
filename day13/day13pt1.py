import sys

earliest_time = int(sys.stdin.readline().rstrip('\n'))
id_strings = sys.stdin.readline().rstrip('\n').split(',')
operational_ids = []
for ids in id_strings:
    if ids != 'x':
        operational_ids.append(int(ids))

min_time = 999999
min_id = 999999
for id in operational_ids:
    time = (-earliest_time) % id
    if time < min_time:
        min_time = time
        min_id = id

print(min_id * min_time)
