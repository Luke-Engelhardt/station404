import random

def placeTraps(spaceship):
    for i in range(len(spaceship)):
        for j in range(len(spaceship)):
            if random.randint(1, 7) == 1:
                spaceship[i][j] = 1
    return spaceship
    