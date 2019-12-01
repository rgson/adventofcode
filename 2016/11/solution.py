#!/usr/bin/env python3

#####
# UNFINISHED!
#####

from itertools import combinations
import enum
import copy
import re

class Item(object):
    def __init__(self, type, material):
        self.type = type
        self.material = material
    def complement(self):
        type = 'microchip' if self.type == 'generator' else 'generator'
        return Item(type, self.material)
    def __eq__(self, other):
        return self.type == other.type and self.material == other.material
    def __hash__(self):
        return hash((self.type, self.material))
    def __str__(self):
        return '{0} {1}'.format(self.material, self.type)

class State(object):
    def __init__(self):
        self.elevator = 0
        self.floors = [[] for i in range(4)]
    def copy(self):
        return copy.deepcopy(self)
    def add(self, floor, item):
        self.floors[floor].append(item)
    def move(self, floor, items):
        for item in items:
            self.floors[self.elevator].remove(item)
            self.floors[floor].append(item)
        self.elevator = floor
    def valid(self):
        for floor in self.floors:
            if any(i.type == 'generator' for i in floor):
                chips = [i for i in floor if i.type == 'microchip']
                if any(chip.complement() not in floor for chip in chips):
                    return False
        return True
    def done(self):
        return all(len(f) == 0 for f in self.floors[:-1])
    def child_states(self):
        items = self.floors[self.elevator]
        loads = [x for r in [1, 2] for x in combinations(items, r)]
        to_floors = [self.elevator - 1, self.elevator + 1]
        to_floors = [f for f in to_floors if 0 <= f and f < len(self.floors)]
        for to_floor in to_floors:
            for load in loads:
                state = self.copy()
                state.move(to_floor, load)
                yield state
    def __eq__(self, other):
        return self.elevator == other.elevator and self.floors == other.floors
    def __hash__(self):
        return hash((self.elevator, tuple([tuple(x) for x in self.floors])))
    def __str__(self):
        return '\n'.join('Floor {0}: {1}'.format(n, [str(i) for i in f]) for n, f in enumerate(self.floors))

def generate_input_state():
    """
    The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator, a ruthenium generator, a ruthenium-compatible microchip, a cobalt generator, and a cobalt-compatible microchip.
    The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
    The third floor contains nothing relevant.
    The fourth floor contains nothing relevant.
    """
    state = State()
    state.add(0, Item('generator', 'polonium'))
    state.add(0, Item('generator', 'thulium'))
    state.add(0, Item('microchip', 'thulium'))
    state.add(0, Item('generator', 'promethium'))
    state.add(0, Item('generator', 'ruthenium'))
    state.add(0, Item('microchip', 'ruthenium'))
    state.add(0, Item('generator', 'cobalt'))
    state.add(0, Item('microchip', 'cobalt'))
    state.add(1, Item('microchip', 'polonium'))
    state.add(1, Item('microchip', 'promethium'))
    return state

def find_solution(state, steps):
    queue = [(state, 0)]
    seen = set()
    while queue:
#        print("##########################################")
#        print("Steps:", steps)
#        print()
#        print("State:")
#        print(state)
        state, steps = queue.pop(0)
        if state.done():
            return steps
        if state.valid():
            children = [s for s in state.child_states() if s not in seen]
            queue += [(child, steps+1) for child in children]
            seen = seen | set(children)

def task1():
    state = generate_input_state()
    steps = find_solution(state, 0)
    return steps

def task2():
    pass

print(task1())
print(task2())
