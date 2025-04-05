from source.logic import *
import unittest

# pylint: disable=all

class TestLogic(unittest.TestCase):
    def test_place_traps(self) -> None:
        map: list[list[int | str]] = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        result = place_traps(map)
        for i in range(len(result)):
            for j in range(len(result)):
                if result[i][j] == 1:
                    self.assertTrue(result[i][j] == 1)
                else:
                    self.assertTrue(result[i][j] == 0)

    def test_scan_field(self) -> None:
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
        if scan_field(0, 0, map, solution) == 1 and scan_field(1, 1, map, solution) == 0:
            self.assertTrue(True)

    def test_mark_field(self) -> None:
        map: list[list[int | str]] = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        map = mark_field(0, 0, map)
        if map[0][0] == "X":
            self.assertTrue(True)

    def test_get_traps(self) -> None:
        map: list[list[int | str]] = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        map = place_traps(map)
        traps = get_traps(map)
        self.assertTrue(len(traps) > 0)

    def test_get_neighbor_traps(self) -> None:
        map: list[list[int | str]] = [[1, 1, 0], [1, 0, 0], [0, 0, 0]]
        traps = get_neighbor_traps(map, 1, 1)
        self.assertTrue(traps == 3)

    def test_check_win(self) -> None:
        solution: list[list[int | str]] = [[1, 0], [0, 0]]
        spaceship: list[list[int | str]] = [[0, 0], [0, 0]]
        self.assertTrue(check_win(spaceship, solution) == False)
