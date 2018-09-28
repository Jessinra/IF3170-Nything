from solver.hill_climbing import HillClimbing
import random


class FullScanHillClimbing(HillClimbing):
    def __init__(self, chess_board):
        super().__init__(chess_board)
    
    def get_new_move(self):
        moved_piece = random.choice(self.chess_board.pieces)

        optimal_score = self.current_score
        optimal_position = moved_piece.position

        for empty_tile in self.get_empty_tiles():
            move_score = self.evaluate_move(moved_piece, empty_tile)
            if move_score >= optimal_score:
                optimal_score = move_score
                optimal_position = empty_tile

        return moved_piece, optimal_position