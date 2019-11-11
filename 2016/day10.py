#!/usr/bin/env python3
from collections import defaultdict
from functools import reduce
from operator import mul
import re

input = open('input/day10.txt', 'r').read();

class Output(object):
    def __init__(self):
        self.values = set()
    def assign(self, value):
        self.values = self.values | {value}
    def count(self):
        return len(self.values)

class Bot(Output):
    def transfer(self, low, high):
        if low:
            low.assign(min(self.values))
        if high:
            high.assign(max(self.values))
        self.values = set()

def parse_command(line):
    match = re.match('bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', line)
    if match:
        return {'cmd'         : 'transfer',
                'bot_id'      : int(match.group(1)),
                'low_type'    : match.group(2),
                'low_id'      : int(match.group(3)),
                'high_type'   : match.group(4),
                'high_id'     : int(match.group(5))}
    match = re.match('value (\d+) goes to bot (\d+)', line)
    if match:
        return {'cmd'   : 'assign',
                'value' : int(match.group(1)),
                'bot_id': int(match.group(2))}
    return None

def task1(input):
    cmds = [parse_command(line) for line in input.splitlines() if line]
    bots = defaultdict(Bot)

    assigns = [c for c in cmds if c['cmd'] == 'assign']
    for c in assigns:
        bots[c['bot_id']].assign(c['value'])

    transfers = [c for c in cmds if c['cmd'] == 'transfer']
    while transfers:
        i, c = next((i, c) for i, c in enumerate(transfers) if bots[c['bot_id']].count() == 2)
        bot = bots[c['bot_id']]
        low = bots[c['low_id']] if c['low_type'] == 'bot' else None
        high = bots[c['high_id']] if c['high_type'] == 'bot' else None
        if bot.values == {61, 17}:
            return c['bot_id']
        bot.transfer(low, high)
        del transfers[i]

def task2(input):
    cmds = [parse_command(line) for line in input.splitlines() if line]
    bots = defaultdict(Bot)
    outputs = defaultdict(Output)

    assigns = [c for c in cmds if c['cmd'] == 'assign']
    for c in assigns:
        bots[c['bot_id']].assign(c['value'])

    transfers = [c for c in cmds if c['cmd'] == 'transfer']
    while transfers:
        i, c = next((i, c) for i, c in enumerate(transfers) if bots[c['bot_id']].count() == 2)
        bot = bots[c['bot_id']]
        low = bots[c['low_id']] if c['low_type'] == 'bot' else outputs[c['low_id']]
        high = bots[c['high_id']] if c['high_type'] == 'bot' else outputs[c['high_id']]
        bot.transfer(low, high)
        del transfers[i]

    return reduce(mul, [list(outputs[i].values)[0] for i in range(3)], 1)

print(task1(input))
print(task2(input))
