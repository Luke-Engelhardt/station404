"""Main game module, handling user input and gameplay loop"""

import sys
from source import gamemap
from source import logic


def main_menu() -> None:
    """Main menu function to start game or show instructions"""
    print("1. Start game")
    print("2. Instructions")
    print("3. Quit")
    choice = input("Please select an option: ")
    if choice == "1":
        main()
    elif choice == "2":
        logic.instructions()
    elif choice == "3":
        print("Goodbye...")
        sys.exit()
    else:
        print("Invalid input. Please try again.")


def main() -> None:
    """Main function for gameplay loop"""
    game_map = gamemap.Map()
    solution_map = gamemap.Map()
    spaceship = game_map.make_map(8)
    solution = solution_map.make_map(8)
    solution = logic.place_traps(solution)
    player_won = False

    while not logic.check_win(spaceship, solution):
        logic.clear_terminal()
        print("1. View Spacestation")
        print("2. Scan Field")
        print("3. Mark Field")
        choice = input("Please select an option: ")

        if choice == "1":
            logic.clear_terminal()
            game_map.print_map(spaceship)
            input("Press enter to continue...")
        elif choice == "2":
            logic.clear_terminal()
            game_map.print_map(spaceship)
            try:
                y = int(input("Please enter the x coordinate: "))
                x = int(input("Please enter the y coordinate: "))
                if x < 0 or x > 7 or y < 0 or y > 7:
                    print("Invalid coordinates! Please enter numbers between 0 and 7.")
                    continue
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue
            if logic.scan_field(x, y, spaceship, solution) == 1:
                print("You stepped into a trap. GAME OVER!")
                input("Press ENTER to go back to the main menu...")
                break
            print("You didn't find a trap.")
        elif choice == "3":
            logic.clear_terminal()
            game_map.print_map(spaceship)
            try:
                y = int(input("Please enter the x coordinate: "))
                x = int(input("Please enter the y coordinate: "))
                if x < 0 or x > 7 or y < 0 or y > 7:
                    print("Invalid coordinates! Please enter numbers between 0 and 7.")
                    continue
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue
            spaceship = logic.mark_field(x, y, spaceship)
        else:
            print("Invalid input. Please try again.")
    if player_won:
        print("Congratulations! You won!")
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    logic.welcome()
    while True:
        main_menu()
        logic.clear_terminal()
#Author: Luke Engelhardt
#Version: 1.0