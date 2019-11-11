#!/usr/bin/env python3
from collections import Counter

input = open('input/day6.txt', 'r').read();

def task1(input):
    lines = [line for line in input.splitlines() if line]
    columns = zip(*lines)
    counters = [Counter(col) for col in columns]
    mostcommon = [c.most_common(1)[0][0] for c in counters]
    return ''.join(mostcommon)

def task2(input):
    lines = [line for line in input.splitlines() if line]
    columns = zip(*lines)
    counters = [Counter(col) for col in columns]
    leastcommon = [c.most_common()[:-2:-1][0][0] for c in counters]
    return ''.join(leastcommon)

print(task1(input))
print(task2(input))
