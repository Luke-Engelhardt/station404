from source.gamemap import map
import unittest


class TestGameMap(unittest.TestCase):
    def test_makeMap(self):
        game_map = map()
        result = game_map.makeMap(3)
        self.assertTrue(len(result) == 3)
        self.assertTrue(result[0][0] == 0)

    def test_printMap(self):
        game_map = map()
        test_map = [[0, 1], [1, 0]]
        game_map.printMap(test_map)
        self.assertTrue(True)
