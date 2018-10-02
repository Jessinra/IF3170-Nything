from solver.factory import SolverModelFactory
from file_parser import FileParser
from solver.state_evaluator import StateEvaluator

population_count = 10
mutation_prob = 0.15
solver = SolverModelFactory.create_model("genetic_algorithm",
    population_count, 
    mutation_prob)

order = FileParser.parse_data("example_board/14bishop.txt")
solver.generate_population(order)
for i in range(0, 1000):
    print('try :' + str(i+1))
    solver.next_step()
    best = max(solver.population)
    print(StateEvaluator().evaluate(best.chess_board))

best = max(solver.population)
print(best.chess_board)
print(StateEvaluator().evaluate(best.chess_board))
