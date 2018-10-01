from solver.base_solver import BaseSolver
import random
import copy


class Individuals(BaseSolver):
    individual_count = 0

    def __init__(self, chess_board):
        super().__init__()
        self.chess_board = chess_board
        self.pieces_position = []
        self.score = 0
        self.fitness_score = 0
        self.set_id()

    def set_score(self):
        _, _, self.score = self.evaluator.evaluate(self.chess_board)

    def generate_pieces_position(self):
        self.pieces_position = []
        for chess_piece in self.chess_board.pieces:
            self.pieces_position.append(chess_piece.position)

    def mutate_pieces_position(self):

        empty_tiles = self.chess_board.get_empty_tiles()
        random_index = random.randint(0, len(self.pieces_position) - 1)

        self.pieces_position[random_index] = random.choice(empty_tiles)

    def place_chess_piece_according_to_pieces_positions(self):

        self.chess_board.initialize_empty_board()
        for i in range(0, len(self.pieces_position)):
            chess_piece = self.chess_board.pieces[i]
            chess_piece.move(self.pieces_position[i])
            self.add_piece_to_board(chess_piece)

    def set_id(self):
        Individuals.individual_count += 1
        self.id = Individuals.individual_count

    def deepcopy_pieces_position(self):
        return copy.deepcopy(self.pieces_position)

    @staticmethod
    def reset_individual_count():
        Individuals.individual_count = 0

    def __lt__(self, other):
        return self.score < other.score

    def add_piece_to_board(self, chess_piece):
        self.chess_board.add_piece_to_board(chess_piece)
