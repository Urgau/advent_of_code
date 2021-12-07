#!/usr/bin/env python

import statistics
import sys

if __name__ == "__main__":
    numbers = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            numbers = [int(a) for a in line.strip().split(',')]

    margin = 40
    meanNumbers = int(statistics.mean(numbers))
    medianNumbers = int(statistics.median(numbers))

    costs = []
    for dest in range(medianNumbers - margin, medianNumbers + margin):
        cost = 0
        for n in numbers:
            cost += abs(n - dest)
        # print(dest, cost)
        costs.append(cost)

    print(f"Part 1: {min(costs)}")

    costs = []
    for dest in range(meanNumbers - margin, meanNumbers + margin):
        cost = 0
        for n in numbers:
            cost += sum(a for a in range(abs(n - dest) + 1))
        # print(dest, cost)
        costs.append(cost)

    print(f"Part 2: {min(costs)}")
