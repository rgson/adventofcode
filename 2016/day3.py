#!/usr/bin/env python3
input = open('input/day3.txt', 'r').read();

def task1(input):
    numbers = [sorted([int(x) for x in line.split()]) for line in input.splitlines() if line]
    valid = [True if sum(n[:2]) > n[2] else False for n in numbers]
    return sum(valid)

def task2(input):
    numbers = [[int(x) for x in line.split()] for line in input.splitlines() if line]
    numbers = [x for row in zip(*numbers) for x in row]
    numbers = [sorted(numbers[i:i+3]) for i in range(0, len(numbers), 3)]
    valid = [True if sum(n[:2]) > n[2] else False for n in numbers]
    return sum(valid)

print(task1(input))
print(task2(input))
