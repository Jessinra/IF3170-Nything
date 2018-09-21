
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
        for row in range(self.max_row):
            if row not in self.board:
                self.board[row] = {}
            for col in range(self.max_col):
                self.board[row][col] = None

    def add_piece_to_board(self, chess_piece):
        # Set board[row][col] to the chess piece
        row, col = chess_piece.position
        self.board[row][col] = chess_piece
    
    def get_tile_status(self, position):
        # Return board[row][col] (chesspiece)
        row, col = position
        return self.board[row][col]

    def get_tile_color(self, position):
        """ Used by evaluator for scoring purposes """

        chess_piece = self.get_tile_status(position)
        return chess_piece.color if chess_piece is not None else None

    def update_chess_piece(self, chess_piece, from_position):
        row, col = from_position
        self.board[row][col] = None
        row, col = chess_piece.position
        self.board[row][col] = chess_piece

    
        