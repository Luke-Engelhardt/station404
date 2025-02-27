import gamemap
import logic
import os

def __init__(self):
    pass

def mainMenu():
    print("1. Start game")
    print("2. Instructions")
    print("3. Quit")
    choice = input("Please select an option: ")
    if choice == "1":
        main()
    elif choice == "2":
        logic.instructions()
    elif choice == "3":
        print('Goodbye...')
        quit()
    else:
        print("Invalid input. Please try again.")

def main():
    map = gamemap.map()
    solution = gamemap.map()
    spaceship = map.makeMap(8)
    solution = logic.placeTraps(solution.makeMap(8))
    playerWon = False
    
    while not logic.checkWin(spaceship, solution):
        logic.clearTerminal()
        print('1. View Spacestation')
        print('2. Scan Field')
        print('3. Mark Field')
        choice = input("Please select an option: ")
        
        if choice == "1":
            logic.clearTerminal()
            map.printMap(spaceship)
            input("Press enter to continue...")
        elif choice == "2":
            logic.clearTerminal()
            map.printMap(spaceship)
            y = int(input("Please enter the x coordinate: "))  
            x = int(input("Please enter the y coordinate: "))  
            if logic.scanField(x, y, spaceship, solution) == 1:
                print("You stepped into a trap. GAME OVER!")
                break
            else:
                print("You didn't find a trap.")
        elif choice == "3":
            logic.clearTerminal()
            map.printMap(spaceship)
            y = int(input("Please enter the x coordinate: "))  
            x = int(input("Please enter the y coordinate: ")) 
            spaceship = logic.markField(x, y, spaceship)
        else:
            print("Invalid input. Please try again.")
    if playerWon:
        print("Congratulations! You won!")
    else:
        print("Thanks for playing!")
if __name__ == "__main__":
    logic.welcome()
    while True:
        mainMenu()
        logic.clearTerminal()
    
        