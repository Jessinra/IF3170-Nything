from chess_piece.base_piece import ChessPiece
from chess_constant import ChessConstants


class ChessRook(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.type = "Rook"

    def __str__(self):
        return 'R' if self.color == 'w' else 'r'

    def get_attack_pattern(self):
        current_row, current_col = self.position
        attack_pattern = self.get_default_attack_pattern()

        for i in range(current_row):
            attack_pattern['N'].append((current_row - i - 1, current_col))

        for i in range(ChessConstants.max_col-current_col-1):
            attack_pattern['E'].append((current_row, current_col + i + 1))

        for i in range(ChessConstants.max_row-current_row-1):
            attack_pattern['S'].append((current_row + i + 1, current_col))

        for i in range(current_col):
            attack_pattern['W'].append((current_row, current_col - i -1))

        return attack_pattern
