#!/usr/bin/env python

import sys

def count_until_less(l, x):
    tmp = 0
    for a in l:
        tmp += 1
        if a >= x:
            break
    return tmp

if __name__ == "__main__":
    grid = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.strip()
            if line:
                grid.append(list(map(int, line)))

    w = len(grid[0])
    h = len(grid)

    scenicScores = []
    treesVisible = w * 2 + (h - 2) * 2
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            leftTrees = [grid[y][xTmp] for xTmp in range(0, x)]
            rightTrees = [grid[y][xTmp] for xTmp in range(x + 1, w)]
            upTrees = [grid[yTmp][x] for yTmp in range(0, y)]
            downTrees = [grid[yTmp][x] for yTmp in range(y + 1, h)]

            currentTree = grid[y][x]
            leftTrees.reverse()
            upTrees.reverse()

            if max(leftTrees) < currentTree or \
                    max(upTrees) < currentTree or \
                    max(rightTrees) < currentTree or \
                    max(downTrees) < currentTree:
                treesVisible += 1

            score = count_until_less(leftTrees, currentTree) * \
                count_until_less(upTrees, currentTree) * \
                count_until_less(rightTrees, currentTree) * \
                count_until_less(downTrees, currentTree)
            scenicScores.append(score)

    print("Trees visible: {}".format(treesVisible))
    print("Max scenic score: {}".format(max(scenicScores)))

