#!/usr/bin/env python

import sys

allowDiagonal = True
sizeOfMatrix = 1000

if __name__ == "__main__":
    lines = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            words = line.split(" -> ")
            nums = words[0].split(",")
            start = (int(nums[0]), int(nums[1]))
            nums = words[1].split(",")
            end = (int(nums[0]), int(nums[1]))
            lines.append((start, end))

    matrix = [[0 for _ in range(sizeOfMatrix)] for _ in range(sizeOfMatrix)]

    for (x1, y1), (x2, y2) in lines:
        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    matrix[y][x] += 1
        elif allowDiagonal:
            for x, y in zip(
                    range(x1, x2 + (-1 if x1 > x2 else 1), -1 if x1 > x2 else 1),
                    range(y1, y2 + (-1 if y1 > y2 else 1), -1 if y1 > y2 else 1)):
                matrix[y][x] += 1

    pointsWhereOverlap = 0
    for l in matrix:
        for v in l:
            if v >= 2:
                pointsWhereOverlap += 1

    print(f"At how many points do at least two lines overlap? {pointsWhereOverlap}")
