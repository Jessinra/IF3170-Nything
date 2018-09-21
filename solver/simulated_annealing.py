from solver.incremental_solver import IncrementalSolver
import random


class SimulatedAnnealing(IncrementalSolver):
    def __init__(self, chess_board, threshold_generator):
        super().__init__(chess_board)
        self.step = 0
        self.threshold_generator = threshold_generator

    def next_step(self):
        moved_piece, new_position = self.get_random_neighbour()
        move_score = self.evaluate_move(moved_piece, new_position)

        if self.is_good_move(move_score) or self.should_bad_move_be_accepted(move_score):
            self.move_chess_piece(moved_piece, new_position)
            self.current_score = move_score

        self.step += 1

    def get_random_neighbour(self):
        return random.choice(self.chess_board.pieces), random.choice(self.get_empty_tiles())

    def get_empty_tiles(self):
        empty_tiles = []
        for i in range(self.chess_board.min_row, self.chess_board.max_row):
            for j in range(self.chess_board.min_col, self.chess_board.max_col):
                tiles = self.chess_board.get_tile_status((i, j))
                
                if not tiles:
                    empty_tiles.append((i, j))

        return empty_tiles

    def is_good_move(self, move_score):
        return move_score > self.current_score

    def should_bad_move_be_accepted(self, bad_move_score):
        return random.random() < self.get_threshold(self.current_score - bad_move_score, self.step)
        
    def get_threshold(self, score_difference, step):
        return self.threshold_generator.calculate_threshold(score_difference, step)


