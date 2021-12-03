#!/usr/bin/env python

import sys

def bitCounts(input, pos):
    return len(list(filter(lambda x: x[pos] == '1', input)))

def filterCandidates(fn, candidates):
    n = 0
    while len(candidates) > 1:
        if fn(bitCounts(candidates, n)*2, len(candidates)):
            candidates = list(filter(lambda x: x[n] == '1', candidates))
        else:
            candidates = list(filter(lambda x: x[n] == '0', candidates))
        n += 1
    return int(candidates[0], 2)

if __name__ == "__main__":
    bits = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            bits.append(line.strip())

    counts = [[0, 0] for _ in range(len(bits[0]))]
    for b in bits:
        for i, byte in enumerate(b):
            if byte == "0":
                counts[i][0] += 1
            else:
                counts[i][1] += 1

    epsilon, gamma = "", ""
    for count in counts:
        if count[0] < count[1]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    epsilon = int(epsilon, 2)
    gamma = int(gamma, 2)

    oxygen = filterCandidates(lambda a, b: a >= b, bits)
    co2 = filterCandidates(lambda a, b: a < b, bits)

    print(f"epsilon: {epsilon} - gamma: {gamma} - r: {epsilon * gamma}")
    print(f"oxygen: {oxygen} - co2: {co2} - r: {oxygen * co2}")
