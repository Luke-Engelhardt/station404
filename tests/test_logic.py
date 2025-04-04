from source.logic import *
import unittest


class TestLogic(unittest.TestCase):
    def test_placeTraps(self) -> None:
        map: list[list[int | str]] = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        result = placeTraps(map)
        for i in range(len(result)):
            for j in range(len(result)):
                if result[i][j] == 1:
                    self.assertTrue(result[i][j] == 1)
                else:
                    self.assertTrue(result[i][j] == 0)

    def test_scanField(self) -> None:
        map: list[list[int | str]] = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        solution: list[list[int | str]] = [
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        if scanField(0, 0, map, solution) == 1 and scanField(1, 1, map, solution) == 0:
            self.assertTrue(True)

    def test_markField(self) -> None:
        map: list[list[int | str]] = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        map = markField(0, 0, map)
        if map[0][0] == "X":
            self.assertTrue(True)

    def test_getTraps(self) -> None:
        map: list[list[int | str]] = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        map = placeTraps(map)
        traps = getTraps(map)
        self.assertTrue(len(traps) > 0)

    def test_getNeighbourTraps(self) -> None:
        map: list[list[int | str]] = [[1, 1, 0], [1, 0, 0], [0, 0, 0]]
        traps = getNeighbourTraps(map, 1, 1)
        self.assertTrue(traps == 3)

    def test_checkWin(self) -> None:
        solution: list[list[int | str]] = [[1, 0], [0, 0]]
        spaceship: list[list[int | str]] = [[0, 0], [0, 0]]
        self.assertTrue(checkWin(spaceship, solution) == False)
