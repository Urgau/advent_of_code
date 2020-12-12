#!/usr/bin/env python3

import math
import sys

class Coord:
    def __init__(self, east=0, north=0):
        self.east = east
        self.north = north
        self.dir = (1, 0)

    def moveNorth(self, val):
        self.north += val

    def moveSouth(self, val):
        self.north -= val

    def moveEast(self, val):
        self.east += val

    def moveWest(self, val):
        self.east -= val

    def left(self, deg):
        self.rotateDir(math.radians(deg))

    def right(self, deg):
        self.rotateDir(math.radians(-deg))

    def moveLeft(self, deg):
        self.rotatePos(math.radians(deg))

    def moveRight(self, deg):
        self.rotatePos(math.radians(-deg))

    def forward(self, val):
        dirX, dirY = self.dir
        if dirX == -1 and dirY == 0:
            self.moveWest(val)
        elif dirX == 0 and dirY == 1:
            self.moveNorth(val)
        elif dirX == 1 and dirY == 0:
            self.moveEast(val)
        elif dirX == 0 and dirY == -1:
            self.moveSouth(val)
        else:
            raise Exception("Unknow dir: {}".format(self.dir))

    def rotatePos(self, rad):
        east = self.east
        north = self.north
        self.east = round(math.cos(rad) * east - math.sin(rad) * north)
        self.north = round(math.sin(rad) * east + math.cos(rad) * north)

    def rotateDir(self, rad):
        dirX, dirY = self.dir
        self.dir = (
            round(math.cos(rad) * dirX - math.sin(rad) * dirY),
            round(math.sin(rad) * dirX + math.cos(rad) * dirY)
        )

    def manhattanDistance(self):
        return abs(self.north) + abs(self.east)

def forwardShip(ship, waypoint, val):
    ship.north += waypoint.north * val
    ship.east += waypoint.east * val

def main(args):
    with open(args[1], "r") as file:
        shipPart1 = Coord()
        cmdsPart1 = {
            "N": shipPart1.moveNorth,
            "S": shipPart1.moveSouth,
            "E": shipPart1.moveEast,
            "W": shipPart1.moveWest,
            "L": shipPart1.left,
            "R": shipPart1.right,
            "F": shipPart1.forward
        }

        shipPart2 = Coord()
        waypoint = Coord(10, 1)
        cmdsPart2 = {
            "N": waypoint.moveNorth,
            "S": waypoint.moveSouth,
            "E": waypoint.moveEast,
            "W": waypoint.moveWest,
            "L": waypoint.moveLeft,
            "R": waypoint.moveRight,
            "F": lambda val: forwardShip(shipPart2, waypoint, val)
        }

        for line in file:
            cmd = line[0]
            val = int(line[1:])
            cmdsPart1[cmd](val)
            cmdsPart2[cmd](val)

        print("What is the Manhattan distance for part1 ? {}".format(shipPart1.manhattanDistance()))
        print("What is the Manhattan distance for part2 ? {}".format(shipPart2.manhattanDistance()))

if __name__ == "__main__":
    main(sys.argv)
