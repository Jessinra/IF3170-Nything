class ChessPlayer:
    def __init__(self, board, solver):
        self.chess_board = board
        self.solver = solver

    def solve(self, iteration_count=0):
        for _ in range(iteration_count):

            try:
                self.solver.next_step()
            except:
                pass
