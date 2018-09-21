from chess_player import ChessPlayer
from solver.factory import SolverModelFactory
from chess_board import ChessBoard
from file_parser import FileParser
from solver.threshold_generator import ConstantGenerator
from copy import deepcopy

for i in range(100):
    board = ChessBoard()
    board = FileParser.load(board, "something.txt")
    threshold = ConstantGenerator(0.1)
    solver = SolverModelFactory.create_model("simulated_annealing", board, threshold)
    player = ChessPlayer(board, solver)
    before_board = deepcopy(board)
    before_score = player.solver.evaluator.evaluate(board)
    player.solve(200)
    score = player.solver.evaluator.evaluate(board)
    print(score)
    print(board)