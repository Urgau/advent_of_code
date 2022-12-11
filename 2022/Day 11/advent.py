#!/usr/bin/env python

import math
import copy
import sys

def add(a1, a2):
    return a1 + a2

def mul(a1, a2):
    return a1 * a2

def pow(a1, a2):
    return math.pow(a1, a2)

class Monkey:
    items = []
    op = None
    div_by = None
    if_true_to = None
    if_false_to = None
    inspected_items = 0

if __name__ == "__main__":
    lcm = 1
    monkeys = []
    with open(sys.argv[1], "r") as file:
        monkey = Monkey()
        for line in file:
            line = line.strip()
            if not line:
                monkeys.append(monkey)
                monkey = Monkey()
            else:
                words = line.split()
                if words[0] == "Monkey":
                    pass
                elif words[0] == "Starting":
                    monkey.items = [int(w.strip(',')) for w in words[2:]]
                elif words[0] == "Operation:":
                    if words[5] == "old":
                        if words[4] == "*":
                            monkey.op = (pow, 2)
                        else:
                            print(words)
                            raise words[1]
                    else:
                        monkey.op = (mul if words[4] == "*" else add, int(words[5]))
                elif words[0] == "Test:":
                    lcm *= int(words[3])
                    monkey.div_by = int(words[3])
                elif words[0] == "If":
                    if words[1] == "true:":
                        monkey.if_true_to = int(words[5])
                    elif words[1] == "false:":
                        monkey.if_false_to = int(words[5])
                    else:
                        print(words)
                        raise words[1]
                else:
                    print(words)
                    raise words[0]
        monkeys.append(monkey)

    def eval_for(monkeys, rounds, divider, use_lcm):
        for _ in range(rounds):
            for monkey in monkeys:
                for old in monkey.items:
                    new = int(monkey.op[0](old, monkey.op[1]) / divider)
                    to = monkey.if_true_to if new % monkey.div_by == 0 else monkey.if_false_to
                    if use_lcm:
                        new = new % lcm
                    monkeys[to].items.append(new)
                    monkey.inspected_items += 1
                monkey.items.clear()

        iits = [monkey.inspected_items for monkey in monkeys]
        iits.sort()

        print("Monkey business after {} rounds: {}".format(rounds, iits[-1] * iits[-2]))

    monkeys_part1 = monkeys
    monkeys_part2 = copy.deepcopy(monkeys)

    eval_for(monkeys_part1, 20, 3.0, False)
    eval_for(monkeys_part2, 10000, 1.0, True)

