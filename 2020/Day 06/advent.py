#!/usr/bin/env python3

import sys

class Group:
    def __init__(self):
        self.len = 0
        self.questions = {}

def main():
    with open(sys.argv[1], "r") as file:
        groups = []
        group = Group()
        for line in file:
            line = line.strip()
            if not line:
                groups.append(group)
                group = Group()
            else:
                group.len += 1
                for c in line:
                    if c not in group.questions:
                        group.questions[c] = 1
                    else:
                        group.questions[c] += 1
        groups.append(group)

        totalAnyoneQuestions = 0
        for group in groups:
            totalAnyoneQuestions += len(group.questions)

        totalEveryoneQuestions = 0
        for group in groups:
            for key in group.questions:
                if group.questions[key] == group.len:
                    totalEveryoneQuestions += 1

        print("Total anyone questions: {}".format(totalAnyoneQuestions))
        print("Total evryone questions: {}".format(totalEveryoneQuestions))

if __name__ == "__main__":
    main()
