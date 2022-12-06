#!/usr/bin/env python

import sys

def first_variable_lenght_marker(bitstream, lenght):
    firstMarkerPos = None
    for i in range(0, len(bitstream) - lenght):
        text = bitstream[i:i+lenght]

        foundDup = False
        for c in text:
            if text.count(c) > 1:
                foundDup = True
                break
        if not foundDup:
            firstMarkerPos = i + lenght
            break
    return firstMarkerPos

if __name__ == "__main__":
    bitstream = None
    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.strip()
            if line:
                bitstream = line

    first4MarkerPos = first_variable_lenght_marker(bitstream, 4)
    first14MarkerPos = first_variable_lenght_marker(bitstream, 14)

    print("First 4 maker pos: {}".format(first4MarkerPos))
    print("First 14 maker pos: {}".format(first14MarkerPos))
