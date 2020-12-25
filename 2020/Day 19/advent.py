#!/usr/bin/env python3

import time
import sys
import re

class Rule:
    def __init__(self, name):
        self.name = name
        self.character = None
        self.leftPart = None
        self.rightPart = None

    def __str__(self):
        return f"{self.name}: {self.character} {self.leftPart} {self.rightPart}"

class Multi():
    def __init__(self, possibilities, indicies, parent=None):
        self.possibilities = possibilities
        self.indicies = indicies
        self.parent = parent

    def append(self, c):
        for i in self.indicies:
            self.possibilities[i] += c

    def appendMulti(self, m):
        self.indicies.extend(m.indicies)

    def branch(self):
        leftIndicies = self.indicies
        rightIndicies = []

        for i in leftIndicies:
            self.possibilities.append(self.possibilities[i])
            rightIndicies.append(len(self.possibilities) - 1)

        return (
            Multi(self.possibilities, leftIndicies, self),
            Multi(self.possibilities, rightIndicies, self)
        )

def recursive(rules, rule, m):
    if rule.character != None:
        m.append(rule.character)
    elif rule.leftPart != None and rule.rightPart != None:
        if rule.name in rule.rightPart:
            pBefore = [""]
            pAfter = [""]
            mBefore = Multi(pBefore, [0], None)
            mAfter = Multi(pAfter, [0], None)

            ruleIndex = rule.rightPart.index(rule.name)
            for i in rule.rightPart[:ruleIndex]:
                recursive(rules, rules[i], mBefore)
            for i in rule.rightPart[ruleIndex + 1:]:
                recursive(rules, rules[i], mAfter)

            if len(pBefore) > 1 and len(pAfter) > 1:
                # Is re supported recursive I could have used that
                # m.append("((({})(?1)({}))*)".format('|'.join(pBefore), '|'.join(pAfter)))

                # Instead I had to used this false recursive hack
                hacks = []
                for i in range(1, 5):
                    hacks.append("({}){{{}}}({}){{{}}}".format('|'.join(pBefore), i, '|'.join(pAfter), i))
                m.append("({})".format('|'.join(hacks)))
            elif len(pBefore) > 1:
                m.append("({})+".format('|'.join(pBefore)))
        else:
            mLeft, mRight = m.branch()

            for i in rule.leftPart:
                recursive(rules, rules[i], mLeft)
            for i in rule.rightPart:
                recursive(rules, rules[i], mRight)

            m.appendMulti(mRight)
    elif rule.leftPart != None:
        for i in rule.leftPart:
            recursive(rules, rules[i], m)
    elif rule.rightPart != None:
        for i in rule.rightPart:
            recursive(rules, rules[i], m)

def generatePossibilities(rules):
    possibilities = [""]
    recursive(rules, rules[0], Multi(possibilities, [0], None))
    return possibilities

def main(args):
    with open(args[1], "r") as file:
        messages = []
        rules = {}

        for line in file:
            line = line.strip()
            if not line:
                continue

            if ":" in line:
                p1 = line.split(": ")
                rule = Rule(int(p1[0]))

                if p1[1].startswith('"'):
                    rule.character = p1[1][1:2]
                elif '|' in p1[1]:
                    p2 = p1[1].split('|')
                    p3 = p2[0].split()
                    p4 = p2[1].split()
                    rule.leftPart = [int(s) for s in p3]
                    rule.rightPart = [int(s) for s in p4]
                else:
                    p2 = p1[1].split()
                    rule.leftPart = [int(s) for s in p2]

                rules[int(p1[0])] = rule
            else:
                messages.append(line)

        start = time.time()
        possibilities = generatePossibilities(rules)
        end = time.time()

        print("How many possibilities? {} ({:.2}s)".format(len(possibilities), end - start))

        start = time.time()
        rePossibilities = []
        for possibility in possibilities:
            if ")+" in possibility:
                print(possibility)
                rePossibilities.append(re.compile(f"^{possibility}$"))
        end = time.time()
        print("How many regex possibilities: {} ({:.2}s)".format(len(rePossibilities), end - start))

        ruleZeroMatchs = 0
        for message in messages:
            if message in possibilities:
                ruleZeroMatchs += 1
                continue

            for rePos in rePossibilities:
                if rePos.match(message):
                    print(message)
                    ruleZeroMatchs += 1
                    break
        print("How many messages completely match rule 0? {}".format(ruleZeroMatchs))

if __name__ == "__main__":
    main(sys.argv)
