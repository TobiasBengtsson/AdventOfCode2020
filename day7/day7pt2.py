import sys

# Search and replace in input to get the format
# light maroon=5 plaid blue,2 bright gray,4 vibrant chartreuse,3 dark indigo

children = {}
for line in sys.stdin:
    line = line.rstrip('\n')
    eq_split = line.split('=')
    parent = eq_split[0]
    children_list = eq_split[1].split(',')

    children[parent] = []
    
    for c in children_list:
        if c == 'no other':
            break
        cs = c.split()
        c_no_number = f'{cs[1]} {cs[2]}'
        c_count = int(cs[0])
        children[parent].append((c_count, c_no_number))

def get_subcount(target):
    if not children.get(target):
        return 0

    count = 0
    for c_count, child in children[target]:
        count += c_count
        count += c_count * get_subcount(child)
    return count

target = 'shiny gold'
print(get_subcount(target))
