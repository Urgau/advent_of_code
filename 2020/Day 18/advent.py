#!/usr/bin/env python3

import sys

class AdventOfCodeNumericParser(object):
    def __init__(self, advanced=False):
        self.advanced = advanced

    def parse(self, expr):
        return expr.replace('(', "( ").replace(')', " )").split()

    def pharentises(self, expr):
        start = None
        end = None
        lvl = 0

        for i, c in enumerate(expr):
            if c == '(':
                lvl += 1
                if start is None:
                    start = i
            elif c == ')':
                lvl -= 1
                if lvl == 0:
                    end = i
                    break

        return start, end

    def eval_expr(self, expr, advanced):
        while '(' in expr:
            start, end = self.pharentises(expr)
            expr[start:end + 1] = self.eval_expr(expr[start + 1:end + 1 - 1], advanced)

        if advanced == False:
            result = int(expr[0])
            for i in range(1, len(expr), 2):
                if expr[i] == '+':
                    result += int(expr[i + 1])
                elif expr[i] == '*':
                    result *= int(expr[i + 1])
                else:
                    raise Exception("ERROR: {}".format(expr[i]))
            return [result]

        while '+' in expr:
            index = int(expr.index('+'))
            expr[index - 1:index + 1 + 1] = self.eval_expr(expr[index - 1: index + 1 + 1], False)
        return self.eval_expr(expr, False)

    def eval(self, input):
        return int(self.eval_expr(self.parse(input), self.advanced)[0])

def main(args):
    aocNP = AdventOfCodeNumericParser()
    aocNPAdvanced = AdventOfCodeNumericParser(advanced=True)

    with open(args[1], "r") as file:
        somme = 0
        sommeAdvanced = 0

        for line in file:
            somme += aocNP.eval(line.strip())
            sommeAdvanced += aocNPAdvanced.eval(line.strip())

        print("What is the sum of the resulting values? {}".format(somme))
        print("What do you get if you add up the results of evaluating the homework problems using these new rules? {}".format(sommeAdvanced))

if __name__ == "__main__":
    main(sys.argv)
