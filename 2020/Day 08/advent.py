#!/usr/bin/env python3

import sys

def exec(commands):
    cmdNext = 0
    cmdFlow = []
    globalCounter = 0
    while cmdNext not in cmdFlow and len(commands) > cmdNext:
        cmdFlow.append(cmdNext)
        cmd, val = commands[cmdNext]
        if cmd == "acc" or cmd == "nop":
            if cmd == "acc":
                globalCounter += val
            cmdNext += 1
        elif cmd == "jmp":
            cmdNext += val
        else:
            raise Exception("Unkown command {} {}".format(cmd, val))
    if cmdNext in cmdFlow:
        return (False, globalCounter)
    return (True, globalCounter)

def fixAndExec(commands):
    cmdIndexChanged = None
    globalCounterWithFix = None
    for i in range(len(commands)):
        prevCmd, prevVal = commands[i]
        if prevCmd == "jmp" or prevCmd == "nop":
            commands[i] = ("nop" if prevCmd == "jmp" else "jmp", prevVal)
            g, c = exec(commands)
            if g == True:
                cmdIndexChanged = i
                globalCounterWithFix = c
                break
            commands[i] = (prevCmd, prevVal)
    return (cmdIndexChanged, globalCounterWithFix)

def main(args):
    with open(args[1], "r") as file:
        commands = []
        for line in file:
            words = line.strip().split()
            commands.append((words[0], int(words[1])))

        _, globalCounterBeforeInfiniteLoop = exec(commands)
        print("Immediately before any instruction is executed a second time, what value is in the accumulator? {}".format(globalCounterBeforeInfiniteLoop))

        cmdIndexChanged, globalCounterWithFix = fixAndExec(commands)
        print("What is the value of the accumulator after the program terminates? {} (changed command {})".format(globalCounterWithFix, cmdIndexChanged + 1))

if __name__ == "__main__":
    main(sys.argv)
