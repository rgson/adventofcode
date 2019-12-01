#!/usr/bin/env python3
input = open('input.txt', 'r').read();

def task1(input):
    instructions = [(i[0], int(i[1:])) for i in input.split(', ')]
    # 0: North, 1: East, 2: South, 3: West
    movement = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    facing = 0
    position = (0, 0)
    for direction, distance in instructions:
        facing = (facing + 1 if direction == 'R' else facing - 1) % 4
        position = (position[0] + movement[facing][0] * distance,
                    position[1] + movement[facing][1] * distance)
    return abs(position[0]) + abs(position[1])

def task2(input):
    instructions = [(i[0], int(i[1:])) for i in input.split(', ')]
    # 0: North, 1: East, 2: South, 3: West
    movement = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
    facing = 0
    position = (0, 0)
    visited = {position}
    for direction, distance in instructions:
        facing = (facing + 1 if direction == 'R' else facing - 1) % 4
        for d in range(distance):
            position = (position[0] + movement[facing][0],
                        position[1] + movement[facing][1])
            if position in visited:
                return abs(position[0]) + abs(position[1])
            visited.add(position)

print(task1(input))
print(task2(input))
