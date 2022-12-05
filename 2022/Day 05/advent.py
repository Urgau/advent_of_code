#!/usr/bin/env python

import sys

if __name__ == "__main__":
    stacks = []
    moves = []
    with open(sys.argv[1], "r") as file:
        should_be_moves = False
        for line in file:
            if not line.strip():
                should_be_moves = True
            elif should_be_moves:
                words = line.strip().split()
                moves.append((
                    int(words[1]),
                    int(words[3]),
                    int(words[5])
                ))
            elif line[1] != "1":
                stackI = 0
                for (i, c) in enumerate(line):
                    if (i - 1) % 4 == 0:
                        if len(stacks) == stackI:
                            stacks.append([])
                        if c != ' ':
                            stacks[stackI].append(c)
                        stackI += 1

    stacksPart1 = stacks
    stacksPart2 = [[i for i in row] for row in stacks]
    for (how_many, from_pos, to_pos) in moves:
        for _ in range(how_many):
            item = stacksPart1[from_pos - 1].pop(0)
            stacksPart1[to_pos - 1].insert(0, item)
    for (how_many, from_pos, to_pos) in moves:
        for i in range(how_many):
            item = stacksPart2[from_pos - 1].pop(0)
            stacksPart2[to_pos - 1].insert(i, item)

    msgPart1 = ""
    msgPart2 = ""
    for stack in stacksPart1:
        if len(stack) >= 1:
            msgPart1 += stack[0]
    for stack in stacksPart2:
        if len(stack) >= 1:
            msgPart2 += stack[0]

    print("Message part1: {}".format(msgPart1))
    print("Message part2: {}".format(msgPart2))

