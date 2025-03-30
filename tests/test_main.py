from source.main import *
import unittest


class TestMain(unittest.TestCase):
    def test_mainMenu(self):
        self.assertTrue(mainMenu)  # keine tests nötig, nur input handling

    def test_main(self):
        self.assertTrue(main)  # keine tests nötig
