from random import randint


class ChessBoard:
    initialized = False
    min_row = 0
    max_row = 8 
    min_col = 0
    max_col = 8
    
    def __init__(self):
        # Disabled due to GA (population of chess boards needed)
        # if ChessBoard.initialized :
        #    raise Exception("ChessBoard has already been initialized")

        # Implement this
        self.board = {}
        self.pieces = [] # For GA purpose

    def __str__(self):
        result = ""
        for row in range(self.max_row):
            for col in range(self.max_col):
                piece = self.board[row][col]
                if piece is None:
                    result += "."
                else:
                    result += str(piece)
            result += "\n"

        return result

    def initialize_board(self):
        # Set all row col to None
        for row in range(self.max_row):
            if row not in self.board:
                self.board[row] = {}
            for col in range(self.max_col):
                self.board[row][col] = None

    def add_piece_randomly(self, chess_piece):
        placed = False
        while not placed:
            row = randint(self.min_row, self.max_row-1)
            col = randint(self.min_col, self.max_col-1)
            position = (row, col)
            placed = not self.get_tile_status(position)
            chess_piece.position = position
            self.add_piece_to_board(chess_piece)

    def add_piece_to_board(self, chess_piece):
        # Set board[row][col] to the chess piece
        row, col = chess_piece.position
        self.board[row][col] = chess_piece
        if chess_piece not in self.pieces:
            self.pieces.append(chess_piece)

    def get_piece_on_tile(self, position):
        row, col = position
        return self.board[row][col]

    def get_tile_status(self, position):
        # Return board[row][col] (chesspiece)
        row, col = position
        return self.board[row][col] is not None

    def get_tile_color(self, position):
        """ Used by evaluator for scoring purposes """

        chess_piece = self.get_tile_status(position)
        return chess_piece.color if chess_piece is not None else None

    def update_chess_piece(self, chess_piece, from_position):
        row, col = from_position
        self.board[row][col] = None
        row, col = chess_piece.position
        self.board[row][col] = chess_piece
