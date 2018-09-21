
class StateEvaluator:

    def __init__(self):
        pass

    def evaluate(self, chess_board):

        score = 0
        for piece in chess_board.pieces:
            score -= self.evaluate_piece_attack_target(chess_board, piece)

        return score

    def evaluate_piece_attack_target(self, chess_board, chess_piece):
        
        attack_pattern = chess_piece.get_attack_pattern()

        score = 0
        for direction in attack_pattern:
            tiles_to_check = attack_pattern[direction]
            for tile in tiles_to_check:
                piece_on_checked_tile = chess_board.get_tile_status(tile)
                if piece_on_checked_tile is not None:
                    score += self.get_score(piece_on_checked_tile, chess_piece)
                    break

    def get_score(self, targeted_piece, chess_piece):

        if targeted_piece.color == chess_piece.color:
            return 1
        else:
            return -1
                    