#!/usr/bin/env python

import sys

STEPS = 100
SIZE = 10

if __name__ == "__main__":
    matrix = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            matrix.append([int(a) for a in line.strip()])

    step = 1
    totalFlashes = 0
    while True:
        expanded = []
        flashes = []

        for y in range(SIZE):
            for x in range(SIZE):
                matrix[y][x] += 1
                if matrix[y][x] > 9:
                    def expand(x, y):
                        if (x, y) in expanded:
                            return
                        expanded.append((x, y))
                        for yAround in range(-1, 1 + 1):
                            for xAround in range(-1, 1 + 1):
                                if xAround == 0 and yAround == 0:
                                    continue
                                if y + yAround >= 0 and y + yAround < SIZE and \
                                    x + xAround >= 0 and x + xAround < SIZE:
                                    matrix[y + yAround][x + xAround] += 1
                                    if matrix[y + yAround][x + xAround] > 9:
                                        expand(x + xAround, y + yAround)

                    expand(x, y)

        for y in range(SIZE):
            for x in range(SIZE):
                if matrix[y][x] > 9:
                    flashes.append((x, y))
                    matrix[y][x] = 0

        totalFlashes += len(flashes)
        if step == 100:
            print(f"Total flashes: {totalFlashes}")
        if len(flashes) == 10 * 10:
            print(f"All flash simultaneously: step={step}")
            break
        step += 1

