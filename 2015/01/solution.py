#!/usr/bin/env python3
input = open('input.txt', 'r').read();

def task1(input):
    return sum([1 if c == '(' else -1 for c in input if c in ['(', ')']])

def task2(input):
    floor = 0
    for i, c in enumerate(input):
        floor += 1 if c == '(' else -1
        if floor < 0:
            return i + 1

print(task1(input))
print(task2(input))

