import os
import sys

class Map:
    def __init__(self):
        self.map = ['.'*30]*10
        self.start = Vec(1,1)
        self.goal = Vec(10,9)
        
    def print_with_state(self, state):
        for y, line in enumerate(self.map):
            for x, c in enumerate(line):
                curr = Vec(x,y)
                if curr == state.pos:
                    print('M', end='')
                elif curr == self.goal:
                    print('G', end='')
                elif curr in state.choices():
                    for i, choice in enumerate(state.choices()):
                        if curr == choice:
                            print(i, end='')
                else:
                    print(c, end='')
            print()
    
    def print_solution(self, sol):
        steps = list(step.pos for step in sol.branch())
        for y, line in enumerate(self.map):
            for x, c in enumerate(line):
                curr = Vec(x,y)
                if curr in steps:
                    for i, step in enumerate(steps):
                        if curr == step:
                            print(i, end='')
                else:
                    print(c, end='')
            print()

    def is_position_valid(self, pos):
        return pos.x >= 0 and pos.y >= 0 and pos.x < len(self.map[0]) and pos.y < len(self.map) 

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "Vec(%s,%s)" % (self.x, self.y)

    def __repr__(self):
        return str(self)


class State:
    def __init__(self, pos, vel=Vec(0,0), parent=None):
        self.pos = pos
        self.vel = vel
        self.parent = parent
    
    def choices(self):
        for dx in -1,0,1:
            for dy in -1,0,1:
                yield self.pos+self.vel+Vec(dx,dy)

    def choose(self, choice):
        return State(pos=choice, vel=choice-self.pos-self.vel, parent=self)

    def branch(self):
        if self.parent:
            yield from self.parent.branch()
        yield self

    def __str__(self):
        return "State(pos=%s,vel=%s,parent=%s)" % (self.pos, self.vel, self.parent)


######### SOLVER ##############

def trim(states):
    return states 

def solve(map):
    start = State(map.start)
    map.print_with_state(start)
    to_explore = [start]
    to_explore_next = []
    while True:
        print("let's explore ",len(to_explore))
        for state in to_explore:
            for choice in state.choices():
                next_state = state.choose(choice)
                if map.is_position_valid(next_state.pos):
                    if next_state.pos == map.goal:
                        return next_state
                    to_explore_next.append(next_state)
                if len(to_explore_next) > 100000:
                    print("Nope, try to optimize the algo!")
                    sys.exit()
        to_explore = to_explore_next
        to_explore_next = []




def play(map):
    state = State(map.start)
    while True:
        os.system('clear')
        print('\n'*4)
        map.print_with_state(state)
        print('\n'*4)

        if state.pos == map.goal:
            print("bravo!")
            break
        if not map.is_position_valid(state.pos):
            print("Ooops, you went outside the bounds")
            break

        choices = list(state.choices())
        print(state.vel)
        i = int(input("Choice: "))
        state = state.choose(choices[i])


map = Map()
sol = solve(map)
map.print_solution(sol)
