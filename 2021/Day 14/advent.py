#!/usr/bin/env python

import collections
import sys

if __name__ == "__main__":
    rules = {}
    # template = ""
    template = {}
    counter = collections.Counter()
    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.strip()
            if not template:
                # template = line
                for c1, c2 in zip(line[:], line[1:]):
                    if not c1 + c2 in template:
                        template[c1 + c2] = 1
                    else:
                        template[c1 + c2] += 1
                counter.update(line)
            elif line:
                words = line.split(" -> ")
                rules[words[0]] = words[1]

    for step in range(40):
        newTemplate = {}
        for a in template:
            b = rules[a]
            left = a[0] + b
            right = b + a[-1]
            if not left in newTemplate:
                newTemplate[left] = template[a]
            else:
                newTemplate[left] += template[a]
            if not right in newTemplate:
                newTemplate[right] = template[a]
            else:
                newTemplate[right] += template[a]
            counter.update({b: template[a]})
        template = newTemplate
        commons = counter.most_common()
        print(f"[{step+1}]: max(template) - min(template): {commons[0][1] - commons[-1][1]}")
