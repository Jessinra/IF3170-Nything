from chess_piece.base_piece import ChessPiece


class ChessRook(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.type = "Rook"

    def __str__(self):
        return 'R' if self.color == 'w' else 'r'

    def get_attack_pattern(self):
        pass
