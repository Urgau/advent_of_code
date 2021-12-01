#!/usr/bin/env python

import sys

if __name__ == "__main__":
    numbers = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            numbers.append(int(line))

    numberOfIncrease = 0
    for prev, curr in zip(numbers, numbers[1:]):
        if curr > prev:
            numberOfIncrease += 1
    print(f"numberOfIncrease: {numberOfIncrease}")


    numberOfIncreaseBy3Sum = 0
    for aPos, bPos in zip(range(0, len(numbers), 1), range(1, len(numbers), 1)):
        if sum(numbers[bPos:bPos+3]) > sum(numbers[aPos:aPos+3]):
            numberOfIncreaseBy3Sum += 1
    print(f"numberOfIncreaseBy3Sum: {numberOfIncreaseBy3Sum}")
