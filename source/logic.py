"""Game logic module - handles trap placement, field scanning, and win condition checking"""

import random
import os

# pylint: disable=line-too-long
# disabling pylint line-too-long check as it marks ascii art


def place_traps(spaceship: list[list[int | str]]) -> list[list[int | str]]:
    """randomly places traps"""
    for i, row in enumerate(spaceship):
        for j, _ in enumerate(row):
            if random.randint(1, 7) == 1:
                spaceship[i][j] = 1
    return spaceship


def scan_field(
    x: int, y: int, spaceship: list[list[int | str]], solution: list[list[int | str]]
) -> int:
    """scans a field and changes the value of the field for the number of nearby traps"""
    neighbor_traps = get_neighbor_traps(solution, x, y)
    if solution[int(x)][int(y)] == 1:
        return 1
    if neighbor_traps == 0:
        spaceship[int(x)][int(y)] = " "
    else:
        spaceship[int(x)][int(y)] = neighbor_traps
    return 0


def mark_field(
    x: int, y: int, spaceship: list[list[int | str]]
) -> list[list[int | str]]:
    """marks a field at coordinates (x,y) with an X"""
    spaceship[int(x)][int(y)] = "X"
    return spaceship


def get_traps(spaceship: list[list[int | str]]) -> list[tuple[int, int]]:
    """returns a list of coordinates where traps are located in the spaceship grid"""
    traps = []
    for i, row in enumerate(spaceship):
        for j, cell in enumerate(row):
            if cell == 1:
                traps.append((i, j))
    return traps


def get_neighbor_traps(spaceship: list[list[int | str]], x: int, y: int) -> int:
    """counts the number of traps in nearby fields"""
    neighbor_traps = 0
    size = len(spaceship)
    for i in range(max(0, x - 1), min(size, x + 2)):
        for j in range(max(0, y - 1), min(size, y + 2)):
            if (i != x or j != y) and spaceship[i][j] == 1:  # Skip scanned cell
                neighbor_traps += 1
    return neighbor_traps


def check_win(
    spaceship: list[list[int | str]], solution: list[list[int | str]]
) -> bool:
    """Checks if all traps have been correctly marked in the spaceship grid"""
    for trap in get_traps(solution):
        if spaceship[trap[0]][trap[1]] != "X":
            return False
    return True


def welcome() -> None:
    """displays welcome screen with ascii art"""
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
    """Display game instructions and rules"""
    clear_terminal()
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


def clear_terminal() -> None:
    """Clears the terminal"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
