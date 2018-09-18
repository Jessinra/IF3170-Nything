from chess_board import ChessBoard


class ChessPlayer:
    def __init__(self, solver):
        self.chess_board = ChessBoard()
        self.solver = solver

    def move_chess_piece(self, chess_piece, position):
        from_position = chess_piece.position
        chess_piece.move(position)
        self.chess_board.update_chess_piece(chess_piece, from_position)

    def solve(self, iteration_count=0):
        for _ in range(iteration_count):
            chess_piece, position = self.solver.next_step()
            self.move_chess_piece(chess_piece, position)