from chess_board import ChessBoard


class ChessPlayer:
    def __init__(self, board, solver):
        self.chess_board = board
        self.solver = solver

    def solve(self, iteration_count=0):
        for _ in range(iteration_count):
            
            # chess_piece, position = self.solver.next_step()
            # self.move_chess_piece(chess_piece, position)

            # solver return none,
            try:
                self.solver.next_step()
            except:
                pass