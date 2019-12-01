#!/usr/bin/python3

def fuel(mass):
    return mass // 3 - 2

def masses(input):
    return (int(line.strip()) for line in input.splitlines() if line)

def task1(input):
    return sum(fuel(mass) for mass in masses(input))

def fuel_recursive(mass):
    f = fuel(mass)
    return (f + fuel_recursive(f)) if f > 0 else 0

def task2(input):
    return sum(fuel_recursive(mass) for mass in masses(input))

input = open('input.txt', 'r').read()
print(task1(input))
print(task2(input))
