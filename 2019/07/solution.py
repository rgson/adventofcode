#!/usr/bin/python3

import itertools
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

def read_input(in_):
    return in_.pop(0)

def write_output(value, out):
    out.append(value)

def execute_stepwise(state, in_, out):
    pos = 0
    while True:
        op, modes = tokenize(state[pos])
        if op == 1:  # add
            x = read(state, pos+1, modes[0])
            y = read(state, pos+2, modes[1])
            write(state, pos+3, x + y)
            pos += 4
        elif op == 2:  # multiply
            x = read(state, pos+1, modes[0])
            y = read(state, pos+2, modes[1])
            write(state, pos+3, x * y)
            pos += 4
        elif op == 3:  # input
            write(state, pos+1, read_input(in_))
            pos += 2
        elif op == 4:  # output
            write_output(read(state, pos+1, modes[0]), out)
            pos += 2
        elif op == 5:  # jump-if-true
            x = read(state, pos+1, modes[0])
            y = read(state, pos+2, modes[1])
            pos = y if x != 0 else pos+3
        elif op == 6:  # jump-if-false
            x = read(state, pos+1, modes[0])
            y = read(state, pos+2, modes[1])
            pos = y if x == 0 else pos+3
        elif op == 7:  # less-than
            x = read(state, pos+1, modes[0])
            y = read(state, pos+2, modes[1])
            write(state, pos+3, int(x < y))
            pos += 4
        elif op == 8:  # equals
            x = read(state, pos+1, modes[0])
            y = read(state, pos+2, modes[1])
            write(state, pos+3, int(x == y))
            pos += 4
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

def amplify_signal(program, phase_settings, signal=0):
    for phase in phase_settings:
        out = []
        execute(program, [phase, signal], out)
        signal = out.pop()
    return signal

def amplify_signal_loop(program, phase_settings, signal=0):
    processes, ins, outs = [], [], []
    for phase in phase_settings:
        ins.append([phase])
        outs.append([])
        processes.append(execute_stepwise(program, ins[-1], outs[-1]))
    while True:
        for process, in_, out in zip(processes, ins, outs):
            in_.append(signal)
            for _ in process:
                if out:
                    signal = out.pop()
                    break
            else:
                return signal

def task1(input):
    program = deserialize(input)
    return max(
        amplify_signal(program, phase_settings)
        for phase_settings in itertools.permutations(range(5))
    )

def task2(input):
    program = deserialize(input)
    return max(
        amplify_signal_loop(program, phase_settings)
        for phase_settings in itertools.permutations(range(5, 10))
    )

input = open('input.txt', 'r').read()
print(task1(input))
print(task2(input))
