from board import Board
import unittest
from config import WHITE, BLACK, EMPTY

test_list = [
    ((4, 4, WHITE), [(2, 4), (4, 2)]),
    # ((4, 4, BLACK), [(2, 2)]),
    # ((3, 3, WHITE), [(3, 5), (5, 3)]),
    ]

class TestBoard(unittest.TestCase):
    def test_lookup(self):
        for input, expected in test_list:
            with self.subTest():
                b = Board()
                (row, column, color) = input
                self.assertEqual(b.lookup(row, column, color), expected)
if __name__ == '__main__':
    unittest.main()