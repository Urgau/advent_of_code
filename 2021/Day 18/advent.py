#!/usr/bin/env python

# Based on: https://topaz.github.io/paste/#XQAAAQD1BwAAAAAAAAA0m0pnuFI8c9WAoVc3IiG2klervCCkc3Fk33PvMZ8ZxYTRWczt5PtHYRBHYFff4ul0TRcyM/2lzDiSzW4VNg/PNjmJjYW9ckowDG1eb/5D8V9Rco3xOqXH2QGG6rijExTF9a0BoO3AniSgROLnmdNs7IU2MHGEC1h46yQ0I9+/3NjIUx/j8JHXp+mzyHeUNzRE08VPVEOSWXc3c3QusQxOVetAC819kymhm0NzeCxcwoJ9ZYfcsrRX5xnIAmqzM9aaaovASm+9WXOTEmnSGlA5F5tp/mtzkYg4NCbbjyqcbfkwfcNBrOtWvU3uLvgr9fOwII9t6HPvxgluyyLD6g8IDYx0LQH3WI5hEtaFc+zkGOEMChNgLKcICmEJT3JuA1amciIbQF41aYyQ00jTs/zh/iPi5G/1nPjr3tUGlu3nkom0d1dLjG1jMTb6njwPljb67fgjBBwRn0UM+NLHQS6r+0Smj46UmiaFFhF7HT/4iRvjk9wLabssahI1MHbORR6Wqn7QNrkq8D2ceGvUZHrggSf1u5UXB2tt7jE1Pp5F7jcFR4FPeUVYueXQejrMWOxxz+XQ3Mxz7AAe6aalOZpe/RBpUzycp/LsiKQLnGzIMArHzZ4qyjbBnlmIOHVfT9xfFZQE6Cpd7/gT6qBup60k2bVxVv54Wv8ihs4HhVbX3XaR37X4xA4gVtXb4sxaIy5a/s4W8qc0yQnGpC5w/aYewQ4n3DWFqvdQHF93/gtD7zE1p5SxTCU/2dpO0aXV3J190kXCyCa29JaUf6xzqf74CwL1id++qiv6N+Ouxr2NUxbrgzsNVb+4qnhUDRxpNTBdasf0azv/srvyWGuB2omx1T3igvdj/pbyAA==
# I was short on time. :'-(

import functools
import sys
import re

def tokenize(expr):
    return [int(token) if '0' <= token[0] <= '9' else token
            for token in re.findall("\[|\]|\d+", expr)]

def explode(tokens):
    depth = 0
    for index in range(len(tokens) - 4):
        if (depth >= 4 and
            tokens[index + 0] == '[' and
            tokens[index + 3] == ']'):
            for left in range(index - 1, -1, -1):
                if isinstance(tokens[left], int):
                    tokens[left] += tokens[index + 1]
                    break
            for right in range(index + 4, len(tokens)):
                if isinstance(tokens[right], int):
                    tokens[right] += tokens[index + 2]
                    break
            tokens[index : index + 4] = [0]
            return True
        elif tokens[index] == '[':
            depth += 1
        elif tokens[index] == ']':
            depth -= 1
    return False

def split(tokens):
    for index in range(len(tokens)):
        if isinstance(tokens[index], int) and tokens[index] >= 10:
            tokens[index : index + 1] = ['[',
                                         (tokens[index] + 0) // 2,
                                         (tokens[index] + 1) // 2,
                                         ']']
            return True
    return False

def reduct(tokens):
    while explode(tokens) or split(tokens):
        pass
    return tokens

def magnitude(tokens):
    stack = []
    for token in tokens:
        if isinstance(token, int):
            stack.append(token)
        elif token == ']':
            stack[-2 :] = [3 * stack[-2] + 2 * stack[-1]]
    return stack[-1]

if __name__ == "__main__":
    numbers = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            numbers.append(tokenize(line.strip()))

    total = functools.reduce(
        lambda left, right: reduct(['['] + left + right + [']']),
        numbers)
    print("Part 1:", magnitude(total))

    largest = 0
    for left in numbers:
        for right in numbers:
            total = reduct(['['] + left + right + [']'])
            largest = max(largest, magnitude(total))
    print("Part 2:", largest)
