from solver.base_solver import BaseSolver
import random


class SimulatedAnnealing(IncrementalSolver):
    def __init__(self, chess_board, temperature, ratio):
        super().__init__(chess_board)
        self.temperature = temperature
        self.ratio = ratio

    def next_step(self):
        moved_piece = random.choice(self.chess_board.pieces)
        new_position = random.choice(self.get_empty_tiles())

        current_score = self.evaluator.evaluate(self.chess_board)
        move_score = self.evaluate_move(moved_piece, new_position)

        self.temperature /= self.ratio
        if move_score > current_score or random.uniform(0, 1) <= 0.5:
            return (moved_piece, new_position)
        else
            return None

    def get_empty_tiles(self):

        empty_tiles = []
        for i in range(self.chess_board.min_row, self.chess_board.max_row):
            for j in range(self.chess_board.min_col, self.chess_board.max_col):
                tiles = self.chess_board.get_tile_status((i, j))
                
                if tiles is None: 
                    empty_tiles.append((i, j))

        return empty_tiles