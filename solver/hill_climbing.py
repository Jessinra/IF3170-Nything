from solver.incremental_solver import IncrementalSolver
import random


class HillClimbing(IncrementalSolver):
    def __init__(self, chess_board):
        super().__init__(chess_board)

    def next_step(self):
        empty_tiles = self.get_empty_tiles()
        moved_piece = random.choice(self.chess_board.pieces)
        minimum_score = self.evaluator.evaluate(self.chess_board)
        minimum_position = moved_piece.position
        for position in empty_tiles:
            move_score = self.evaluate_move(moved_piece, position)
            if move_score <= minimum_score:
                minimum_score = move_score
                minimum_position = position

        current_score = self.evaluator.evaluate(self.chess_board)

        if self.is_good_move(current_score, minimum_score):
            self.move_chess_piece(moved_piece, minimum_position)

    def get_empty_tiles(self):
        empty_tiles = []
        for i in range(self.chess_board.min_row, self.chess_board.max_row):
            for j in range(self.chess_board.min_col, self.chess_board.max_col):
                tiles = self.chess_board.get_tile_status((i, j))

                if not tiles:
                    empty_tiles.append((i, j))

        return empty_tiles

    def is_good_move(self, current_score, move_score):
        return move_score > current_score


