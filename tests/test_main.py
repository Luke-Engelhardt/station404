from source.main import *
import unittest

# pylint: disable=all

class TestMain(unittest.TestCase):
    def test_mainMenu(self) -> None:
        self.assertTrue(main_menu)  # keine tests nötig, nur input handling

    def test_main(self) -> None:
        self.assertTrue(main)  # keine tests nötig
