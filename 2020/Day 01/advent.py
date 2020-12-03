#!/usr/bin/env python

import sys

if __name__ == "__main__":
    numbers = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            numbers.append(int(line))
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            a1 = numbers[i]
            a2 = numbers[j]
            if i != j and a1 + a2 == 2020:
                print("WIN: {} + {}: {}".format(a1, a2, a1 * a2))
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            for k in range(0, len(numbers)):
                a1 = numbers[i]
                a2 = numbers[j]
                a3 = numbers[k]
                if i != j and j != k and a1 + a2 + a3 == 2020:
                    print("WIN: {} + {} + {}: {}".format(a1, a2, a3, a1 * a2 * a3))
