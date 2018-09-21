from chess_piece.base_piece import ChessPiece
from chess_board import ChessBoard


class ChessBishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.type = "Bishop"

    def __str__(self):
        return 'B' if self.color == 'w' else 'b'

    def get_attack_pattern(self):
        current_row, current_col = self.position
        attack_pattern = self.get_default_attack_pattern()

        shortest = min(current_col, current_row)
        for i in range(shortest):
            attack_pattern['NE'].append((current_row - i - 1, current_col - i - 1))

        shortest = min(ChessBoard.max_col - current_col -1, current_row)
        for i in range(shortest):
            attack_pattern['NW'].append((current_row - i - 1, current_col + i + 1))

        shortest = min(current_col, ChessBoard.max_col - current_row - 1)
        for i in range(shortest):
            attack_pattern['SW'].append((current_row + i + 1, current_col - i - 1))

        shortest = min(ChessBoard.max_col - current_col - 1, ChessBoard.max_col - current_row - 1)
        for i in range(shortest):
            attack_pattern['SE'].append((current_row + i + 1, current_col + i + 1))

        return attack_pattern
