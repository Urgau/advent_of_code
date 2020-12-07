#!/usr/bin/env python3

import sys

class Bag:
    def __init__(self, name, parent=None):
        self.name = name
        self.parents = [parent] if parent is not None else []
        self.contents = {}

def findOrCreate(bags, name, parent=None):
    #print(name, parent)
    if name in bags:
        bag = bags[name]
        if parent is not None:
            bag.parents.append(parent)
        return bag
    else:
        bag = Bag(name, parent)
        bags[name] = bag
        return bag

alreadyPass = {}
def recurseParents(currentBag, fromBag):
    total = 1 if fromBag is not None else 0
    for pBag in currentBag.parents:
        if pBag not in alreadyPass:
            alreadyPass[pBag] = True
            total += recurseParents(pBag, currentBag)
    return total

def recurseChildren(currentBag, fromBag):
    total = 0
    for bag in currentBag.contents:
        total += currentBag.contents[bag] * recurseChildren(bag, currentBag)
    return total + sum(currentBag.contents.values())

def main():
    with open(sys.argv[1], "r") as file:
        bags = {}
        for line in file:
            ctn = line.split(" bags contain ")
            virgules = ctn[1].split(",")

            leftBag = findOrCreate(bags, ctn[0])
            for virgule in virgules:
                virgule = virgule.strip().rstrip(".")
                if virgule and virgule != "no other bags":
                    howMany = int(virgule[0])
                    name = virgule[1: -5 if howMany > 1 else -4].strip()
                    rightBag = findOrCreate(bags, name, leftBag)
                    leftBag.contents[rightBag] = howMany

        shinyGoldBag = bags["shiny gold"]
        print("How many bag colors can eventually contain at least one shiny gold bag? {}"
              .format(recurseParents(shinyGoldBag, None)))
        print("How many individual bags are required inside your single shiny gold bag? {}"
              .format(recurseChildren(shinyGoldBag, None)))

if __name__ == "__main__":
    main();
