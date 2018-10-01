import unittest
from chess_board import ChessBoard
from chess_piece.rook import Rook
from chess_piece.bishop import Bishop
from chess_piece.knights import Knight
from solver.state_evaluator import StateEvaluator


class TestEvaluator(unittest.TestCase):
    evaluator = StateEvaluator()

    def setUp(self):
        self.display_test_name()
        self.prepare_board()

    def display_test_name(self):
        print("Checking {}".format(self.id()))

    def prepare_board(self):
        self.board = ChessBoard()

    def evaluate_score(self):
        _, _, score = TestEvaluator.evaluator.evaluate(self.board)
        return score

    def test_same_color_attack(self):
        piece_01 = Rook("white")
        piece_02 = Rook("white")

        piece_01.position = (3, 3)
        piece_02.position = (3, 6)

        self.board.add_piece_to_board(piece_01)
        self.board.add_piece_to_board(piece_02)

        expected_score = -2
        self.assertEqual(self.evaluate_score(), expected_score)

    def test_diff_color_attack(self):
        piece_01 = Rook("white")
        piece_02 = Rook("black")

        piece_01.position = (3, 3)
        piece_02.position = (3, 6)

        self.board.add_piece_to_board(piece_01)
        self.board.add_piece_to_board(piece_02)

        expected_score = 2
        self.assertEqual(self.evaluate_score(), expected_score)

    def test_same_color_asymetry_attack(self):
        piece_01 = Rook("white")
        piece_02 = Bishop("white")

        piece_01.position = (3, 3)
        piece_02.position = (3, 6)

        self.board.add_piece_to_board(piece_01)
        self.board.add_piece_to_board(piece_02)

        expected_score = -1
        self.assertEqual(self.evaluate_score(), expected_score)

    def test_diff_color_asymetry_attack(self):
        piece_01 = Rook("white")
        piece_02 = Bishop("black")

        piece_01.position = (3, 3)
        piece_02.position = (3, 6)

        self.board.add_piece_to_board(piece_01)
        self.board.add_piece_to_board(piece_02)

        expected_score = 1
        self.assertEqual(self.evaluate_score(), expected_score)

    def test_non_attack(self):
        piece_01 = Rook("white")
        piece_02 = Bishop("black")

        piece_01.position = (3, 3)
        piece_02.position = (4, 6)

        self.board.add_piece_to_board(piece_01)
        self.board.add_piece_to_board(piece_02)

        expected_score = 0
        self.assertEqual(self.evaluate_score(), expected_score)

    def test_inline_attack(self):
        piece_01 = Rook("white")
        piece_02 = Bishop("white")
        piece_03 = Bishop("black")  # hiding behind piece 2

        piece_01.position = (3, 3)
        piece_02.position = (3, 4)
        piece_03.position = (3, 5)

        self.board.add_piece_to_board(piece_01)
        self.board.add_piece_to_board(piece_02)
        self.board.add_piece_to_board(piece_03)

        expected_score = -1
        self.assertEqual(self.evaluate_score(), expected_score)

    def test_inline_attackII(self):
        piece_01 = Rook("white")
        piece_02 = Bishop("black")
        piece_03 = Bishop("black")  # hiding behind piece 2

        piece_01.position = (3, 3)
        piece_02.position = (3, 4)
        piece_03.position = (3, 5)

        self.board.add_piece_to_board(piece_01)
        self.board.add_piece_to_board(piece_02)
        self.board.add_piece_to_board(piece_03)

        expected_score = 1
        self.assertEqual(self.evaluate_score(), expected_score)

    def test_multi_direction_attack(self):
        piece_01 = Rook("white")
        piece_02 = Bishop("white")
        piece_03 = Bishop("black")  # hiding behind piece 2

        piece_01.position = (3, 3)
        piece_02.position = (3, 1)
        piece_03.position = (3, 5)

        self.board.add_piece_to_board(piece_01)
        self.board.add_piece_to_board(piece_02)
        self.board.add_piece_to_board(piece_03)

        expected_score = 0  # +1 -1
        self.assertEqual(self.evaluate_score(), expected_score)

    def test_knight_attack(self):
        piece_01 = Rook("white")
        piece_02 = Knight("white")

        piece_01.position = (3, 3)
        piece_02.position = (5, 4)

        self.board.add_piece_to_board(piece_01)
        self.board.add_piece_to_board(piece_02)

        expected_score = -1
        self.assertEqual(self.evaluate_score(), expected_score)


if __name__ == "__main__":
    unittest.main()
