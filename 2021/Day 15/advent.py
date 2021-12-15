#!/usr/bin/env python

from heapq import *
import sys

# https://www.reddit.com/r/adventofcode/comments/rgqzt5/comment/homzqnk/
def find(G):
    D = [[2**31 for _ in x] for x in G]
    D[0][0] = 0

    todo = [(0, (0, 0))]
    while todo:
        _, (x, y) = heappop(todo)
        for a, b in neighbours(G, x, y):
            if D[a][b] > G[a][b] + D[x][y]:
                D[a][b] = G[a][b] + D[x][y]
                heappush(todo, (D[a][b], (a, b)))
    return D[-1][-1]

def neighbours(G, x, y):
    X, Y = len(G), len(G[0])
    for a, b in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
        if 0 <= a < X and 0 <= b < Y: yield a, b

def extend(G):
    X, Y = len(G), len(G[0])
    return [[(G[x%X][y%Y] + x//X+y//Y - 1)%9+1
        for y in range(5*Y)] for x in range(5*X)]

if __name__ == "__main__":
    matrix = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            matrix.append([int(a) for a in line.strip()])

    print(find(matrix), find(extend(matrix)))
