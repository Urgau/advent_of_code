#!/usr/bin/env python

import functools
import json
import sys

def cmp(left, right):
    match left, right:
        case int(), list():
            return cmp([left], right)
        case list(), int():
            return cmp(left, [right])
        case int(), int():
            return left - right
        case list(), list():
            for i, j in zip(left, right):
                if (r := cmp(i, j)) != 0:
                    return r
            return cmp(len(left), len(right))

if __name__ == "__main__":
    packets = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.strip()
            if line:
                packets.append(json.loads(line))

    sumIndiciesInRightOrder = 0
    for (i, (left, right)) in enumerate(zip(packets[::2], packets[1::2])):
        if cmp(left, right) <= 0:
            sumIndiciesInRightOrder += i + 1

    print("Sum of indicies for packet pairs in the right order: {}".format(sumIndiciesInRightOrder))

    dividerPackets = [[[2]], [[6]]]

    packets += dividerPackets
    packets.sort(key=functools.cmp_to_key(cmp))

    decoderKey = 1
    for (i, packet) in enumerate(packets):
        if packet in dividerPackets:
            decoderKey *= i + 1

    print("Decoder key: {}".format(decoderKey))
