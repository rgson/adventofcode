#!/usr/bin/env python3
import re

input = open('input.txt', 'r').read();

def parse_input(input):
    lines = [line for line in input.splitlines() if line]
    matches = [re.match('([a-z\-]+)(\d+)\[(\w+)\]', line) for line in lines]
    groups = [match.group(1, 2, 3) for match in matches]
    return groups

def task1(input):
    text = ''.join(input.split())
    output = ''
    match = re.search('(\((\d+)x(\d+)\))', text)
    while match:
        marker_start, marker_end = match.span(1)
        repeat_len, repeat_times = [int(x) for x in match.group(2, 3)]
        output += text[:marker_start]
        output += text[marker_end:(marker_end+repeat_len)] * repeat_times
        text = text[(marker_end+repeat_len):]
        match = re.search('(\((\d+)x(\d+)\))', text)
    output += text
    return len(output)

def task2(input):
    text = ''.join(input.split())
    length = 0
    match = re.search('(\((\d+)x(\d+)\))', text)
    while match:
        marker_start, marker_end = match.span(1)
        repeat_len, repeat_times = [int(x) for x in match.group(2, 3)]
        length += marker_start
        length += task2(text[marker_end:(marker_end+repeat_len)]) * repeat_times
        text = text[(marker_end+repeat_len):]
        match = re.search('(\((\d+)x(\d+)\))', text)
    length += len(text)
    return length

print(task1(input))
print(task2(input))
