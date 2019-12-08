#!/usr/bin/env python3
import re
from collections import Counter
from operator import itemgetter

input = open('input.txt', 'r').read();

def parse_input(input):
    lines = [line for line in input.splitlines() if line]
    matches = [re.match('([a-z\-]+)(\d+)\[(\w+)\]', line) for line in lines]
    groups = [match.group(1, 2, 3) for match in matches]
    return groups

def task1(input):
    groups = parse_input(input)
    sectorsum = 0
    for name, sector, checksum in groups:
        counter = Counter(name.replace('-', ''))
        alphabetized = sorted(counter.items(), key=itemgetter(0))
        ordered = sorted(alphabetized, key=itemgetter(1), reverse=True)
        firstfive = ''.join([a[0] for a in ordered[:5]])
        sectorsum += int(sector) if checksum == firstfive else 0
    return sectorsum

def task2(input):
    groups = parse_input(input)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for name, sector, checksum in groups:
        shift = int(sector) % len(alphabet)
        shifted = (2 * alphabet)[shift:shift+len(alphabet)]
        translation = str.maketrans(alphabet + '-', shifted + ' ')
        decrypted = name.translate(translation)
        if re.match('north|pole|object', decrypted):
            return sector

print(task1(input))
print(task2(input))
