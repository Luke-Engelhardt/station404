import random
import os


def placeTraps(spaceship: list[list[int | str]]) -> list[list[int | str]]:
    for i in range(len(spaceship)):
        for j in range(len(spaceship)):
            if random.randint(1, 7) == 1:
                spaceship[i][j] = 1
    return spaceship


def scanField(x: int, y: int, spaceship: list[list[int | str]], solution: list[list[int | str]]) -> int:
    neighbourTraps = getNeighbourTraps(solution, x, y)
    if solution[int(x)][int(y)] == 1:
        return 1
    else:
        if neighbourTraps == 0:
            spaceship[int(x)][int(y)] = " "
        else:
            spaceship[int(x)][int(y)] = neighbourTraps
        return 0


def markField(x: int, y: int, spaceship: list[list[int | str]]) -> list[list[int | str]]:
    spaceship[int(x)][int(y)] = "X"
    return spaceship


def getTraps(spaceship: list[list[int | str]]) -> list[tuple[int, int]]:
    traps = []
    for i in range(len(spaceship)):
        for j in range(len(spaceship)):
            if spaceship[i][j] == 1:
                traps.append((i, j))
    return traps


def getNeighbourTraps(spaceship: list[list[int | str]], x: int, y: int) -> int:
    neighbourTraps = 0
    size = len(spaceship)
    for i in range(max(0, x - 1), min(size, x + 2)):
        for j in range(max(0, y - 1), min(size, y + 2)):
            if (i != x or j != y) and spaceship[i][
                j
            ] == 1:  # gescannte zelle überspringen
                neighbourTraps += 1
    return neighbourTraps


def checkWin(spaceship: list[list[int | str]], solution: list[list[int | str]]) -> bool:
    for trap in getTraps(solution):
        if spaceship[trap[0]][trap[1]] != "X":
            return False
    return True


def welcome() -> None:
    print(
        """ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓██████████████▓▒░░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░   
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓█████████████▓▒░░▒▓████████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
                                                                                                          
                                                                                                          """
    )
    print("")
    print(
        """ 
░▒▓████████▓▒░▒▓██████▓▒░  
   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ 
   ░▒▓█▓▒░   ░▒▓██████▓▒░  
                           
                           
          """
    )
    print("")
    print(
        """ 
 ░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░       ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░   ░▒▓█▓▒░  ░▒▓████████▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
       ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
       ░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓███████▓▒░   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░▒▓████████▓▒░      ░▒▓█▓▒░ 
                                                                                                                                  
                                                                                                                                  
          """
    )


def instructions() -> None:
    clearTerminal()
    print(
        """\
STATION404 - INSTRUCTIONS

Welcome to STATION404, an abandoned space station filled with deadly traps.
Your mission is to navigate the wreckage and locate all the traps before it's too late!

GAME ACTIONS:
1. SHOW SPACESHIP
   - Displays the current map of the spaceship, showing explored areas and marked traps.

2. SCAN FIELD (x, y)
   - Scans the given coordinates for traps:
     - If a trap is present → GAME OVER!
     - If traps are in neighboring fields → Shows the number of adjacent traps.
     - If no traps are nearby → The field becomes empty.

3. MARK FIELD (x, y)
   - Places an 'X' on the selected coordinates to mark a suspected trap location.

Survive, map the traps, and escape STATION404!
"""
    )
    input("Press enter to continue...")


def clearTerminal() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
