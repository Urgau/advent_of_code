#!/usr/bin/env python

import sys

X = 0
Y = 1

if __name__ == "__main__":
    target_area = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            components = line.strip().lstrip("target area: ").split(",")
            for component in components:
                component = component.strip()
                ws = component.split("=")
                nb = ws[1].split("..")
                target_area.append((int(nb[0]), int(nb[1])))

    def calculus(velocity):
        velX, velY = velocity[X], velocity[Y]
        positions = []

        x, y = velX, velY
        while True:
            positions.append((x, y))
            if x >= target_area[X][0] and x <= target_area[X][1] and \
                    y >= target_area[Y][0] and y <= target_area[Y][1]:
                return positions
            # print(x, y)
            if x >= target_area[X][1] or y <= min(target_area[Y]):
                return None
            if velX != 0:
                velX += -1 if velX > 0 else 1
            velY -= 1
            x += velX
            y += velY

    valid = 0
    maxGlobalP = (0, 0)
    for x in range(-100, 300):
        for y in range(-500, 1000):
            p = calculus((x, y))
            if not p is None:
                valid += 1
                maxP = max(p, key=lambda item: item[1])
                maxGlobalP = max(maxGlobalP, maxP, key=lambda item: item[1])

    print(f"Part 1: {maxGlobalP}")
    print(f"Part 2: {valid}")
