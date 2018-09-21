from solver.incremental_solver import IncrementalSolver
import random


class SimulatedAnnealing(IncrementalSolver):
    def __init__(self, chess_board, threshold_generator):
        super().__init__(chess_board)
        self.step = 0
        self.threshold_generator = threshold_generator

    def next_step(self):
        moved_piece = random.choice(self.chess_board.pieces)
        new_position = random.choice(self.get_empty_tiles())

        current_score = self.evaluator.evaluate(self.chess_board)
        move_score = self.evaluate_move(moved_piece, new_position)

        if self.is_good_move(current_score, move_score):
            self.move_chess_piece(moved_piece, new_position)

        elif self.is_move_accepted_by_chances(current_score - move_score):
            self.move_chess_piece(moved_piece, new_position)

        self.step += 1

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

    def is_move_accepted_by_chances(self, score_difference):
        return random.uniform(0, 1) <= self.get_threshold(score_difference, self.step)
        
    def get_threshold(self, score_difference, step):
        return self.threshold_generator.calculate_threshold(score_difference, step)


