from chess_board import ChessBoard


class ChessPlayer:
    def __init__(self, solver):
        self.chess_board = ChessBoard()
        self.solver = solver

    def solve(self, iteration_count=0):
        for _ in range(iteration_count):
            
            # chess_piece, position = self.solver.next_step()
            # self.move_chess_piece(chess_piece, position)

            # solver return none, 
            self.solver.next_step()