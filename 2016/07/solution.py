#!/usr/bin/env python3
input = open('input.txt', 'r').read();

def contains_abba(s):
    for i in range(len(s)-3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            return True
    return False

def task1(input):
    lines = [line for line in input.splitlines() if line]
    splitlines = [line.replace('[', ']').split(']') for line in lines]
    count = 0
    for split in splitlines:
        abba_outside_brackets = max([contains_abba(s) for s in split[::2]])
        abba_within_brackets = max([contains_abba(s) for s in split[1::2]])
        count += 1 if abba_outside_brackets and not abba_within_brackets else 0
    return count

def task2(input):
    lines = [line for line in input.splitlines() if line]
    splitlines = [line.replace('[', ']').split(']') for line in lines]
    count = 0
    for split in splitlines:
        outside_brackets = split[::2]
        within_brackets = split[1::2]
        abas = {s[i:i+3] for s in outside_brackets for i in range(len(s)-2)
                if s[i] == s[i+2] and s[i] != s[i+1]}
        babs = {aba[1] + aba[0] + aba[1] for aba in abas}
        count += bool(sum([1 for s in within_brackets for bab in babs if bab in s]))
    return count

print(task1(input))
print(task2(input))
