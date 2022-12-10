#!/usr/bin/env python

import sys

NOOP=1
ADDX=2

def foo(cycles):
    if cycles == 20 or cycles == 60 or cycles == 100 or \
            cycles == 140 or cycles == 180 or cycles == 220:
        return True
    return False

if __name__ == "__main__":
    insts = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.strip()
            if line:
                words = line.split()
                if words[0] == "noop":
                    insts.append((NOOP, None))
                elif words[0] == "addx":
                    insts.append((ADDX, int(words[1])))
                else:
                    raise words

    regX = 1
    cycles = 0
    sumSignal = 0
    sprite = []
    spriteRow = ""
    spritePositionStart = 0
    spritePositionEnd = 3

    for (inst, val) in insts:
        if len(spriteRow) + 1 >= spritePositionStart and \
                len(spriteRow) + 1 < spritePositionEnd:
            spriteRow += '#'
        else:
            spriteRow += '.'
        cycles += 1

        if foo(cycles):
            sumSignal += cycles * regX
        if cycles % 40 == 0:
            sprite.append(spriteRow)
            spriteRow = ""

        if inst == ADDX:
            if len(spriteRow) + 1 >= spritePositionStart and \
                    len(spriteRow) + 1 < spritePositionEnd:
                spriteRow += '#'
            else:
                spriteRow += '.'
            cycles += 1

            regX += val
            spritePositionStart = regX
            spritePositionEnd = regX + 3

            if foo(cycles):
                sumSignal += cycles * regX
            if cycles % 40 == 0:
                sprite.append(spriteRow)
                spriteRow = ""

    print("Sum signal at specific interval: {}".format(sumSignal))
    print("\nSprite:")
    for row in sprite:
        print(row)

