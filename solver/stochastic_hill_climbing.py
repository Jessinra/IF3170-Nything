from solver.incremental_solver import IncrementalSolver
import random


class StochasticHillClimbing(IncrementalSolver):
    def __init__(self, chess_board):
        super().__init__(chess_board)

    def next_step(self):
        empty_tiles = self.get_empty_tiles()
        moved_piece = random.choice(self.chess_board.pieces)

        self.current_score = self.evaluator.evaluate(self.chess_board)

        position = random.choice(empty_tiles)
        move_score = self.evaluate_move(moved_piece, position)

        if self.is_good_move(move_score):
            self.move_chess_piece(moved_piece, position)
