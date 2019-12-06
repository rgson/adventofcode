#!/usr/bin/python3

from collections import defaultdict
import heapq

def parse_orbits(input):
    for line in input.splitlines():
        yield tuple(line.strip().split(')'))

def map_satellite_to_body(orbits):
    return {satellite: body for body, satellite in orbits}

def distance_to_center(orbit_map, satellite):
    body = orbit_map.get(satellite)
    return 0 if not body else 1 + distance_to_center(orbit_map, body)

def adjacency_matrix(orbits):
    matrix = defaultdict(lambda: defaultdict(lambda: False))
    for body, satellite in orbits:
        matrix[body][satellite] = matrix[satellite][body] = True
    return matrix

def shortest_path(matrix, source, target):
    queue, seen = [(0, source)], {source}
    while queue:
        distance, node = heapq.heappop(queue)
        if node == target:
            return distance
        for neighbor in matrix[node]:
            if neighbor not in seen:
                heapq.heappush(queue, (distance+1, neighbor))
                seen.add(neighbor)

def task1(input):
    orbit_map = map_satellite_to_body(parse_orbits(input))
    return sum(distance_to_center(orbit_map, x) for x in orbit_map)

def task2(input):
    matrix = adjacency_matrix(parse_orbits(input))
    return shortest_path(matrix, 'YOU', 'SAN') - 2

input = open('input.txt', 'r').read()
print(task1(input))
print(task2(input))
