#!/usr/bin/env python

import sys

if __name__ == "__main__":
    states = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    with open(sys.argv[1], "r") as file:
        for line in file:
            numbers = line.strip().split(',')
            for a in numbers:
                states[int(a)] += 1

    for d in range(256):
        newStates = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
        for key, val in states.items():
            if key == 0:
                newStates[8] = val
                newStates[6] = val
            else:
                newStates[key - 1] += val
        states = newStates
        print(f"After {d+1} days: {sum(a for a in states.values())}")
