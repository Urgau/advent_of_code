#!/usr/bin/env python3

import sys

def countOccupiedNeightboursTrace(seats, xPos, yPos, xDir, yDir):
    x = xPos + xDir
    y = yPos + yDir
    while 0 <= x < len(seats[0]) and 0 <= y < len(seats):
        if seats[y][x] == "#":
            return 1
        if seats[y][x] == "L":
            return 0
        x += xDir
        y += yDir
    return 0

def countOccupiedNeightbours(seats, xPos, yPos):
    occupied = 0
    for yDir in range(-1, 1 + 1):
        for xDir in range(-1, 1 + 1):
            if xDir == 0 and yDir == 0:
                continue
            occupied += countOccupiedNeightboursTrace(seats, xPos, yPos, xDir, yDir)
    return occupied

def countOccupiedNearest(seats, xPos, yPos):
    occupied = 0
    for yDir in range(-1, 1 + 1):
        for xDir in range(-1, 1 + 1):
            if xDir == 0 and yDir == 0:
                continue
            x, y = xPos + xDir, yPos + yDir
            if y < 0 or y >= len(seats) or x < 0 or x >= len(seats[0]):
                continue
            if seats[y][x] == "#":
                occupied += 1
    return occupied

def simulate(seatsIn, maxOccupied, countOccupied):
    seatsOut = []
    changed = False
    for y in range(len(seatsIn)):
        seatsOutLine = []
        for x in range(len(seatsIn[0])):
            if seatsIn[y][x] == 'L' and countOccupied(seatsIn, x, y) == 0:
                seatsOutLine.append('#')
                changed = True
            elif seatsIn[y][x] == '#' and countOccupied(seatsIn, x, y) >= maxOccupied:
                seatsOutLine.append('L')
                changed = True
            else:
                seatsOutLine.append(seatsIn[y][x])
        seatsOut.append(seatsOutLine)
    return (changed, seatsOut)

def simuateUntilStable(seats, maxOccupied, countOccupied):
    changed = True
    while changed == True:
        changed, seats = simulate(seats, maxOccupied, countOccupied)
    return seats

def main(args):
    with open(args[1], "r") as file:
        seats = []
        for line in file:
            seats.append(line.strip())

        seatsNearestStable = simuateUntilStable(seats, 4, countOccupiedNearest)
        print("Neartest: How many seats end up occupied? {}".format(sum(line.count('#') for line in seatsNearestStable)))

        seatsNeightboursStable = simuateUntilStable(seats, 5, countOccupiedNeightbours)
        print("Neightbours: How many seats end up occupied? {}".format(sum(line.count('#') for line in seatsNeightboursStable)))

if __name__ == "__main__":
    main(sys.argv)
