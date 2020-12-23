#!/usr/bin/env python3

import sys

def play(cups, moves):
    size = len(cups)
    cc = 0

    for _ in range(moves):
        c1 = cups[(cc + 1) % size]
        c2 = cups[(cc + 2) % size]
        c3 = cups[(cc + 3) % size]

        dc = cups[cc] - 1
        ccv = cups[cc]

        cups.remove(c1)
        cups.remove(c2)
        cups.remove(c3)

        while dc not in cups:
            dc = dc - 1 if dc > 1 else size

        pivot = cups.index(dc) + 1
        cups[pivot:pivot] = [c1, c2, c3]
        cc = (cups.index(ccv) + 1) % size

def main(args):
    cups = list(map(int, args[1]))

    cupsPart1 = cups[:]
    cupsPart2 = cups + list(range(10, 1000000+1))

    play(cupsPart1, 100)
    oneIndex = cupsPart1.index(1)
    print("What are the labels on the cups after cup 1? {}{}"
          .format(''.join(map(str, cupsPart1[oneIndex + 1:])), ''.join(map(str, cupsPart1[:oneIndex]))))

    # Very very slow
    play(cupsPart2, 10000000)
    oneIndex = cups.index(1)
    print("What do you get if you multiply their labels together? {}"
          .format(cupsPart2[oneIndex + 1] * cupsPart2[oneIndex + 2]))

if __name__ == "__main__":
    main(sys.argv)
