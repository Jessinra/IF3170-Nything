from Chess_piece import ChessPiece
from Chess_board import ChessBoard

class ChessKnight(ChessPiece):

    def __init__(self, color):
        
        self.type = "Knight"
        self.color = color

    def get_attack_pattern(self):

        pass