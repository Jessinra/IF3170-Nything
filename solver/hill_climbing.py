from solver.incremental_solver import IncrementalSolver
import random
import abc

class HillClimbing(IncrementalSolver):
    def __init__(self, chess_board):
        super().__init__(chess_board)

    def next_step(self):
        moved_piece, new_position = self.get_new_move()
        move_score = self.evaluate_move(moved_piece, new_position)

        if self.is_good_move(move_score):
            self.move_chess_piece(moved_piece, new_position)
            self.current_score = move_score

    def experiment_next_step(self):    
        moved_piece, new_position = self.get_new_move()
        move_score = self.evaluate_move(moved_piece, new_position)

        # Experimental purpose
        diff = self.current_score - move_score

        if self.is_good_move(move_score):
            self.move_chess_piece(moved_piece, new_position)
            self.current_score = move_score

        # Experimental purpose
        return diff