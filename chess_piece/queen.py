from chess_piece.base_piece import ChessPiece
from chess_board import ChessBoard


class ChessQueen(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.type = "Queen"

    def __str__(self):
        return 'Q' if self.color == 'w' else 'q'

    def get_attack_pattern(self):
        current_row, current_col = self.position
        attack_pattern = self.default_attack_pattern
        
        for i in range(current_row):
            attack_pattern['N'].append((current_row - i, current_col))

        for i in range(current_col, ChessBoard.max_col):
            attack_pattern['E'].append((current_row, current_col + i))

        for i in range(current_row, ChessBoard.max_row):
            attack_pattern['S'].append((current_row + i, current_col))

        for i in range(current_col):
            attack_pattern['E'].append((current_row, current_col - i))

        shortest = min(current_col, current_row)
        for i in range(shortest):
            attack_pattern['NE'].append((current_row - i, current_col - i))

        shortest = min(ChessBoard.max_col - current_col, current_row)
        for i in range(shortest):
            attack_pattern['NW'].append((current_row - i, current_col + i))

        shortest = min(current_col, ChessBoard.max_col - current_row)
        for i in range(shortest):
            attack_pattern['SW'].append((current_row + i, current_col - i))

        shortest = min(ChessBoard.max_col - current_col, ChessBoard.max_col - current_row)
        for i in range(shortest):
            attack_pattern['SE'].append((current_row + i, current_col + i))

        return attack_pattern





