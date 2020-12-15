#!/usr/bin/env python3

import sys

class Spoke():
    def __init__(self):
        self.spoke = 0
        self.when = []

    def append(self, turn):
        self.spoke += 1
        self.when.append(turn)

def increase(speaked, p, turn):
    if p in speaked:
        speaked[p].append(turn)
    else:
        spoke = Spoke()
        spoke.append(turn)
        speaked[p] = spoke
    return p

def main(args):
    n = int(args[1])
    inputs = args[2].split(',')
    speaked = {}

    for p in inputs:
        speaked[int(p)] = Spoke()

    lastSpoke = None
    for turn in range(1, n + 1):
        if len(speaked) >= turn:
            lastSpoke = int(inputs[turn - 1])
            speaked[lastSpoke].append(turn)
        elif speaked[lastSpoke].spoke == 1:
            lastSpoke = increase(speaked, 0, turn)
        else:
            p = speaked[lastSpoke]
            lastSpoke = increase(speaked, p.when[-1] - p.when[-2], turn)
        #print(f"{turn}: {lastSpoke}")
    print(f"{n}: {lastSpoke}")

if __name__ == "__main__":
    main(sys.argv)
