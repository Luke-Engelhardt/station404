import gamemap
import logic

def __init__(self):
    pass

def main():
    pass

if __name__ == "__main__":
    map = gamemap.map()
    solution = gamemap.map()
    spaceship = map.makeMap(10)
    solution = logic.placeTraps(solution.makeMap(10))
    map.printMap(spaceship)
    map.printMap(logic.markField(3, 5, spaceship))
    logic.welcome()
    logic.mainMenu()
    
    