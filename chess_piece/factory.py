from chess_piece.queen import ChessQueen
from chess_piece.rook import ChessRook
from chess_piece.bishop import ChessBishop
from chess_piece.knights import ChessKnight


class ChessPieceFactory:
    @staticmethod
    def execute_creation_order(chess_piece_order):
        created_chess_pieces = {}
        for order in chess_piece_order:
            piece_color, piece_type, number_of_pieces = order

            if piece_color not in created_chess_pieces:
                created_chess_pieces[piece_color] = {}

            if piece_type not in created_chess_pieces[piece_color]:
                created_chess_pieces[piece_color][piece_type] = []

            for _ in range(0, number_of_pieces):
                chess_piece = ChessPieceFactory.create_chess_piece(piece_type, piece_color)
                created_chess_pieces[piece_color][piece_type].append(chess_piece)

        return created_chess_pieces

    @staticmethod
    def create_chess_piece(piece_type, piece_color):
        if piece_type.lower() == "queen":
            return ChessQueen(piece_color)

        elif piece_type.lower() == "rook":
            return ChessRook(piece_color)

        elif piece_type.lower() == "bishop":
            return ChessBishop(piece_color)

        elif piece_type.lower() == "knight":
            return ChessKnight(piece_color)
