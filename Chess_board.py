

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

    def initialize_board(self):
        pass

    def add_piece_to_board(self, chess_piece):
        pass
    
    

    def get_tile_status(self, positiion):
        pass