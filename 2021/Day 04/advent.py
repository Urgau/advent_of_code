#!/usr/bin/env python

import sys

class Board:
    def __init__(self):
        self.lines = [[], [], [], [], []]

if __name__ == "__main__":

    boards = []
    numbers = []
    with open(sys.argv[1], "r") as file:
        b_pos = 0
        board = Board()
        for i, line in enumerate(file):
            if i == 0:
                numbers = [int(n) for n in line.split(',')]
            elif line.strip():
                board.lines[b_pos] = [(int(n), False) for n in line.split()]
                b_pos += 1
                if b_pos == 5:
                    b_pos = 0
                    boards.append(board)
                    board = Board()

    winningBoards = []
    for n in numbers:
        for b in boards:
            if b in winningBoards:
                continue
            complete = False
            for l in b.lines:
                trues = 0
                for i, v in enumerate(l):
                    if v[0] == n:
                        l[i] = (n, True)
                        trues += 1
                    elif v[1] == True:
                        trues += 1
                if trues == 5:
                    complete = True
                    break
            for i in range(5):
                if b.lines[0][i][1] == True and b.lines[1][i][1] == True and \
                        b.lines[2][i][1] == True and b.lines[3][i][1] == True and b.lines[4][i][1] == True:
                    complete = True
                    break
            if complete:
                sum = 0
                for l in b.lines:
                    for v in l:
                        if v[1] == False:
                            sum += v[0]
                print(f"[{len(winningBoards)+1}nth] sum: {sum} - n: {n} - result: {n * sum}")
                winningBoards.append(b)
