from solver.hill_climbing import HillClimbing
import random


class StochasticHillClimbing(HillClimbing):
    def __init__(self, chess_board):
        super().__init__(chess_board)
    
    def get_new_move(self):
        return random.choice(self.chess_board.pieces), random.choice(self.chess_board.get_all_tiles())