#!/usr/bin/python3

import itertools

def parse_range(input):
    return tuple(int(i) for i in input.strip().split('-'))

def digits(integer):
    return [int(digit) for digit in str(integer)]

def pairs(xs):
    yield from zip(xs, xs[1:])

def are_increasing(xs):
    return all(a <= b for a, b in pairs(xs))

def has_doubles(xs):
    return any(a == b for a, b in pairs(xs))

def group_lengths(xs):
    yield from (len(list(group)) for key, group in itertools.groupby(xs))

def task1(input):
    start, end = parse_range(input)
    return sum(
        1 for i in range(start, end)
        if are_increasing(digits(i))
        and has_doubles(digits(i))
    )

def task2(input):
    start, end = parse_range(input)
    return sum(
        1 for i in range(start, end)
        if are_increasing(digits(i))
        and 2 in group_lengths(digits(i))
    )

input = open('input.txt', 'r').read()
print(task1(input))
print(task2(input))
