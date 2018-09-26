from chess_piece.queen import Queen
from chess_piece.rook import Rook
from chess_piece.bishop import Bishop
from chess_piece.knights import Knight


class ChessPieceFactory:
    pieces = [Bishop, Queen, Rook, Knight]
    piece_class_dict = {}
    for piece in pieces:
        piece_class_dict[piece.__name__.lower()] = piece

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
        return ChessPieceFactory.piece_class_dict[piece_type](piece_color)
