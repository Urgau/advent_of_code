#!/usr/bin/env python3

import itertools
import sys
import re

# https://stackoverflow.com/a/48591967
MOVEMAP = {
    'e' : ( 1,  0),
    'w' : (-1,  0),
    'se': ( 1,  1),
    'sw': ( 0,  1),
    'ne': ( 0, -1),
    'nw': (-1, -1)
}

def walk(moves):
    x, y = 0, 0

    for move in moves:
        dx, dy = MOVEMAP[move]
        x += dx
        y += dy

    return (x, y)

def evolve(positions):
    lx = min([ v[0] for v in positions ]) - 2
    ly = min([ v[1] for v in positions ]) - 2
    hx = max([ v[0] for v in positions ]) + 2
    hy = max([ v[1] for v in positions ]) + 2
    newPositions = set()

    for x, y in itertools.product(range(lx, hx), range(ly, hy)):
        n = sum([ (x + dx, y + dy) in positions for dx, dy in MOVEMAP.values() ])

        if (x, y) in positions and not (n == 0 or n > 2):
            newPositions.add((x, y))
        elif (x, y) not in positions and n == 2:
            newPositions.add((x, y))

    return newPositions

def main(args):
    positions = set()

    with open(args[1], "r") as file:
        reMoves = re.compile('|'.join(MOVEMAP.keys()))

        for line in file:
            moves = reMoves.findall(line)
            pos = walk(moves)

            if pos in positions:
                positions.remove(pos)
            else:
                positions.add(pos)

    blackSidesUp = len(positions)
    print("How many tiles are left with the black side up? {}".format(blackSidesUp))

    for _ in range(100):
        positions = evolve(positions)

    blackSidesUpAfter100Days = len(positions)
    print("How many tiles are left with the black side up after 100 days? {}".format(blackSidesUpAfter100Days))

if __name__ == "__main__":
    main(sys.argv)
