from solver.incremental_solver import IncrementalSolver
import random


class FullScanHillClimbing(IncrementalSolver):
    def __init__(self, chess_board):
        super().__init__(chess_board)

    def next_step(self):
        empty_tiles = self.get_empty_tiles()
        moved_piece = random.choice(self.chess_board.pieces)

        self.current_score = self.evaluator.evaluate(self.chess_board)
        maximum_score = self.current_score
        maximum_position = moved_piece.position

        for position in empty_tiles:
            move_score = self.evaluate_move(moved_piece, position)
            if move_score >= maximum_score:
                maximum_score = move_score
                maximum_position = position

        if self.is_good_move(maximum_score):
            self.move_chess_piece(moved_piece, maximum_position)
