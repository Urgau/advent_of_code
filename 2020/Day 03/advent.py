#!/usr/bin/env python

import math
import sys

if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        lines = [line.rstrip() for line in file]
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        slopesTrees = []
        slopesOpens = []

        for slp in range(len(slopes)):
            (X, Y) = (0, 0)
            (Xd, Yd) = slopes[slp]
            Ymax = len(lines)
            Xmax = len(lines[0])
            trees = 0
            opens = 0

            X += Xd
            Y += Yd
            while Y < Ymax:
                if lines[Y][X] == '#':
                    trees += 1
                else:
                    opens += 1
                X += Xd
                X = (X % Xmax)
                Y += Yd
            slopesTrees.append(trees)
            slopesOpens.append(opens)
            print("{} => Trees: {} | Opens: {}".format(slopes[slp], trees, opens))
        print("Total trees: {} | Total opens: {}".format(math.prod(slopesTrees), math.prod(slopesOpens)))
