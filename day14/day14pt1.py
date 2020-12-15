import sys

memory = {}
mask = ''
for line in sys.stdin:
    line = line.rstrip('\n')
    if line[:4] == 'mask':
        mask = line[7:]
        print(mask)
    else:
        sp = line.split('=')
        address = int(sp[0].split('[')[1].split(']')[0])
        num = int(sp[1].strip())
        num_binstr = format(num, 'b')
        num_binstr = num_binstr.zfill(36)
        masked_bin = ''
        for mask_char, num_char in zip(mask, num_binstr):
            if mask_char == 'X':
                masked_bin += num_char
            else:
                masked_bin += mask_char
        memory[address] = int(masked_bin, 2)

print(sum(memory.values()))
