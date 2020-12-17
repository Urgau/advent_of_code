#!/usr/bin/env python3

import collections
import itertools
import sys

class Grid():
    @staticmethod
    def from_file(file, dim):
        actives = set((r, c) for r, line in enumerate(file.read().splitlines())
                     for c, n in enumerate(line) if n == '#')
        return Grid(actives, dim)

    def __init__(self, actives, dim):
        self.actives = set((0,) * (dim - 2) + cube for cube in actives)
        self.dim = dim

    def cycles(self, n):
        for i in range(n):
            self.next()
        return len(self.actives)

    def next(self):
        # https://github.com/mastermedo/aoc/blob/master/2020/day/17.py
        neighbours = collections.defaultdict(int)
        new_actives = set()

        for cube in self.actives:
            for offset in itertools.product((-1, 0, 1), repeat=self.dim):
                if offset != (0,) * self.dim:
                    neighbour = tuple(x + dx for x, dx in zip(cube, offset))
                    neighbours[neighbour] += 1

        for cube, n in neighbours.items():
            if cube in self.actives and n in [2, 3]:
                new_actives.add(cube)
            elif cube not in self.actives and n == 3:
                new_actives.add(cube)

        self.actives = new_actives

def main(args):
    with open(args[1], "r") as file:
        print("How many cubes are left in the active state after the sixth cycle with 3 dimensions? {}"
              .format(Grid.from_file(file, 3).cycles(6)))

    with open(args[1], "r") as file:
        print("How many cubes are left in the active state after the sixth cycle with 4 dimensions? {}"
              .format(Grid.from_file(file, 4).cycles(6)))

if __name__ == "__main__":
    main(sys.argv)
