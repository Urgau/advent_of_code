#!/usr/bin/env python

import sys

if __name__ == "__main__":
    moves = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.strip()
            if not not line:
                moves.append(line.split())

    totalScorePart1 = 0
    totalScorePart2 = 0
    for move in moves:
        opponent = ord(move[0]) - ord("A")
        us = ord(move[1]) - ord("X")

        totalScorePart1 += (us + 1) + 3 * ((us - opponent + 1) % 3)
        totalScorePart2 += (us * 3) + (us + opponent - 1) % 3 + 1

    print(f"totalScorePart1: {totalScorePart1}")
    print(f"totalScorePart2: {totalScorePart2}")
