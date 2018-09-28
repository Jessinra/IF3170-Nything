from chess_player import ChessPlayer
from solver.factory import SolverModelFactory
from chess_board import ChessBoard
from file_parser import FileParser
from solver.threshold_generator import ConstantGenerator
from copy import deepcopy

parent = 4
mutation_prob = 0.25
solver = SolverModelFactory.create_model("genetic_algorithm", parent, mutation_prob)
solver.generate()
solver.next_step()
for i in range(0, solver.population_count):
    print(solver.population[i].position)
    print(solver.new_parent_position[i])



