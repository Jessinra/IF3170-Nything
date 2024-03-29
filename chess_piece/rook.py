from chess_piece.base_piece import ChessPiece
import chess_constant


class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.type = "Rook"

    def get_attack_pattern(self):
        current_row, current_col = self.position
        attack_pattern = self.get_default_attack_pattern()

        for i in range(current_row):
            attack_pattern['N'].append((current_row - i - 1, current_col))

        for i in range(chess_constant.MAX_COL - current_col - 1):
            attack_pattern['E'].append((current_row, current_col + i + 1))

        for i in range(chess_constant.MAX_ROW - current_row - 1):
            attack_pattern['S'].append((current_row + i + 1, current_col))

        for i in range(current_col):
            attack_pattern['W'].append((current_row, current_col - i - 1))

        return attack_pattern
