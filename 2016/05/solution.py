#!/usr/bin/env python3
from itertools import count
from hashlib import md5

input = open('input.txt', 'r').read();

def task1(input):
    doorid = input.strip();
    password = ''
    for i in count():
        s = (doorid + str(i)).encode('utf-8')
        h = md5(s).hexdigest()
        if h[:5] == 5*'0':
            password += h[5]
            if len(password) == 8:
                return password

def task2(input):
    doorid = input.strip();
    password = 8*[None]
    filled = 0
    for i in count():
        s = (doorid + str(i)).encode('utf-8')
        h = md5(s).hexdigest()
        if h[:5] == 5*'0':
            try:
                index = int(h[5])
                if not password[index]:
                    password[index] = h[6]
                    filled += 1
                    if filled == 8:
                        return ''.join(password)
            except (IndexError, ValueError):
                pass

print(task1(input))
print(task2(input))
