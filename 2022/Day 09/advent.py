#!/usr/bin/env python

import math
import sys

def sign(a):
    if a == 0:
        return 0
    elif a < 0:
        return -1
    else:
        return 1

def simuate_with_x_tail(moves, x_tail):
    positions = [(0, 0) for _ in range(x_tail)]
    positionsSeen = {"0x0": True}

    for move in moves:
        (dir, how_many) = move
        if dir == "R":
            dirX = +1
            dirY = 0
        elif dir == "L":
            dirX = -1
            dirY = 0
        elif dir == "U":
            dirX = 0
            dirY = +1
        elif dir == "D":
            dirX = 0
            dirY = -1
        else:
            raise dir

        for _ in range(how_many):
            positions[0] = (positions[0][0] + dirX, positions[0][1] + dirY)
            for i in range(x_tail - 1):
                head, tail = positions[i], positions[i + 1]
                if math.sqrt(
                        math.pow(head[0] - tail[0], 2) +
                        math.pow(head[1] - tail[1], 2)) >= 2:
                    positions[i + 1] = (
                        tail[0] + sign(head[0] - tail[0]),
                        tail[1] + sign(head[1] - tail[1])
                    )

            positionsSeen["{}x{}".format(positions[x_tail - 1][0], positions[x_tail - 1][1])] = True
    return len(positionsSeen)

if __name__ == "__main__":
    moves = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.strip()
            if line:
                words = line.split()
                moves.append((words[0], int(words[1])))

    # Native part 1:
    # positionTailSeen = {"0x0": True}
    # tailPos = (0, 0)
    # headPos = (0, 0)
    #
    # for move in moves:
    #     (dir, how_many) = move
    #     if dir == "R":
    #         dirX = +1
    #         dirY = 0
    #     elif dir == "L":
    #         dirX = -1
    #         dirY = 0
    #     elif dir == "U":
    #         dirX = 0
    #         dirY = +1
    #     elif dir == "D":
    #         dirX = 0
    #         dirY = -1
    #     else:
    #         raise dir
    #
    #     for _ in range(how_many):
    #         newHeadPos = (headPos[0] + dirX, headPos[1] + dirY)
    #         if math.sqrt(
    #                 math.pow(newHeadPos[0] - tailPos[0], 2) +
    #                 math.pow(newHeadPos[1] - tailPos[1], 2)) >= 2:
    #             tailPos = headPos
    #             positionTailSeen["{}x{}".format(tailPos[0], tailPos[1])] = True
    #         headPos = newHeadPos
    #
    # print(len(positionTailSeen))

    print("Sum position seen at least one time with 2 length: {}"
          .format(simuate_with_x_tail(moves, 2)))
    print("Sum position seen at least one time with 10 length: {}"
          .format(simuate_with_x_tail(moves, 10)))
