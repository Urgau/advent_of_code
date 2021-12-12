#!/usr/bin/env python

import collections
import sys

def have_2_lower_components(path):
    counter = collections.Counter(path)

    for a in counter:
        if a.islower() and counter[a] >= 2:
            return True
    return False

if __name__ == "__main__":
    caves = {}
    with open(sys.argv[1], "r") as file:
        for line in file:
            words = line.strip().split("-")
            if words[0] not in caves:
                caves[words[0]] = [words[1]]
            else:
                caves[words[0]].append(words[1])
            if words[1] not in caves:
                caves[words[1]] = [words[0]]
            else:
                caves[words[1]].append(words[0])

    paths = []
    def recur(path):
        last = path[-1]

        if last == "end":
            paths.append(path)
            return

        last_cave = caves[last]
        for next in last_cave:
            if next == "start":
                continue
            if next.islower() and (next in path and have_2_lower_components(path)):
                continue
            new = path + [next]
            recur(new)

    recur(["start"])

    print(f"Part 1: {sum(1 if not have_2_lower_components(path) else 0 for path in paths)}")
    print(f"Part 2: {len(paths)}")
