#!/usr/bin/env python3

import sys

def findSum(numbers, x):
    for n1 in numbers:
        for n2 in numbers:
            if n1 + n2 == x:
                return (n1, n2)
    return None

BEFORE=25
def main(args):
    with open(args[1], "r") as file:
        numbers = []
        for line in file:
            numbers.append(int(line.strip()))

        firstNumberNotSumOfTwo = None
        for i in range(BEFORE, len(numbers)):
            if findSum(numbers[i - BEFORE:i], numbers[i]) == None:
                firstNumberNotSumOfTwo = numbers[i]
                break

        encryptionWeakness = None
        for rLen in range(2, 40):
            for i in range(rLen, len(numbers)):
                setOfNumbers = numbers[i - rLen:i]
                if sum(setOfNumbers) == firstNumberNotSumOfTwo:
                    encryptionWeakness = min(setOfNumbers) + max(setOfNumbers)
                    break
            if encryptionWeakness != None:
                break

        print("What is the first number that is not the sum of two numbers? {}".format(firstNumberNotSumOfTwo))
        print("What is the encryption weakness in your XMAS-encrypted list of numbers? {}".format(encryptionWeakness))

if __name__ == "__main__":
    main(sys.argv)
