import sys

g_count = 0

for line in sys.stdin:
    line = line.rstrip('\n')
    split = line.split(' ')
    pos1 = int(split[0].split('-')[0])
    pos2 = int(split[0].split('-')[1])
    letter = split[1].rstrip(':')
    
    passwd = split[2]
    pos = 1
    if (passwd[pos1-1] == letter and passwd[pos2-1] != letter) or (passwd[pos1-1] != letter and passwd[pos2-1] == letter):
        g_count += 1

print(g_count)
