#!/usr/bin/env python3

import sys

def findLoopSize(until, start=1, subjetNumber=7):
    val = start
    index = 0

    while val != until:
        val *= subjetNumber
        val %= 20201227
        index += 1

    return index

def handshake(subjectNumber, loopSize):
    val = 1

    for _ in range(loopSize):
        val *= subjectNumber
        val %= 20201227

    return val

def main(args):
    cardPubKey = int(args[1])
    doorPubKey = int(args[2])

    cardLoopSize = findLoopSize(cardPubKey)
    doorLoopSize = findLoopSize(doorPubKey)

    doorEncryptionKey = handshake(doorPubKey, cardLoopSize)
    cardEncryptionKey = handshake(cardPubKey, doorLoopSize)

    assert doorEncryptionKey == cardEncryptionKey

    print("What encryption key is the handshake trying to establish? {}".format(doorEncryptionKey))


if __name__ == "__main__":
    main(sys.argv)
