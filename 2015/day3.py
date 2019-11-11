#!/usr/bin/env python3
input = open('input/day3.txt', 'r').read();

def move(position, direction):
    x, y = position
    x += 1 if direction == '>' else -1 if direction == '<' else 0
    y += 1 if direction == '^' else -1 if direction == 'v' else 0
    return (x, y)

def find_visited(directions):
    position = (0, 0)
    visited = {position}
    for direction in directions:
        position = move(position, direction)
        visited.add(position)
    return visited

def task1(input):
    return len(find_visited(input))

def task2(input):
    santa = find_visited([d for i, d in enumerate(input) if i % 2])
    robot = find_visited([d for i, d in enumerate(input) if not i % 2])
    return len(santa | robot)

print(task1(input))
print(task2(input))
