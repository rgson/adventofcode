#!/usr/bin/env python3
import re

input = open('input.txt', 'r').read();

def parse_command(line):
    match = re.match('(rect) (\d+)x(\d+)', line)
    if not match:
        match = re.match('(rotate \w+) [xy]=(\d+) by (\d+)', line)
    if match:
        cmd, a, b = match.group(1, 2, 3)
        return (cmd, int(a), int(b))
    return None

def screen_rect(screen, width, height):
    for x in range(width):
        for y in range(height):
            screen[y][x] = True

def screen_rotate_row(screen, row, pixels):
    for i in range(pixels):
        prev = screen[row][-1]
        for column in range(len(screen[row])):
            prev, screen[row][column] = screen[row][column], prev

def screen_rotate_column(screen, column, pixels):
    for i in range(pixels):
        prev = screen[-1][column]
        for row in range(len(screen)):
            prev, screen[row][column] = screen[row][column], prev

def screen_render(screen, commands):
    cmds = [parse_command(line) for line in commands]
    for (cmd, a, b) in cmds:
        if (cmd == 'rect'):
            screen_rect(screen, a, b)
        elif (cmd == 'rotate row'):
            screen_rotate_row(screen, a, b)
        elif (cmd == 'rotate column'):
            screen_rotate_column(screen, a, b)

def screen_print(screen):
    return '\n'.join([''.join(['#' if x else '.' for x in row]) for row in screen])

def task1(input):
    lines = [line for line in input.splitlines() if line]
    screen = [50*[False] for row in range(6)]
    screen_render(screen, lines)
    return sum([sum(row) for row in screen])

def task2(input):
    lines = [line for line in input.splitlines() if line]
    screen = [50*[False] for row in range(6)]
    screen_render(screen, lines)
    return screen_print(screen)

print(task1(input))
print(task2(input))
