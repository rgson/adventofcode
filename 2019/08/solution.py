#!/usr/bin/python3

width, height = 25, 6

def group_layers(data, width, height):
    image_size = width * height
    for i in range(0, len(data), image_size):
        yield data[i:i+image_size]

def count_occurrences(iterable, elem):
    return sum(i == elem for i in iterable)

def decode_image(data, width, height):
    for pixel in zip(*group_layers(data, width, height)):
        yield next(value for value in pixel if value != '2')

def draw_image(image, width):
    color = ('X', '_', ' ')
    for i, pixel in enumerate(image):
        yield color[int(pixel)]
        if (i+1) % width == 0:
            yield '\n'

def task1(input):
    image_layers = group_layers(input.strip(), width, height)
    layer = min(image_layers, key=lambda x: count_occurrences(x, '0'))
    return count_occurrences(layer, '1') * count_occurrences(layer, '2')

def task2(input):
    decoded = ''.join(decode_image(input.strip(), width, height))
    return ''.join(draw_image(decoded, width))

input = open('input.txt', 'r').read()
print(task1(input))
print(task2(input))
