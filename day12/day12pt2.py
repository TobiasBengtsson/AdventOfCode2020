import sys

class Ship:
    def __init__(self):
        self.coords = [0,0]
        self.directions = ['N', 'E', 'S', 'W']
        self.waypoint = [1, 10]
    
    def process_instruction(self, inst):
        if inst[0] in self.directions:
            self.move_waypoint(int(inst[1:]), inst[0])
        elif inst[0] == 'F':
            self.move_forward(int(inst[1:]))
        elif inst[0] == 'L':
            self.turn_waypoint_left(int(inst[1:]))
        elif inst[0] == 'R':
            self.turn_waypoint_right(int(inst[1:]))

    def move_waypoint(self, steps, direction):
        if direction == 'N':
            self.waypoint[0] += steps
        if direction == 'S':
            self.waypoint[0] -= steps
        if direction == 'E':
            self.waypoint[1] += steps
        if direction == 'W':
            self.waypoint[1] -= steps

    def move_forward(self, steps):
        self.coords[0] += self.waypoint[0] * steps
        self.coords[1] += self.waypoint[1] * steps

    def turn_waypoint_left(self, degrees):
        turns = degrees // 90
        for _ in range(turns):
            wp_0 = self.waypoint[0]
            wp_1 = self.waypoint[1]
            self.waypoint[0] = wp_1
            self.waypoint[1] = -wp_0

    def turn_waypoint_right(self, degrees):
        turns = degrees // 90
        for _ in range(turns):
            wp_0 = self.waypoint[0]
            wp_1 = self.waypoint[1]
            self.waypoint[0] = -wp_1
            self.waypoint[1] = wp_0

ship = Ship()
for line in sys.stdin:
    line = line.rstrip('\n')
    ship.process_instruction(line)
    
print(abs(ship.coords[0]) + abs(ship.coords[1]))
