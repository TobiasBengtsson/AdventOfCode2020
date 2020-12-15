import sys
import time

instructions = []
mask = ''
for line in sys.stdin:
    line = line.rstrip('\n')
    if line[:4] == 'mask':
        mask = line[7:]
    else:
        sp = line.split('=')
        address_str = sp[0].split('[')[1].split(']')[0]
        address = int(address_str)
        address_binstr = format(address, 'b')
        address_binstr = address_binstr.zfill(36)
        masked_binstr = ''
        for mask_char, address_char in zip(mask, address_binstr):
            if mask_char == '0':
                masked_binstr += address_char
            else:
                masked_binstr += mask_char

        instructions.append((masked_binstr, int(sp[1].strip())))

def intersect(address_set_1, address_set_2):
    # The memory addresses are actually sets of addresses and we
    # can implement an efficient intersect function.
    # Ex. 1001X10X1
    #     10X1XX0XX
    #     ---------
    #     1001X10X1
    if not address_set_1 or not address_set_2:
        return None
    intersection = ''
    for a1, a2 in zip(address_set_1, address_set_2):
        if a1 == a2:
            intersection += a1
        elif a1 == 'X':
            intersection += a2
        elif a2 == 'X':
            intersection += a1
        else:
            # a1 and a2 are different numbers
            return None
    return intersection

def intersect_list(address_sets):
    # Useful for intersecting 3 or more sets
    if len(address_sets) > 2:
        return intersect(address_sets[0], intersect_list(address_sets[1:]))
    elif len(address_sets) == 2:
        return intersect(address_sets[0], address_sets[1])
    elif address_sets:
        return address_sets[0]
    else:
        return None

# When (a set of) memory adress(es) are written, they end
# up as they are in the base array.
#
# We then check which previous writes that are overwritten,
# and add the part that was overwritten to the less array
# for the index corresponding to the earlier write.
#
# Value for every write is stored in vals.
base = []
less = []
vals = []
for i, (a, v) in enumerate(instructions):
    base.append(a)
    less.append([])
    vals.append(v)
    for j, (a2, _) in enumerate(instructions[:i]):
        # Can improve O of finding conflicts with some R-tree like data structure?
        inter = intersect(a, a2)
        if inter:
            if inter == a:
                # The whole previous write has been overwritten.
                # We can now discard it.
                less[j] = []
                vals[j] = 0
            elif vals[j] != 0: # No need to overwrite prev. discarded
                less[j].append(inter)

def cardinality(address_set):
    if not address_set:
        return 0

    return 2 ** address_set.count('X')

def get_union_idxs(depth, sets_n):
    # https://proofwiki.org/wiki/Cardinality_of_Set_Union
    # Returns a list of lists of indices 1 < i1 < i2 < .. < ik < n
    # for given depth = k - 1
    #
    # E.g.
    # get_union_idxs(3, 4)
    # [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
    if depth == 0:
        for i in range(sets_n):
            yield [i]
        return

    if depth >= sets_n:
        raise Exception("Depth was greater than number of sets")
    
    # We build by appending the last ik to the prev. depth
    # E.g.
    # prev_depth            depth
    # [0, 1]                [0, 1, 2]
    #                       [0, 1, 3]
    #                       [0, 1, 4]
    # [0, 2]                [0, 2, 3]
    #                       [0, 2, 4]
    # [0, 3]                [0, 3, 4]
    # [1, 2]                [1, 2, 3]
    #                       [1, 2, 4]
    # ...
    prev_depth = get_union_idxs(depth - 1, sets_n)
    for p in prev_depth:
        i = p[-1] + 1
        while i < sets_n:
            p_copy = p.copy()
            p_copy.append(i)
            yield p_copy
            i += 1

def cardinality_union(sets):
    # https://proofwiki.org/wiki/Cardinality_of_Set_Union

    rolling_sum = 0

    for depth in range(len(sets)):
        depth_sum = 0
        depth_idxs = get_union_idxs(depth, len(sets))
        for idxs in depth_idxs:
            l = []
            for i in idxs:
                l.append(sets[i])

            inter = intersect_list(l)
            depth_sum += cardinality(inter)
        
        if depth % 2 == 0:
            rolling_sum += depth_sum
        else:
            rolling_sum -= depth_sum

    return rolling_sum

answer = 0
for b, l, v in zip(base, less, vals):
    b_cardinality = cardinality(b)
    b_cardinality -= cardinality_union(l)
    answer += b_cardinality * v

print(answer)
