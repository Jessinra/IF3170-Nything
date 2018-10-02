class StateEvaluator:
    def evaluate(self, chess_board):
        score_same_color = 0
        score_diff_color = 0

        for piece in chess_board.pieces:
            same_score, diff_score = self.evaluate_piece_attack_target(chess_board, piece)
            score_same_color += same_score
            score_diff_color += diff_score

        single_score = score_diff_color - score_same_color
        return score_same_color, score_diff_color, single_score

    def evaluate_chess_count(self, chess_board):
        same_piece = 0
        diff_piece = 0
        for piece in chess_board.pieces:
            same_score, diff_score = self.evaluate_piece_attack_target(chess_board, piece)
            if same_score > 0:
                same_piece += 1
            if diff_score > 0:
                diff_piece += 1

        return same_piece, diff_piece

    def evaluate_piece_attack_target(self, chess_board, chess_piece):
        attack_pattern = chess_piece.get_attack_pattern()

        score_same_color = 0
        score_diff_color = 0

        for direction in attack_pattern:
            tiles_to_check = attack_pattern[direction]
            for tile in tiles_to_check:
                piece_on_checked_tile = chess_board.get_piece_on_tile(tile)
                if piece_on_checked_tile is not None:
                    same_score, diff_score = self.get_score(piece_on_checked_tile, chess_piece)
                    score_same_color += same_score
                    score_diff_color += diff_score

                    break

        return score_same_color, score_diff_color

    def get_score(self, targeted_piece, chess_piece):
        if targeted_piece.color == chess_piece.color:
            return 1, 0  # minimize same color
        else:
            return 0, 1  # maximize different color
