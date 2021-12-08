#!/usr/bin/env python

import collections
import sys

class Entry:
    def __init__(self, paterns, outputs):
        self.paterns = paterns
        self.outputs = outputs

if __name__ == "__main__":
    entries = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            a = line.strip().split(" | ")
            entries.append(Entry(a[0].split(' '), a[1].split(' ')))

    c = collections.Counter()
    for entry in entries:
        for output in entry.outputs:
            c.update({len(output): 1})

    print(f"Part 1: {c[2] + c[3] + c[4] + c[7]}")

    # values = []
    #
    # c = collections.Counter()
    # for entry in entries:
    #     for patern in entry.paterns:
    #         c.update(list(patern))
    #
    # normalization = {}
    # for entry in entries:
    #     for patern in entry.paterns:
    #         new = ""
    #         for char in patern:
    #             new += str(c[char])
    #         print(new)
    #
    # print(c)
    #
    # print(f"Part 2: {sum(values)}")
