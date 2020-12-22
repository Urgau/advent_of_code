#!/usr/bin/env python

import sys

def combat(n, player1, player2):
    print("-- Round {} --".format(n))
    print("P1: {}".format(player1))
    print("P2: {}".format(player2))

    cp1 = player1.pop(0)
    cp2 = player2.pop(0)

    print("P1 plays: {}".format(cp1))
    print("P2 plays: {}".format(cp2))

    if cp1 > cp2:
        player1.append(cp1)
        player1.append(cp2)

        print("P1 wins the round!")
    elif cp1 < cp2:
        player2.append(cp2)
        player2.append(cp1)

        print("P2 wins the round!")
    else:
        assert cp1 != cp2
    return len(player1) == 0 or len(player2) == 0

def recursiveCombat(r, g, positions, player1, player2):
    print("-- Round {} (Game {}) --".format(r, g))
    print("P1: {}".format(player1))
    print("P2: {}".format(player2))

    for posP1, posP2 in positions:
        if posP1 == player1 and posP2 == player2:
            print("LOOP {} with {} ::: {} {}".format(posP1, posP2, player1, player2))
            player1.extend(player2)
            player2.clear()
            return True
    positions.append((player1[:], player2[:]))

    cp1 = player1.pop(0)
    cp2 = player2.pop(0)

    print("P1 plays: {}".format(cp1))
    print("P2 plays: {}".format(cp2))

    if len(player1) >= cp1 and len(player2) >= cp2:
        print("Playing a sub-game to determine the winner...")
        subPlayer1 = player1[:cp1]
        subPlayer2 = player2[:cp2]
        subPositions = []
        subG = g + 1
        subN = 1

        while recursiveCombat(subN, subG, subPositions, subPlayer1, subPlayer2) == False:
            subN += 1

        if len(subPlayer1) != 0:
            player1.append(cp1)
            player1.append(cp2)
            print("P1 win sub-game !!!")
        elif len(subPlayer2) != 0:
            player2.append(cp2)
            player2.append(cp1)
            print("P2 win sub-game !!!")
    elif cp1 > cp2:
        player1.append(cp1)
        player1.append(cp2)

        print("P1 wins the round!")
    elif cp1 < cp2:
        player2.append(cp2)
        player2.append(cp1)

        print("P2 wins the round!")
    else:
        assert cp1 != cp2
    return len(player1) == 0 or len(player2) == 0

def main(args):
    player1 = []
    player2 = []

    game = args[1]
    with open(args[2], "r") as file:
        p1 = False
        p2 = False
        for line in file:
            line = line.strip()
            if line == "Player 1:":
                p1 = True
                p2 = False
            elif line == "Player 2:":
                p1 = False
                p2 = True
            elif not line:
                continue
            elif p1:
                player1.append(int(line))
            elif p2:
                player2.append(int(line))

    n = 1
    if game == "combat":
        while combat(n, player1, player2) == False:
            n += 1
    elif game == "recursive-combat":
        positions = []
        while recursiveCombat(n, 1, positions, player1, player2) == False:
            n += 1
    else:
        raise Exception("{} is not a game!".format(game))

    winner = player1 if len(player1) > 0 else player2
    winnerScore = sum([(i + 1) * v for i, v in enumerate(winner[::-1])])

    print("What is the winning player's score? {}".format(winnerScore))

if __name__ == "__main__":
    main(sys.argv)
