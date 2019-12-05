#!/usr/bin/python3

import sys

def deserialize(input):
    return [int(x) for x in input.strip().split(',')]

def digits(integer):
    return [int(digit) for digit in str(integer)]

def tokenize(instruction):
    a, b, c, d, e = (4*[0] + digits(instruction))[-5:]
    return (e + 10 * d, (c, b, a))

def read(state, pos, immediate_mode=False):
    return state[pos] if immediate_mode else read(state, state[pos], True)

def write(state, pos, value):
    state[state[pos]] = value

def read_input(stdin):
    return int(stdin.pop(0))

def write_output(value):
    print('|', value)

def execute(state, pos=0, stdin=None):
    op, modes = tokenize(state[pos])
    if op == 1:  # add
        x = read(state, pos+1, modes[0])
        y = read(state, pos+2, modes[1])
        write(state, pos+3, x + y)
        return execute(state, pos+4, stdin)
    if op == 2:  # multiply
        x = read(state, pos+1, modes[0])
        y = read(state, pos+2, modes[1])
        write(state, pos+3, x * y)
        return execute(state, pos+4, stdin)
    if op == 3:  # input
        write(state, pos+1, read_input(stdin))
        return execute(state, pos+2, stdin)
    if op == 4:  # output
        write_output(read(state, pos+1, modes[0]))
        return execute(state, pos+2, stdin)
    if op == 5:  # jump-if-true
        x = read(state, pos+1, modes[0])
        y = read(state, pos+2, modes[1])
        p = y if x != 0 else pos+3
        return execute(state, p, stdin)
    if op == 6:  # jump-if-false
        x = read(state, pos+1, modes[0])
        y = read(state, pos+2, modes[1])
        p = y if x == 0 else pos+3
        return execute(state, p, stdin)
    if op == 7:  # less-than
        x = read(state, pos+1, modes[0])
        y = read(state, pos+2, modes[1])
        write(state, pos+3, int(x < y))
        return execute(state, pos+4, stdin)
    if op == 8:  # equals
        x = read(state, pos+1, modes[0])
        y = read(state, pos+2, modes[1])
        write(state, pos+3, int(x == y))
        return execute(state, pos+4, stdin)
    if op == 99:  # halt
        return state
    print('1202 program alarm', file=sys.stderr)
    return state

def task1(input):
    execute(deserialize(input), stdin=[1])

def task2(input):
    execute(deserialize(input), stdin=[5])

input = open('input.txt', 'r').read()
print(task1(input))
print(task2(input))
