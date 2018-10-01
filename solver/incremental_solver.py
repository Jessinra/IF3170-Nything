from solver.base_solver import BaseSolver

class IncrementalSolver(BaseSolver):
    def __init__(self, chess_board):
        super().__init__()
        self.chess_board = chess_board
        _, _, self.current_score = self.evaluator.evaluate(self.chess_board)

    def get_new_move(self):
        raise RuntimeError("Method not implemented yet!")

    def move_chess_piece(self, chess_piece, position):
        from_position = chess_piece.position
        chess_piece.move(position)
        self.chess_board.update_chess_piece(chess_piece, from_position)

    def evaluate_move(self, moved_piece, new_position):
        # Store original position as we need to move the piece for evaluation
        old_position = moved_piece.position

        # Try to forecast score
        self.move_chess_piece(moved_piece, new_position)
        _, _, score = self.evaluator.evaluate(self.chess_board)

        # Revert back to original position
        self.move_chess_piece(moved_piece, old_position)

        return score

    def get_empty_tiles(self):
        return self.chess_board.get_empty_tiles()

    def is_good_move(self, move_score):
        return self.current_score <= move_score
