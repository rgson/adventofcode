#!/usr/bin/env python3
input = open('input/day2.txt', 'r').read();

def task1(input):
    input = [[int(n) for n in l.split('x')] for l in input.split('\n') if l]
    total = 0
    for line in input:
        l, w, h = line
        sides = sorted([l*w, w*h, h*l])
        total += 2 * sum(sides) + sides[0]
    return total

def task2(input):
    input = [[int(n) for n in l.split('x')] for l in input.split('\n') if l]
    total = 0
    for line in input:
        sides = sorted(line)
        total += 2*sum(sides[:2]) + sides[0]*sides[1]*sides[2]
    return total

print(task1(input))
print(task2(input))
