#!/usr/bin/env python

import sys

if __name__ == "__main__":
    # graph = {}
    # start = None
    # end = None
    # width = None
    # height = None
    # with open(sys.argv[1], "r") as file:
    #     y = 0
    #     for line in file:
    #         line = line.strip()
    #         if line:
    #             for (x, c) in enumerate(line):
    #                 pos = (x, y)
    #                 graph[pos] = c
    #                 if c == 'S':
    #                     start = pos
    #                 elif c == 'E':
    #                     end = pos
    #             width = x
    #         height = y
    #         y += 1
    #
    # print(width, height, start, end)
    # graph_dijkstra = {}
    # for x in range(width + 1):
    #     for y in range(height + 1):
    #         edges = {}
    #         current_c = graph[(x, y)]
    #         if x - 1 >= 0 and y >= 0:
    #             if abs(ord(current_c) - ord(graph[(x - 1, y)])) <= 1 or current_c == 'S':
    #                 edges[(x - 1, y)] = 1
    #         if x + 1 < width and y < height:
    #             if abs(ord(current_c) - ord(graph[(x + 1, y)])) <= 1 or current_c == 'S':
    #                 edges[(x + 1, y)] = 1
    #         if x >= 0 and y - 1 >= 0:
    #             if abs(ord(current_c) - ord(graph[(x, y - 1)])) <= 1 or current_c == 'S':
    #                 edges[(x, y - 1)] = 1
    #         if x < width and y + 1 < height:
    #             if abs(ord(current_c) - ord(graph[(x, y + 1)])) <= 1 or current_c == 'S':
    #                 edges[(x, y + 1)] = 1
    #         graph_dijkstra[(x, y)] = edges

    # Inspired from https://github.com/ephemient/aoc2022/ because I can't get the dijkstra
    # algo to work properly
    grid = [list(map(ord, l.strip())) for l in open(sys.argv[1]).readlines()]
    h, w = len(grid), len(grid[0])
    start, end = [[(y, x) for x in range(w) for y in range(h) if grid[y][x] == c][0] for c in (ord("S"), ord("E"))]

    grid[start[0]][start[1]] = ord("a")
    grid[end[0]][end[1]] = ord("z")

    q = [(0, end)]
    seen = set()
    p1 = p2 = 0
    while True:
        l, p = q.pop(0)
        if p in seen:
            continue
        seen.add(p)
        y, x = p
        if grid[y][x] == ord("a"):
            if not p2:
                p2 = l
            elif p == start:
                p1 = l
                break

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and (ny, nx) not in seen and (grid[y][x] - grid[ny][nx]) <= 1:
                q.append((l + 1, (ny, nx)))

    print(p1, p2)
