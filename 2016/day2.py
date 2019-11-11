#!/usr/bin/env python3
input = open('input/day2.txt', 'r').read();

def clamp(n, lower, upper):
    return max(lower, min(n, upper))

def task1(input):
    instructions = [line for line in input.splitlines() if line]
    key = {(d % 3, d // 3): d + 1 for d in range(9)}
    x, y = 1, 1; # 5
    code = ""
    for line in instructions:
        for c in line:
            x = clamp(x + 1 if c == 'R' else x - 1 if c == 'L' else x, 0, 2)
            y = clamp(y + 1 if c == 'D' else y - 1 if c == 'U' else y, 0, 2)
        code += str(key[(x, y)])
    return code

def task2(input):
    instructions = [line for line in input.splitlines() if line]
    key = [[None, None, '1' , None, None],
           [None, '2' , '3' , '4' , None],
           ['5' , '6' , '7' , '8' , '9' ],
           [None, 'A' , 'B' , 'C' , None],
           [None, None, 'D' , None, None]]
    x, y = 0, 2; # 5
    code = ""
    for line in instructions:
        for c in line:
            x2 = x + 1 if c == 'R' else x - 1 if c == 'L' else x
            y2 = y + 1 if c == 'D' else y - 1 if c == 'U' else y
            try:
                x, y = (x2, y2) if key[y2][x2] else (x, y)
            except IndexError:
                pass
        code += key[y][x]
    return code

print(task1(input))
print(task2(input))
