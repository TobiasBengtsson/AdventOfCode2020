import sys

# Originally solved by Wolfram Alpha by pasting the following:
# -t mod 23 = 0, -t mod 41 = 13, -t mod 733 = 23, -t mod 13 = 10, -t mod 17 = 3, -t mod 19 = 4, -t mod 29 = 23, -t mod 449 = 54, -t mod 37 = 17 

earliest_time = int(sys.stdin.readline().rstrip('\n'))
id_strings = sys.stdin.readline().rstrip('\n').split(',')
operational_ids = []
targets = []
for i, ids in enumerate(id_strings):
    if ids != 'x':
        operational_ids.append(int(ids))
        targets.append(i % int(ids))
