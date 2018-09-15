from Chess_piece import ChessPiece
from Chess_board import ChessBoard

class ChessRook(ChessPiece):

    def __init__(self, color):
       
        self.type = "Rook"
        self.color = color

    def __str__(self):
        return 'R' if self.color == 'w' else 'r'

    def get_attack_pattern(self):

        pass