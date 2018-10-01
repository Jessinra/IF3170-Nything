class StateEvaluator:
    def evaluate(self, chess_board):
        score = 0
        for piece in chess_board.pieces:
            score += self.evaluate_piece_attack_target(chess_board, piece)

        return score

    def evaluate_piece_attack_target(self, chess_board, chess_piece):
        attack_pattern = chess_piece.get_attack_pattern()

        tuple_score = (0, 0)  # (same, diff)

        for direction in attack_pattern:
            tiles_to_check = attack_pattern[direction]
            for tile in tiles_to_check:
                piece_on_checked_tile = chess_board.get_piece_on_tile(tile)
                if piece_on_checked_tile is not None:
                    tuple_score += self.get_score(piece_on_checked_tile, chess_piece)
                    break

        single_score = tuple_score[0] + tuple_score[1]
        return tuple_score, single_score

    def get_score(self, targeted_piece, chess_piece):
        if targeted_piece.color == chess_piece.color:
            return -1, 0  # minimize same color
        else:
            return 0, 1  # maximize different color
