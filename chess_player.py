class ChessPlayer:
    def __init__(self, board, solver):
        self.chess_board = board    # To be deleted...
        self.solver = solver

    def solve(self, iteration_count=0):
        for _ in range(iteration_count):

            try:
                self.solver.next_step()
            except:
                pass

    def experiment_solve(self, iteration_count=0):
        for _ in range(iteration_count):

            try:
                # For research / experiment purpose, 
                return self.solver.experiment_next_step()
            except:
                pass
