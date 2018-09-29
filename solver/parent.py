from solver.base_solver import BaseSolver


class Parent(BaseSolver):
    parent_id = 1

    def __init__(self, chess_board):
        super().__init__()
        self.chess_board = chess_board
        self.position = []
        self.score = 0
        self.fitness_score = 0
        self.id = Parent.parent_id
        Parent.parent_id += 1

    @staticmethod
    def reset_id():
        Parent.parent_id = 1

    def __lt__(self, other):
        self_score = self.evaluator.evaluate(self.chess_board)
        other_score = other.evaluator.evaluate(other.chess_board)
        return self_score >= other_score
