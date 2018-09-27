import unittest
from chess_board import ChessBoard

class TestBoard(unittest.TestCase):
    
    def setUp(self):
        self.display_test_name()

    def display_test_name(self):
        print ("Checking {}".format(self.id()))

    def test_to_str_empty_board(self):

        board = ChessBoard()
        expected = "........\n........\n........\n........\n........\n........\n........\n........\n"

        self.assertEqual(str(board), expected)


if __name__ == "__main__":


    unittest.main()