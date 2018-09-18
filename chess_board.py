import constants


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
        self.pieces = {} # For GA purpose

    def __str__(self):
        return '\n'.join([''.join(['.' if piece is None else str(piece) for piece in row]) for row in self.board])

    def initialize_board(self):
        # Set all row col to None
        for r in range(self.max_row):
            if r not in self.board:
                self.board[r] = {}
            for c in range(self.max_col):
                self.board[r][c] = None

    def add_piece_to_board(self, chess_piece):
        # Set board[row][col] to the chess piece
        r, c = chess_piece.position
        self.board[r][c] = chess_piece
    
    def get_tile_status(self, position):
        # Return board[row][col]
        r, c = position
        return self.board[r][c] is not None

    def update_chess_piece(self, chess_piece, from_position):
        r, c = from_position
        self.board[r][c] = None
        r, c = chess_piece.position
        self.board[r][c] = chess_piece
