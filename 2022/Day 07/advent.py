#!/usr/bin/env python

import sys

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.directories = []

    def dir(self, name):
        for dir in self.directories:
            if dir.name == name:
                return dir
        dir = Directory(name, self)
        self.directories.append(dir)
        return dir

    def file(self, name, size):
        for file in self.files:
            if file.name == name:
                return file
        file = File(name, size, self)
        self.files.append(file)
        return file

class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.parent = parent
        self.size = size

if __name__ == "__main__":
    filesystem = Directory(None, None)
    with open(sys.argv[1], "r") as file:
        current_dir = filesystem
        for line in file:
            line = line.strip()
            if not line:
                continue
            words = line.split()
            if words[0] == "$":
                if words[1] == "cd":
                    if words[2] == "/":
                        current_dir = filesystem
                    elif words[2] == "..":
                        current_dir = current_dir.parent
                    else:
                        current_dir = current_dir.dir(words[2])
                elif words[1] == "ls":
                    if len(words) > 2:
                        print(words)
                        raise "eee"
            elif words[0] == "dir":
                current_dir.dir(words[1])
            else:
                current_dir.file(words[1], int(words[0]))

    sizes = []
    sumDirSizeAtMost100000 = 0
    def recur(dir):
        global sizes
        global sumDirSizeAtMost100000
        size = 0
        for dirit in dir.directories:
            size += recur(dirit)
        for file in dir.files:
            size += file.size
        if size <= 100000:
            sumDirSizeAtMost100000 += size
        sizes.append(size)
        return size

    totalSize = recur(filesystem)
    print("Sum directory size at most 100000: {}".format(sumDirSizeAtMost100000))

    freeSpace = 70000000 - totalSize
    minSpaceToFree = 30000000 - freeSpace

    sizes.sort()

    minDirSize = None
    for size in sizes:
        if size >= minSpaceToFree:
            minDirSize = size
            break
    print("Min size dir to delete: {}".format(minDirSize))
