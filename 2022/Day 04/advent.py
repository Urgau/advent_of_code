#!/usr/bin/env python

import sys

if __name__ == "__main__":
    pairs = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.strip()
            if line:
                ranges = line.split(',')
                range0 = ranges[0].split('-')
                range1 = ranges[1].split('-')
                pairs.append(
                    (
                        (int(range0[0]), int(range0[1])),
                        (int(range1[0]), int(range1[1]))
                    )
                )

    totalOverlap = 0
    totalCompleteContains = 0
    for ((range0_0, range0_1), (range1_0, range1_1)) in pairs:
        # Complete contains
        if range0_0 >= range1_0 and range0_1 <= range1_1:
            totalCompleteContains += 1
        elif range1_0 >= range0_0 and range1_1 <= range0_1:
            totalCompleteContains += 1

        # Overlap
        if range0_0 >= range1_0 and range0_0 <= range1_1:
            totalOverlap += 1
        elif range0_1 >= range1_0 and range0_1 <= range1_1:
            totalOverlap += 1
        elif range1_0 >= range0_0 and range1_0 <= range0_1:
            totalOverlap += 1
        elif range1_1 >= range0_0 and range1_1 <= range0_1:
            totalOverlap += 1

    print("Total pair compete contains: {}".format(totalCompleteContains))
    print("Total pair overlap: {}".format(totalOverlap))

