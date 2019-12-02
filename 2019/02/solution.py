#!/usr/bin/python3

import sys

def deserialize(input):
    return [int(x) for x in input.strip().split(',')]

def execute(state, pos=0):
    op = state[pos]
    if op == 1:
        x, y, o = state[pos+1:pos+4]
        state[o] = state[x] + state[y]
        return execute(state, pos+4)
    if op == 2:
        x, y, o = state[pos+1:pos+4]
        state[o] = state[x] * state[y]
        return execute(state, pos+4)
    if op == 99:
        return state
    print('1202 program alarm', file=sys.stderr)
    return state

def task1(input):
    state = deserialize(input)
    state[1] = 12
    state[2] = 2
    state = execute(state)
    return state[0]

def task2(input):
    program = deserialize(input)
    for noun in range(100):
        for verb in range(100):
            state = [x for x in program]
            state[1] = noun
            state[2] = verb
            state = execute(state)
            if state[0] == 19690720:
                return 100 * noun + verb

input = open('input.txt', 'r').read()
print(task1(input))
print(task2(input))
