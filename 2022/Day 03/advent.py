#!/usr/bin/env python

import sys

if __name__ == "__main__":
    rusksacks = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.strip()
            if line:
                line = list(line)
                l = len(line) // 2
                rusksacks.append([line[:l], line[l:]])

    totalErrors = 0
    for rusksack in rusksacks:
        commons = list(set(rusksack[0]).intersection(rusksack[1]))
        common_0 = commons[0]

        if common_0 >= 'a' and common_0 <= 'z':
            totalErrors += ord(common_0) - ord('a') + 1
        elif common_0 >= 'A' and common_0 <= 'Z':
            totalErrors += ord(common_0) - ord('A') + 1 + 26
    print("Sum of errors: {}".format(totalErrors))

    totalPriorities = 0
    for i in range(0, len(rusksacks), 3):
        r0 = set(sum(rusksacks[i + 0], []))
        r1 = set(sum(rusksacks[i + 1], []))
        r2 = set(sum(rusksacks[i + 2], []))

        commons = list(r0 & r1 & r2)
        common_0 = commons[0]

        if common_0 >= 'a' and common_0 <= 'z':
            totalPriorities += ord(common_0) - ord('a') + 1
        elif common_0 >= 'A' and common_0 <= 'Z':
            totalPriorities += ord(common_0) - ord('A') + 1 + 26
    print("Sum of priorities: {}".format(totalPriorities))
