class BaseSolver:
    def __init__(self, chess_board):
        self.board = chess_board

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

    def next_step(self):
        pass
