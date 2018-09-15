

class ChessBoard:

    initialized = False

    min_row = 0
    max_row = 8
    min_col = 0
    max_col = 8
    
    def __init__(self):

        if ChessBoard.initialized :
            raise Exception("ChessBoard has already been initialized")

        # Implement this
        self.board = {}
        self.pieces = {} # For GA purpose
        pass

    def __str__(self):
        return '\n'.join([''.join(['.' if piece is None else str(piece) for piece in row]) for row in self.board])

    def initialize_board(self):

        # Set all row col to None
        pass

    def add_piece_to_board(self, chess_piece):

        # Set board[row][col] to the chess piece
        pass
    
    def get_tile_status(self, position):

        # Return board[row][col]
        pass