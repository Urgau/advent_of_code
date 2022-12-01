#!/usr/bin/env python

import sys

if __name__ == "__main__":
    elfs = []
    with open(sys.argv[1], "r") as file:
        calories = []
        for line in file:
            line = line.strip()
            if not line:
                elfs.append(calories)
                calories = []
            else:
                calories.append(int(line))
        elfs.append(calories)

    sumCaloriesByElf = [sum(calories) for calories in elfs]

    maxCaloriesHelpByOneElf = max(sumCaloriesByElf)
    print("maxCaloriesHelpByOneElf: {}".format(maxCaloriesHelpByOneElf))

    sumCaloriesByElf.sort()
    sumCaloriesTopThreeElfs = sum(sumCaloriesByElf[-3:])
    print("sumCaloriesTopThreeElfs: {}".format(sumCaloriesTopThreeElfs))
