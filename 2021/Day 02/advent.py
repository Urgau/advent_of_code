#!/usr/bin/env python

import sys

if __name__ == "__main__":
    operations = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            elems = line.strip().split()
            operations.append((elems[0], int(elems[1])))

    horizontal, depth = 0, 0
    for cmd, val in operations:
        if cmd == "forward":
            horizontal += val
        elif cmd == "down":
            depth += val
        elif cmd == "up":
            depth -= val
        else:
            raise "error"

    print(f"Part1: horizontal: {horizontal} - depth: {depth} - result: {horizontal * depth}")

    horizontal, depth, aim = 0, 0, 0
    for cmd, val in operations:
        if cmd == "forward":
            horizontal += val
            depth += aim * val
        elif cmd == "down":
            aim += val
        elif cmd == "up":
            aim -= val
        else:
            raise "error"

    print(f"Part2: horizontal: {horizontal} - depth: {depth} - aim: {aim} - result: {horizontal * depth}")

