from Chess_board import ChessBoard

class ChessPlayer:

    def __init__(self, solver):

        self.chess_board = ChessBoard()
        self.solver = solver

    def move_chess_piece(self, chess_piece):

        # get random point 
        # check if point available
        # if yes: move chess to that point
        # else: random again

        pass

    def count_available_attack_target(self, chess_piece):

        attack_pattern = chess_piece.get_attack_pattern()
        score = 0

        for direction in attack_pattern:

            tiles_to_check = attack_pattern[direction]
            for tile in tiles_to_check:

                if self.chess_board.get_tile_status(tile) is not None:
                    # score + 1 or something
                    break

        return score

    def solve(self):

        # apply algorithm to decide movement
        
        pass
        