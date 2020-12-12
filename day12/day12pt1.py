import sys

class Ship:
    def __init__(self):
        self.coords = [0,0]
        self.dir = 'E'
        self.clockwise = ['N', 'E', 'S', 'W']
    
    def process_instruction(self, inst):
        if inst[0] in self.clockwise:
            self.move_forward(int(inst[1:]), inst[0])
        elif inst[0] == 'F':
            self.move_forward(int(inst[1:]), self.dir)
        elif inst[0] == 'L':
            self.turn_left(int(inst[1:]))
        elif inst[0] == 'R':
            self.turn_right(int(inst[1:]))

    def move_forward(self, steps, direction):
        if direction == 'N':
            self.coords[0] += steps
        if direction == 'S':
            self.coords[0] -= steps
        if direction == 'E':
            self.coords[1] += steps
        if direction == 'W':
            self.coords[1] -= steps

    def turn_left(self, degrees):
        self._turn(-degrees)

    def turn_right(self, degrees):
        self._turn(degrees)

    def _turn(self, degrees):
        i = self.clockwise.index(self.dir)
        i = (i + degrees // 90) % 4
        self.dir = self.clockwise[i]

ship = Ship()
for line in sys.stdin:
    line = line.rstrip('\n')
    ship.process_instruction(line)
    
print(abs(ship.coords[0]) + abs(ship.coords[1]))
