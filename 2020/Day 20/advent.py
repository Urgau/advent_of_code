#!/usr/bin/env python3

import math
import sys

TOP=0
RIGHT=1
BOTTOM=2
LEFT=3

class Tile:
    def __init__(self, id):
        self.id = id
        self.content = []
        self.rotation = None
        self.flipVertical = None
        self.flipHorizontal = None
        self.borders = ["", "", "", ""]
        self.connections = [None, None, None, None]

    def connection(self, idx):
        if self.rotation != None:
            idx = int((idx + (self.rotation / 90)) % 4)
        if self.flipped == True:
            idx = int((idx + 2) % 4)
        return self.connections[idx]

def foundCompatibleBorder(tiles, inputTile, bIdx):
    bNormal = inputTile.borders[bIdx]
    bReversed = bNormal[::-1]
    for tile in tiles:
        if tile.id == inputTile.id:
            continue
        for i in [TOP, RIGHT, BOTTOM, LEFT]:
            if tile.connections[i] == None and (tile.borders[i] == bNormal or tile.borders[i] == bReversed):
                inputTile.rotation = (((bIdx + 2) % 4) - i) * 90
                if i == TOP or i == BOTTOM:
                    tile.flipHorizontal = (tile.borders[i] == bReversed)
                else:
                    tile.flipVertical = (tile.borders[i] == bReversed)
                tile.connections[i] = inputTile #(inputTile, bIdx)
                inputTile.connections[bIdx] = tile #(tile, i)
                return tile
    return None

def main(args):
    tiles = []

    with open(args[1], "r") as file:
        tile = None
        contentPos = 0
        for line in file:
            line = line.strip()

            if not line:
                tiles.append(tile)
                contentPos = 0
                tile = None
            elif line.startswith("Tile"):
                tile = Tile(int(line[5:9]))
            else:
                contentPos += 1
                if contentPos == 1:
                    tile.borders[TOP] = line
                elif contentPos == 10:
                    tile.borders[BOTTOM] = line
                else:
                    tile.content.append(line[1:-2])

                tile.borders[LEFT] += line[0]
                tile.borders[RIGHT] += line[-1]
        if tile != None:
            tiles.append(tile)


    for tile in tiles:
        for bIdx in [TOP, RIGHT, BOTTOM, LEFT]:
            if tile.connections[bIdx] == None:
                foundCompatibleBorder(tiles, tile, bIdx)

    corners = []
    cornersProd = 1
    cornerTopLeft = None
    for tile in tiles:
        howManyNone = 0
        for bIdx in [TOP, RIGHT, BOTTOM, LEFT]:
            if tile.connections[bIdx] == None:
                howManyNone += 1
        assert howManyNone <= 2
        if howManyNone == 2:
            cornersProd *= tile.id
            corners.append(tile)
            if tile.connections[TOP] == None and tile.connections[LEFT] == None:
                cornerTopLeft = tile

    assert len(corners) == 4
    print("What do you get if you multiply together the IDs of the four corner tiles? {}".format(cornersProd))

    #width = int(math.sqrt(len(tiles)))
    #positions = [[None,] * width for i in range(width)]

    #positions[0][0] = cornerTopLeft

    #for y in range(1, width):
    #    tile = positions[y - 1][0]
    #    if tile == None:
    #        continue
    #    positions[y][0] = tile.connections[BOTTOM]

    #for y in range(width):
    #    for x in range(1, width):
    #        tile = positions[y][x - 1]
    #        if tile == None:
    #            continue
    #        positions[y][x] = tile.connections[RIGHT]

    #print("Corners:")
    #for corner in corners:
    #    print(corner.id)

    #print("\nPositions:")
    #for line in positions:
    #    for col in line:
    #        tile = col
    #        if tile == None:
    #            print(tile, end=" ")
    #        else:
    #            #print(f"{tile.id}", end=" ")
    #            print(f"{tile.id} ({tile.rotation}, {tile.flipHorizontal} {tile.flipVertical})", end=" ")
    #            if tile.id == 3079:
    #                print(','.join(str(con.id) if con != None else "None" for con in tile.connections))
    #    print()

if __name__ == "__main__":
    main(sys.argv)
