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
        attack_pattern = {}
        
        # N dirrection
        attack_pattern['N'] = []
        for i in range(current_row, ChessBoard.max_row):
            attack_pattern['N'].append((current_row + i, current_col))

        # E dirrection
        attack_pattern['E'] = []
        for i in range(current_col, ChessBoard.max_col):
            attack_pattern['E'].append((current_row, current_col + i))

        attack_pattern['NE'] = []
        pass # ... dst

        return attack_pattern





