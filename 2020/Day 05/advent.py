#!/usr/bin/env python3

import math
import sys

class Seat:
    def __init__(self, boardingPass):
        self.boardingPass = boardingPass
        self.row = self._decode(boardingPass[:7], 0, 127, 'F', 'B')
        self.column = self._decode(boardingPass[7:], 0, 7, 'L', 'R')
        self.id = self.row * 8 + self.column

    def __str__(self):
        return "Seat({}, row: {}, column: {}, id: {})".format(self.boardingPass, self.row, self.column, self.id)

    def __eq__(self, other):
        return self.id == other

    def __hash__(self):
        return self.id

    def _decode(self, input, rangeStart, rangeEnd, lowerHalf, upperHalf):
        for c in input:
            if c == lowerHalf:
                rangeEnd = int(math.floor((rangeEnd - rangeStart) / 2 + rangeStart))
            elif c == upperHalf:
                rangeStart = int(math.ceil(rangeEnd - (rangeEnd - rangeStart) / 2))
            else:
                raise Exception("unkown {} character".format(c))
        if rangeStart != rangeEnd:
            raise Exception("rangeStart {} and rangeEnd {} are not equal".format(rangeStart, rangeEnd))
        return rangeStart

def main():
    seats = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            seats.append(Seat(line.strip()))
    print("Max: {}".format(max(seats, key = lambda k: k.id)))

    all = list(range(100, 800))
    missings = list(set(all).difference(seats))
    print("Missing(s): {}".format(missings))

if __name__ == "__main__":
    main()
