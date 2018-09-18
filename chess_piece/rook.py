from chess_piece.base_piece import ChessPiece


class ChessRook(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.type = "Rook"

    def __str__(self):
        return 'R' if self.color == 'w' else 'r'

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
