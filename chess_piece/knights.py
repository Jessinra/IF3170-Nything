from chess_piece.base_piece import ChessPiece
import chess_constant


class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.type = "Knight"

    def get_attack_pattern(self):
        current_row, current_col = self.position
        attack_pattern = self.get_default_attack_pattern()
        attack_pattern['N'] = [

            (current_row - 2, current_col + 1),  # 1 o'clock direction
            (current_row - 1, current_col + 2),  # 2 o'clock direction
            (current_row + 1, current_col + 2),  # 4 o'clock direction
            (current_row + 2, current_col + 1),  # 5 o'clock direction
            (current_row + 2, current_col - 1),  # 7 o'clock direction
            (current_row + 1, current_col - 2),  # 8 o'clock direction
            (current_row - 1, current_col - 2),  # 10 o'clock direction
            (current_row - 2, current_col - 1),  # 11 o'clock direction
        ]

        filtered_pattern = {'N': []}

        for (row, col) in attack_pattern['N']:

            if row >= chess_constant.MAX_ROW:
                continue
            elif col >= chess_constant.MAX_COL:
                continue
            elif col < 0:
                continue
            elif row < 0:
                continue

            filtered_pattern['N'].append((row, col))

        return filtered_pattern
