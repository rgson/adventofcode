#!/usr/bin/python3

import itertools
import sys

class IntcodeMemory(list):
    def __getitem__(self, index):
        return list.__getitem__(self, index) if index < len(self) else 0
    def __setitem__(self, index, value):
        if index >= len(self):
            self.extend([0] * (index - len(self) + 1))
        return list.__setitem__(self, index, value)

def deserialize(input):
    return IntcodeMemory(int(x) for x in input.strip().split(','))

def digits(integer):
    return [int(digit) for digit in str(integer)]

def tokenize(instruction):
    a, b, c, d, e = (4*[0] + digits(instruction))[-5:]
    return (e + 10 * d, (c, b, a))

def read(state, pos, mode=0, relbase=0):
    if mode == 0:
        return read(state, state[pos], mode=1)
    if mode == 1:
        return state[pos]
    if mode == 2:
        return read(state, state[pos] + relbase, mode=1)
    print('invalid read mode:', mode, file=sys.stderr)

def write(state, pos, value, mode=0, relbase=0):
    if mode == 0:
        state[state[pos]] = value
    elif mode == 2:
        state[state[pos] + relbase] = value
    else:
        print('invalid write mode:', mode, file=sys.stderr)

def read_input(in_):
    return in_.pop(0)

def write_output(value, out):
    out.append(value)

def execute_stepwise(state, in_, out):
    pos, relbase = 0, 0
    while True:
        op, modes = tokenize(state[pos])
        if op == 1:  # add
            x = read(state, pos+1, modes[0], relbase)
            y = read(state, pos+2, modes[1], relbase)
            write(state, pos+3, x + y, modes[2], relbase)
            pos += 4
        elif op == 2:  # multiply
            x = read(state, pos+1, modes[0], relbase)
            y = read(state, pos+2, modes[1], relbase)
            write(state, pos+3, x * y, modes[2], relbase)
            pos += 4
        elif op == 3:  # input
            write(state, pos+1, read_input(in_), modes[0], relbase)
            pos += 2
        elif op == 4:  # output
            write_output(read(state, pos+1, modes[0], relbase), out)
            pos += 2
        elif op == 5:  # jump-if-true
            x = read(state, pos+1, modes[0], relbase)
            y = read(state, pos+2, modes[1], relbase)
            pos = y if x != 0 else pos+3
        elif op == 6:  # jump-if-false
            x = read(state, pos+1, modes[0], relbase)
            y = read(state, pos+2, modes[1], relbase)
            pos = y if x == 0 else pos+3
        elif op == 7:  # less-than
            x = read(state, pos+1, modes[0], relbase)
            y = read(state, pos+2, modes[1], relbase)
            write(state, pos+3, int(x < y), modes[2], relbase)
            pos += 4
        elif op == 8:  # equals
            x = read(state, pos+1, modes[0], relbase)
            y = read(state, pos+2, modes[1], relbase)
            write(state, pos+3, int(x == y), modes[2], relbase)
            pos += 4
        elif op == 9:  # adjust relative base
            x = read(state, pos+1, modes[0], relbase)
            relbase += x
            pos += 2
        elif op == 99:  # halt
            return
        else:  # invalid opcode
            print('1202 program alarm', file=sys.stderr)
            return
        yield state

def last(iterable):
    for item in iterable:
        pass
    return item

def execute(state, in_, out):
    return last(execute_stepwise(state, in_, out))

def task1(input):
    program = deserialize(input)
    out = []
    execute(program, [1], out)
    return out.pop()

def task2(input):
    program = deserialize(input)
    out = []
    execute(program, [2], out)
    return out.pop()

input = open('input.txt', 'r').read()
print(task1(input))
print(task2(input))
