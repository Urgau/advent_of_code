#!/usr/bin/env python3

import collections
import sys

def part1(nums):
    counter = collections.Counter(b - a for a, b in zip([0] + nums, nums))
    return counter[1] * (counter[3] + 1)

def part2(nums):
    counter = collections.Counter((0, ))
    for num in nums:
        counter[num] += sum(counter[i] for i in range(num - 3, num))
    return counter[nums[-1]]

def main(args):
    with open(sys.argv[1], "r") as file:
        nums = []
        for line in file:
            nums.append(int(line.strip()))
        nums = sorted(nums)

        oneThreeJoltDifference = part1(nums)
        print("What is the number of 1-jolt differences multiplied by the number of 3-jolt differences? {}".format(oneThreeJoltDifference))

        distinctWaysToConnect = part2(nums)
        print("What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device? {}".format(distinctWaysToConnect))

if __name__ == "__main__":
    main(sys.argv)
