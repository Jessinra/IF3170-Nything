from random import randint, choice
from chess_piece.factory import ChessPieceFactory
import chess_constant


class ChessBoard:
    min_row = chess_constant.MIN_ROW
    max_row = chess_constant.MAX_ROW
    min_col = chess_constant.MIN_COL
    max_col = chess_constant.MAX_COL

    def __init__(self):
        self.board = {}
        self.pieces = []  # For GA purpose
        self.initialize_empty_board()

    @classmethod
    def load_board(cls, orders):
        instance = cls()

        for order in orders:
            for _ in range(order['count']):
                chess_piece = ChessPieceFactory.create_chess_piece(order['type'], order['color'])
                instance.add_piece_randomly(chess_piece)

    def initialize_empty_board(self):
        for row in range(self.max_row):
            if row not in self.board:
                self.create_new_row(row)
            for col in range(self.max_col):
                self.set_tiles_value((row, col), None)

    def create_new_row(self, row):
        self.board[row] = {}

    def set_tiles_value(self, position, value):
        row, col = position
        self.board[row][col] = value

    def add_piece_randomly(self, chess_piece):
        if (len(self.pieces) == self.max_col * self.max_row):
            return

        positions = []
        for i in range(self.max_row):
            for j in range(self.max_col):
                if not self.is_tile_empty((i, j)):
                    continue
                positions.append((i,j))

        pos = choice(positions)
        chess_piece.position = pos
        self.add_piece_to_board(chess_piece)

    def add_piece_to_board(self, chess_piece):
        self.set_tiles_value(chess_piece.position, chess_piece)

        if chess_piece not in self.pieces:
            self.pieces.append(chess_piece)

    def is_tile_empty(self, position):
        return self.get_piece_on_tile(position) is None

    def get_tile_color(self, position):
        """ Used by evaluator for scoring purposes """

        chess_piece = self.get_piece_on_tile(position)
        return chess_piece.color if chess_piece is not None else None

    def get_piece_on_tile(self, position):
        row, col = position
        return self.board[row][col]

    def update_chess_piece(self, chess_piece, previous_position):
        self.set_tiles_value(previous_position, None)
        self.set_tiles_value(chess_piece.position, chess_piece)

    def __str__(self):

        result = ""
        for row in range(self.max_row):
            for col in range(self.max_col):
                piece = self.get_piece_on_tile((row, col))
                if piece is None:
                    result += "."
                else:
                    result += str(piece)

            result += "\n"

        return result
