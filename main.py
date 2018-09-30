from chess_player import ChessPlayer
from solver.factory import SolverModelFactory
from chess_board import ChessBoard
from file_parser import FileParser
from solver.threshold_generator import ConstantGenerator
from copy import deepcopy

population_count = 4
mutation_prob = 0.25
population_survival = 0.5
max_population = 5000
solver = SolverModelFactory.create_model("genetic_algorithm", 
    population_count, 
    max_population,
    mutation_prob, 
    population_survival)

order = FileParser.parse_data("example_board/3queen.txt")
solver.generate_population(order)
for i in range(0, 5):
    print('try :' + str(i+1))
    solver.next_step()

