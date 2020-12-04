#!/usr/bin/env python3

import sys

REQUIRED = 1
IGNORABLE = 0

USE_VALIDATOR = True
FIELDS = [
    ("byr", REQUIRED, lambda val: int(val) >= 1920 and int(val) <= 2002),
    ("iyr", REQUIRED, lambda val: int(val) >= 2010 and int(val) <= 2020),
    ("eyr", REQUIRED, lambda val: int(val) >= 2020 and int(val) <= 2030),
    ("hgt", REQUIRED, lambda val: isValidHeight(val)),
    ("hcl", REQUIRED, lambda val: val[0] == '#' and int(val[1:], 16) >= 0),
    ("ecl", REQUIRED, lambda val: val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
    ("pid", REQUIRED, lambda val: len(val) == 9 and int(val) >= 0),
    ("cid", IGNORABLE, lambda val: True)
]

def isValidHeight(val):
    nbr = int(val[:-2])
    unit = val[-2:]
    if unit == "cm":
        return nbr >= 150 and nbr <= 193
    elif unit == "in":
        return nbr >= 59 and nbr <= 76
    else:
        return False

def main():
    with open(sys.argv[1], "r") as file:
        entries = []
        keys = {}
        for line in file:
            if line == "\n":
                entries.append(keys.copy())
                keys.clear()
            else:
                words = line.split()
                for word in words:
                    (key, val) = word.split(':')
                    keys[key] = val
        entries.append(keys.copy())

        valid = 0
        invalid = 0
        for entry in entries:
            isValid = True
            for (name, status, validator) in FIELDS:
                if status == REQUIRED:
                    if name not in entry:
                        isValid = False
                        break
                    elif USE_VALIDATOR == True:
                        try:
                            if validator(entry[name]) == False:
                                isValid = False
                                break
                        except:
                            isValid = False
                            break

            if isValid:
                valid += 1
            else:
                invalid += 1

        print("Valid: {} | Invalid: {}".format(valid, invalid))

if __name__ == "__main__":
    main()
