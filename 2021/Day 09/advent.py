#!/usr/bin/env python

import sys

# https://stackoverflow.com/a/595391
def prod(iterable):
    p = 1
    for n in iterable:
        p *= n
    return p

if __name__ == "__main__":
    matrix = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            matrix.append([int(a) for a in line.strip()])

    lowPoints = []
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            adjacentPoints = []
            if x >= 0 and x + 1 < len(matrix[y]):
                adjacentPoints.append(matrix[y][x + 1])
            if x - 1 >= 0:
                adjacentPoints.append(matrix[y][x - 1])
            if y >= 0 and y + 1 < len(matrix):
                adjacentPoints.append(matrix[y + 1][x])
            if y - 1 >= 0:
                adjacentPoints.append(matrix[y - 1][x])
            if matrix[y][x] < min(adjacentPoints):
                lowPoints.append((matrix[y][x], x, y))

    print(f"Part 1: {sum(a + 1 for a, _, _ in lowPoints)}")

    basins = []
    for _, xLowPoint, yLowPoint in lowPoints:
        points = []

        def recur(x, y):
            if y < 0 or y >= len(matrix):
                return
            if x < 0 or x >= len(matrix[0]):
                return
            if matrix[y][x] >= 9:
                return
            if (x, y) in points:
                return
            points.append((x, y))
            recur(x, y - 1)
            recur(x, y + 1)
            recur(x - 1, y)
            recur(x + 1, y)

        recur(xLowPoint, yLowPoint)
        basins.append(points)
    basins.sort(key = len)

    print(f"Part 2: {prod(len(b) for b in basins[-3:])}")
