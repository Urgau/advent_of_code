#!/usr/bin/python3

import collections
import sys

class Constrain():
    def __init__(self, name, ranges):
        self.name = str(name)
        self.ranges = list(ranges)

    def isInRanges(self, val):
        return any(val in range for range in self.ranges)

def main(args):
    with open(args[1], "r") as file:
        constrains = []
        ownTicket = None
        nearbyTickets = []

        phase = 0
        for line in file:
            line = line.strip()
            if not line:
                continue
            elif line == "your ticket:" or line == "nearby tickets:":
                phase += 1
            elif phase == 0:
                s1 = line.split(": ")
                s2 = s1[1].split(" or ")
                ranges = []
                for s in s2:
                    s = s.split("-")
                    ranges.append(range(int(s[0]), int(s[1]) + 1))
                constrains.append(Constrain(s1[0], ranges))
            elif phase == 1:
                ownTicket = list(map(int, line.split(",")))
            elif phase == 2:
                nearbyTickets.append(list(map(int, line.split(","))))
            else:
                assert False

        valids = []
        invalids = []
        for nearbyTicket in nearbyTickets:
            valid = True
            for value in nearbyTicket:
                if not any(constrain.isInRanges(value) for constrain in constrains):
                    invalids.append(value)
                    valid = False
            if valid:
                valids.append(nearbyTicket)

        possibles = collections.defaultdict(list)
        for field in range(len(valids[0])):
            for iConstrain in range(len(constrains)):
                if all(constrains[iConstrain].isInRanges(ticket[field]) for ticket in valids):
                    possibles[field].append(iConstrain)

        order = {}
        for field in sorted(possibles, key=lambda i: len(possibles[i])):
            for index in possibles[field]:
                if index not in order.values():
                    order[field] = index

        errorRate = sum(invalids)
        print("What is your ticket scanning error rate? {}".format(errorRate))

        departures = 1
        for field in order:
            iConstrain = order[field]
            if constrains[iConstrain].name.startswith("depart"):
                departures *= ownTicket[field]
        print("What do you get if you multiply those six values together? {}".format(departures))

if __name__ == "__main__":
    main(sys.argv)
