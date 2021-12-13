#!/usr/bin/env python

import sys

if __name__ == "__main__":
    dots = []
    with open(sys.argv[1], "r") as file:
        instructions = False
        for line in file:
            line = line.strip()
            if not line:
                instructions = True
            elif not instructions:
                nums = line.split(',')
                dots.append((int(nums[0]), int(nums[1])))
            else:
                line = line.strip("fold along ")
                words = line.split("=")
                n = int(words[1])

                if words[0] == "y":
                    newDots = []
                    for x, y in dots:
                        if y <= n:
                            newDots.append((x, y))
                        else:
                            newDots.append((x, n - (y - n)))
                elif words[0] == "x":
                    newDots = []
                    for x, y in dots:
                        if x <= n:
                            newDots.append((x, y))
                        else:
                            newDots.append((n - (x - n), y))
                else:
                    raise words[0]

                dots = set(newDots)
                print(len(dots))
    # print(dots)

    for y in range(6):
        for x in range(50):
            if (x, y) in dots:
                print("#", end="")
            else:
                print(".", end="")
        print()
