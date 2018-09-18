from chess_piece.base_piece import ChessPiece


class ChessBishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.type = "Bishop"

    def __str__(self):
        return 'B' if self.color == 'w' else 'b'

    def get_attack_pattern(self):
        pass
