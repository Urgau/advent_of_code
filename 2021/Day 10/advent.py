#!/usr/bin/env python

import sys

def reverse(c):
    if c == "(":
        return ")"
    elif c == "[":
        return "]"
    elif c == "{":
        return "}"
    elif c == "<":
        return ">"
    raise c

if __name__ == "__main__":
    lines = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            lines.append(line.strip())

    syntaxErrorScore = 0
    incompleteLinesScore = []
    for line in lines:
        stack = []
        syntaxError = False
        for c in line:
            if c == "(" or c == "[" or c == "{" or c == "<":
                stack.append(c)
            else:
                expected = reverse(stack.pop())
                if c != expected:
                    if c == ")":
                        syntaxErrorScore += 3
                    elif c == "]":
                        syntaxErrorScore += 57
                    elif c == "}":
                        syntaxErrorScore += 1197
                    elif c == ">":
                        syntaxErrorScore += 25137
                    else:
                        raise c
                    syntaxError = True
                    break
        if not syntaxError and len(stack) != 0:
            score = 0
            while len(stack) != 0:
                score *= 5
                missing = reverse(stack.pop())
                if missing == ")":
                    score += 1
                elif missing == "]":
                    score += 2
                elif missing == "}":
                    score += 3
                elif missing == ">":
                    score += 4
                else:
                    raise c
            incompleteLinesScore.append(score)

    incompleteLinesScore.sort()
    print(f"Syntax error score: {syntaxErrorScore}")
    print(f"Middle score of incomplete lines: {incompleteLinesScore[int(len(incompleteLinesScore) / 2)]}")

