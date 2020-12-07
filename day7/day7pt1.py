import sys

# Search and replace in input to get the format
# light maroon=5 plaid blue,2 bright gray,4 vibrant chartreuse,3 dark indigo

parents = {}
for line in sys.stdin:
    line = line.rstrip('\n')
    eq_split = line.split('=')
    parent = eq_split[0]
    children = eq_split[1].split(',')
    
    for c in children:
        if c == 'no other':
            break
        cs = c.split()
        c_no_number = f'{cs[1]} {cs[2]}'

        if not parents.get(c_no_number):
            parents[c_no_number] = []
        parents[c_no_number].append(parent)

target = 'shiny gold'
ans = 0
possible = set()
current_parents = parents[target]
while current_parents:
    new_parents = set()
    for p in current_parents:
        possible.add(p)
        if parents.get(p):
            for np in parents[p]:
                new_parents.add(np)
    current_parents = new_parents

print(len(possible))
