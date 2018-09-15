from File_parser import FileParser
from Chess_queen import ChessQueen
from Chess_rook import ChessRook
from Chess_bishop import ChessBishop
from Chess_knights import ChessKnight

class ChessPieceFactory:

    @staticmethod
    def process_creation_order(chess_piece_order):

        created_chess_pieces = {}

        for order in chess_piece_order:
            
            piece_color = order[0]
            piece_type = order[1]
            number_of_pieces = order[2]

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
