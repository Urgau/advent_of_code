#!/usr/bin/env python3

import sys

def applyMask(val, mask):
    result = ""
    val = format(val, 'b').zfill(36)
    for (a, b) in zip(val, mask):
        result += b if b != "X" else a
    return int(result, 2)

def binPermutations(n):
    for i in range(1 << n):
        s = bin(i)[2:]
        s = '0' * (n - len(s)) + s
        yield list(s)

def adresses(pos, mask):
    addrWithMask = ""
    posBin = format(pos, 'b').zfill(36)
    for (a, b) in zip(posBin, mask):
        addrWithMask += b if b != '0' else a
    Xs = addrWithMask.count('X')
    for per in binPermutations(Xs):
        index = 0
        addr = ""
        for c in addrWithMask:
            if c == 'X':
                addr += per[index]
                index += 1
            else:
                addr += c
        yield int(addr, 2)

def main(args):
    with open(args[1], "r") as file:
        masks = []
        memPart1 = {}
        memPart2 = {}

        for line in file:
            if line.startswith("mask"):
                masks.append(line[len("mask = "):])
            elif line.startswith("mem"):
                addr = int(line[line.index("[") + 1:line.index("]")])
                val = int(line[line.index("=") + 2:])

                memPart1[addr] = applyMask(val, masks[-1])
                for addr in adresses(addr, masks[-1]):
                    memPart2[addr] = val

        sumPart1 = sum(memPart1.values())
        print("What is the sum of all values left in memory after it completes? {}".format(sumPart1))

        sumPart2 = sum(memPart2.values())
        print("What is the sum of all values left in memory after it completes? {}".format(sumPart2))

if __name__ == "__main__":
    main(sys.argv)
