from Chess_piece import ChessPiece
from Chess_board import ChessBoard

class ChessBishop(ChessPiece):

    def __init__(self, color):

        self.type = "Bishop"
        self.color = color

    def __str__(self):
        return 'B' if self.color == 'w' else 'b'

    def get_attack_pattern(self):

        pass