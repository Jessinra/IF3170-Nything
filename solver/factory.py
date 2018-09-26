from solver.genetic_algorithm import GeneticAlgorithm
from solver.simulated_annealing import SimulatedAnnealing
from solver.hill_climbing import HillClimbing


class SolverModelFactory:

    @staticmethod
    def create_model(algorithm_type, *args, **kwargs):
        
        if algorithm_type == "genetic_algorithm":
            return GeneticAlgorithm(*args, **kwargs)

        elif algorithm_type == "simulated_annealing":
            return SimulatedAnnealing(*args, **kwargs)

        elif algorithm_type == "hill_climbing":
            return HillClimbing(*args, **kwargs)
