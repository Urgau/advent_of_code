#!/usr/bin/env python

import copy
import sys

WIDTH = 750

if __name__ == "__main__":
    highestY = 0
    grid = [['.' for _ in range(WIDTH)] for _ in range(180)]
    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.strip()
            if line:
                words = line.split()
                startX, startY = None, None
                for word in words[::2]:
                    (endX, endY) = map(int, word.split(','))
                    highestY = max(highestY, endY)
                    if not startX is None and not startY is None:
                        if startX != endX:
                            if endX < startX:
                                for x in range(startX, endX - 1, -1):
                                    grid[startY][x] = '#'
                            else:
                                for x in range(startX, endX + 1, +1):
                                    grid[startY][x] = '#'
                        elif startY != endY:
                            if endY < startY:
                                for y in range(startY, endY - 1, -1):
                                    grid[y][startX] = '#'
                            else:
                                for y in range(startY, endY + 1, +1):
                                    grid[y][startX] = '#'
                        else:
                            raise
                    startX = endX
                    startY = endY

    def recur(grid, posX, posY):
        if grid[posY][posX] != '.':
            return False
        for y in range(posY, 180):
            if grid[y][posX] != '.':
                if grid[y][posX - 1] == '.':
                    return recur(grid, posX - 1, y)
                elif grid[y][posX + 1] == '.':
                    return recur(grid, posX + 1, y)
                else:
                    grid[y - 1][posX] = 'o'
                    return True
        return False

    unitsOfSandBeforeAbyysPart1 = 0
    gridPart1 = copy.deepcopy(grid)
    while recur(gridPart1, 500, 0):
        unitsOfSandBeforeAbyysPart1 += 1
    print("Units of sand before abyss (part 1): {}".format(unitsOfSandBeforeAbyysPart1))

    gridPart2 = copy.deepcopy(grid)
    for x in range(WIDTH):
        gridPart2[highestY + 2][x] = '#'

    unitsOfSandBeforeAbyysPart2 = 0
    while recur(gridPart2, 500, 0):
        unitsOfSandBeforeAbyysPart2 += 1
    print("Units of sand before abyss (part 2): {}".format(unitsOfSandBeforeAbyysPart2))

    # for y in range(180):
    #     for x in range(400, WIDTH):
    #         print(grid[y][x], end='')
    #     print()
