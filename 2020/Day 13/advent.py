#!/usr/bin/env python3

import urllib.parse
import sys

WOLFRAM_URL="https://www.wolframalpha.com/input/?i="

def main(args):
    with open(args[1], "r") as file:
        myTimestamp = int(file.readline().strip())
        timestampResults = []

        busIds = file.readline().strip().split(',')
        for busId in busIds:
            if busId == "x":
                continue
            busId = int(busId)
            tm = busId
            while tm < myTimestamp:
                tm += busId
            timestampResults.append((busId, tm))

        earliestBusId, earliestTm = min(timestampResults, key=lambda x: x[1])
        print("What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus? {}".format(earliestBusId * (earliestTm - myTimestamp)))

        equations = []
        for index in range(len(busIds)):
            if busIds[index] == "x":
                continue
            busId = int(busIds[index])
            equations.append(f"(t+{index})%{busId}=0")
        print(f"What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list? {WOLFRAM_URL}{urllib.parse.quote_plus(','.join(equations))}")

if __name__ == "__main__":
    main(sys.argv)
