from solver.base_solver import BaseSolver


class SimulatedAnnealing(BaseSolver):
    def __init__(self, chess_board):
        super().__init__(chess_board)

    def next_step(self):
        pass
