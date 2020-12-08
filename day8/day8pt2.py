import sys, os

instructions = []
for line in sys.stdin:
    line = line.rstrip('\n')
    spl = line.split()
    instruction = spl[0]
    value = int(spl[1])
    instructions.append((instruction, value))

def is_loop(instructions):
    instruction_i = 0
    already_run = set()
    while instruction_i not in already_run and instruction_i != len(instructions):
        already_run.add(instruction_i)
        instruction, count = instructions[instruction_i]
        if instruction == 'jmp':
            instruction_i += count
        else:
            instruction_i += 1
    return instruction_i in already_run

new_instructions = instructions.copy()
try_i = 0
while is_loop(new_instructions) and try_i <= len(instructions):
    instruction, count = instructions[try_i]
    while instruction != 'jmp':
        try_i += 1
        instruction, count = instructions[try_i]

    new_instructions = instructions.copy()
    new_instructions[try_i] = ('nop', 0)
    try_i += 1

acc = 0
instruction_i = 0
while instruction_i < len(instructions):
    instruction, count = new_instructions[instruction_i]
    if instruction == 'nop':
        instruction_i += 1
    elif instruction == 'acc':
        acc += count
        instruction_i += 1
    elif instruction == 'jmp':
        instruction_i += count

print(acc)
