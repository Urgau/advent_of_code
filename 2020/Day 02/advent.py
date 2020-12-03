#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    valid = 0
    invalid = 0
    with open(sys.argv[1], "r") as file:
        for line in file:
            strs = line.split()
            range = strs[0].split("-")
            rangeStart = int(range[0])
            rangeEnd = int(range[1])
            character = strs[1][0]
            password = strs[2]
            occurence = password.count(character)
            #if occurence >= rangeStart and occurence <= rangeEnd:
            if bool(password[rangeStart - 1] == character) ^ bool(password[rangeEnd - 1] == character):
                valid += 1
            else:
                invalid += 1
    print(valid)
