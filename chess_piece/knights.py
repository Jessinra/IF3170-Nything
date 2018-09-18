from chess_piece.base_piece import ChessPiece


class ChessKnight(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.type = "Knight"

    def __str__(self):
        return 'K' if self.color == 'w' else 'k'

    def get_attack_pattern(self):
        current_row, current_col = self.position
        attack_pattern = self.default_attack_pattern

        return attack_pattern