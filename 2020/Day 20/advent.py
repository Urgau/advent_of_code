#!/usr/bin/env python3

import math
import sys

TOP=0
RIGHT=1
BOTTOM=2
LEFT=3

NESSIE = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
NESSIE_OFFSETS = [(i, j) for i in range(len(NESSIE)) for j in range(len(NESSIE[0])) if NESSIE[i][j] == '#']

class Tile:
    def __init__(self, id):
        self.id = id
        self.content = []
        self.borders = ["", "", "", ""]
        self.connections = [None, None, None, None]

    def rotate(self):
        self.content = [
            ''.join([ self.content[j][i] for j in range(len(self.content)) ])
            for i in range(len(self.content[0]) - 1, -1, -1)
        ]
        self._borders()

    def flip(self, horizontal, vertical):
        if horizontal:
            self.content = [l[::-1] for l in self.content]
        if vertical:
            self.content = self.content[::-1]
        self._borders()

    def _borders(self):
        self.borders = [self.content[0],
                        ''.join([l[-1] for l in self.content]),
                        self.content[-1],
                        ''.join([l[0] for l in self.content])]

    def border(self, idx):
        return self.borders[idx]

    def connection(self, idx):
        return self.connections[idx]

    def hasAnyConnections(self):
        return any([c != None for c in self.connections])

    def hasAllConnections(self):
        return all([c != None for c in self.connections])

visited=[]
def tileBorders(tiles, iTile):
    if iTile.hasAllConnections():
        return
    for bIdx in [TOP, RIGHT, BOTTOM, LEFT]:
        if iTile.connection(bIdx) is None:
            bNormal = iTile.border(bIdx)
            bReversed = bNormal[::-1]
            oIdx = (bIdx + 2) % 4
            for oTile in tiles:
                if oTile.id == iTile.id:
                    continue
                if oTile.connection(oIdx) != None:
                    continue
                for _ in range(4):
                    if oTile.border(oIdx) == bNormal:
                        iTile.connections[bIdx] = oTile
                        oTile.connections[oIdx] = iTile
                    elif oTile.border(oIdx) == bReversed:
                        oTile.flip(bIdx % 2 == 0, bIdx % 2 == 1)
                        iTile.connections[bIdx] = oTile
                        oTile.connections[oIdx] = iTile
                    elif not oTile.hasAnyConnections():
                        oTile.rotate()
                        continue
                    break
                if iTile.connection(bIdx) != None:
                    break
    for bIdx in [TOP, RIGHT, BOTTOM, LEFT]:
        cTile = iTile.connection(bIdx)
        if cTile != None and cTile.id not in visited:
            visited.append(cTile.id)
            tileBorders(tiles, cTile)

def countMonsters(map_monsters):
    count = 0
    for i in range(len(map_monsters) - 2):
        for j in range(len(map_monsters) - 20):
            monster_window = [map_monsters[i + P][j:j+20] for P in range(3)]
            is_monster = all([monster_window[pos[0]][pos[1]] == '#' for pos in NESSIE_OFFSETS])
            if is_monster:
                count += 1
    return count

def main(args):
    tiles = []

    # Parsing
    with open(args[1], "r") as file:
        tile = None
        for line in file:
            line = line.strip()

            if not line:
                tile._borders()
                tiles.append(tile)
                tile = None
            elif line.startswith("Tile"):
                tile = Tile(int(line[5:9]))
            else:
                tile.content.append(line)
        if tile != None:
            tile._borders()
            tiles.append(tile)

    # Logic
    tileBorders(tiles, tiles[0])

    # Part 1
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

    width = int(math.sqrt(len(tiles)))
    map = ["" for _ in range(width * 8)]
    positions = [[None,] * width for i in range(width)]

    positions[0][0] = cornerTopLeft

    for y in range(1, width):
        tile = positions[y - 1][0]
        if tile == None:
            continue
        positions[y][0] = tile.connections[BOTTOM]

    for y in range(width):
        for x in range(1, width):
            tile = positions[y][x - 1]
            if tile == None:
                continue
            positions[y][x] = tile.connections[RIGHT]

    print("Corners:")
    print([tile.id for tile in corners])

    print("\nPositions:")
    for y in range(len(positions)):
        for x in range(len(positions[y])):
            tile = positions[y][x]
            if tile == None:
                print(tile, end=" ")
            else:
                print(f"{tile.id}", end=" ")

            for lX in range(1, 9):
                map[y * 8 + lX - 1] += tile.content[lX][1:9]
        print()
    print()

    # Part 2
    monsters = None
    for _ in range(4):
        map = [
            ''.join([ map[j][i] for j in range(len(map)) ])
            for i in range(len(map[0]) - 1, -1, -1)
        ]
        monsters = countMonsters(map)
        if monsters:
            break
        map = map[::-1]
        monsters = countMonsters(map)
        if monsters:
            break
        map = map[::-1]

    plainBlocks = sum([line.count('#') for line in map])
    monstersBlocks = len(NESSIE_OFFSETS) * monsters

    print("What is the product of the four corner tiles IDs? {}".format(cornersProd))
    print("How many # are not part of a sea monster? {} (with {} sea monsters)"
          .format(plainBlocks - monstersBlocks, monsters))

if __name__ == "__main__":
    main(sys.argv)
