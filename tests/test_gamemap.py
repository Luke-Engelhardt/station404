from source.gamemap import Map
import unittest
import io
import sys

# pylint: disable=all

class TestGameMap(unittest.TestCase):
    def setUp(self):
        self.held_output = io.StringIO()
        sys.stdout = self.held_output
        self.game_map = Map()

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_make_map_size(self) -> None:
        result = self.game_map.make_map(3)
        self.assertEqual(len(result), 3)
        self.assertEqual(len(result[0]), 3)

    def test_make_map_initialization(self) -> None:
        result = self.game_map.make_map(2)
        for row in result:
            for cell in row:
                self.assertEqual(cell, 0)

    def test_make_map_edge_case(self) -> None:
        result = self.game_map.make_map(1)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 1)

    def test_print_map(self) -> None:
        test_map = [[0, 1], [1, 0]]
        self.game_map.print_map(test_map)
        output = self.held_output.getvalue()
        self.assertIn('0 1', output)
        self.assertIn('1 0', output)
        self.assertIn('|', output)
        self.assertIn('-', output)
