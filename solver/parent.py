class Parent:
    parent_id = 1
    def __init__(self, chess_board):
        self.chess_board = chess_board
        self.position = []
        self.score = 0
        self.fitness_score = 0
        self.id = Parent.parent_id
        Parent.parent_id += 1

    def reset_id(self):
        Parent.parent_id = 1