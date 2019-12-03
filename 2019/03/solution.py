#!/usr/bin/python3

origin = (0, 0)

def to_paths(input):
    return [line.strip().split(',') for line in input.splitlines()]

def traverse(path):
    x, y = origin
    for move in path:
        direction, steps = move[0], int(move[1:])
        dx = 1 if direction == 'R' else -1 if direction == 'L' else 0
        dy = 1 if direction == 'U' else -1 if direction == 'D' else 0
        for _ in range(steps):
            x += dx
            y += dy
            yield x, y

def crossings(path1, path2):
    return set(traverse(path1)) & set(traverse(path2))

def steps_to_crossings(path1, path2):
    steps1 = dict(reversed([reversed(x) for x in enumerate(traverse(path1))]))
    steps2 = dict(reversed([reversed(x) for x in enumerate(traverse(path2))]))
    for crossing in steps1.keys() & steps2.keys():
        yield steps1[crossing] + steps2[crossing] + 2  # step count starts at 0

def manhattan_distance(a, b=origin):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def task1(input):
    return min(manhattan_distance(p) for p in crossings(*to_paths(input)))

def task2(input):
    return min(steps_to_crossings(*to_paths(input)))

input = open('input.txt', 'r').read()
print(task1(input))
print(task2(input))
