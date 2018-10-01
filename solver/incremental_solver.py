from solver.base_solver import BaseSolver

class IncrementalSolver(BaseSolver):
    def __init__(self, chess_board):
        super().__init__()
        self.chess_board = chess_board
        _, _, self.current_score = self.evaluator.evaluate(self.chess_board)

    def get_new_move(self):
        raise RuntimeError("Method not implemented yet!")

    def move_chess_piece(self, chess_piece, new_position):
        piece_on_new_position = self.chess_board.get_piece_on_tile(new_position)

        if piece_on_new_position is None:
            self.chess_board.set_tiles_value(chess_piece.position, None)
        else:
            self.chess_board.set_tiles_value(chess_piece.position, piece_on_new_position)
            piece_on_new_position.move(chess_piece.position)

        self.chess_board.set_tiles_value(new_position, chess_piece)
        chess_piece.move(new_position)

    def evaluate_move(self, moved_piece, new_position):
        # Store original position as we need to move the piece for evaluation
        old_position = moved_piece.position

        # Try to forecast score
        self.move_chess_piece(moved_piece, new_position)
        _, _, score = self.evaluator.evaluate(self.chess_board)

        # Revert back to original position
        self.move_chess_piece(moved_piece, old_position)

        return score

    def is_good_move(self, move_score):
        return self.current_score <= move_score
