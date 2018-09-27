import unittest
from chess_piece.queen import Queen
from chess_piece.rook import Rook
from chess_piece.bishop import Bishop
from chess_piece.knights import Knight

class TestAttackPattern(unittest.TestCase):
    def setUp(self):
        self.display_test_name()

    def display_test_name(self):
        print ("Checking {}".format(self.id()))
    def test_queen(self):

        queen = Queen("white")
        queen.position = (5,5)
        expected = {'E': [(5, 6), (5, 7)],
                    'N': [(4, 5), (3, 5), (2, 5), (1, 5), (0, 5)],
                    'NE': [(4, 6), (3, 7)],
                    'NW': [(4, 4), (3, 3), (2, 2), (1, 1), (0, 0)],
                    'S': [(6, 5), (7, 5)],
                    'SE': [(6, 6), (7, 7)],
                    'SW': [(6, 4), (7, 3)],
                    'W': [(5, 4), (5, 3), (5, 2), (5, 1), (5, 0)]}

        self.assertEqual(queen.get_attack_pattern(), expected)

    def test_rook(self):
        rook = Rook("white")
        rook.position = (5,5)
        expected = {'E': [(5, 6), (5, 7)],
                    'N': [(4, 5), (3, 5), (2, 5), (1, 5), (0, 5)],
                    'NE': [],
                    'NW': [],
                    'S': [(6, 5), (7, 5)],
                    'SE': [],
                    'SW': [],
                    'W': [(5, 4), (5, 3), (5, 2), (5, 1), (5, 0)]}

        self.assertEqual(rook.get_attack_pattern(), expected)

    def test_bishop(self):
        bishop = Bishop("white")
        bishop.position = (5,5)
        expected = {'E': [],
                    'N': [],
                    'NE': [(4, 6), (3, 7)],
                    'NW': [(4, 4), (3, 3), (2, 2), (1, 1), (0, 0)],
                    'S': [],
                    'SE': [(6, 6), (7, 7)],
                    'SW': [(6, 4), (7, 3)],
                    'W': []}

        self.assertEqual(bishop.get_attack_pattern(), expected)

    def test_knight(self):

        knight = Knight("white")
        knight.position = (5,5)
        expected = {'N': [(3, 6), (4, 7), (6, 7), (7, 6), (7, 4), (6, 3), (4, 3), (3, 4)]}

        self.assertEqual(knight.get_attack_pattern(), expected)

if __name__ == "__main__":
    unittest.main()