import sys, os

instructions = []
for line in sys.stdin:
    line = line.rstrip('\n')
    spl = line.split()
    instruction = spl[0]
    value = int(spl[1])
    instructions.append((instruction, value))

acc = 0
instruction_i = 0
already_run = set()

while instruction_i not in already_run:
    already_run.add(instruction_i)
    instruction, count = instructions[instruction_i]
    if instruction == 'nop':
        instruction_i += 1
    elif instruction == 'acc':
        acc += count
        instruction_i += 1
    elif instruction == 'jmp':
        instruction_i += count

print(acc)
