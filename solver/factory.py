from solver.genetic_algorithm import GeneticAlgorithm
from solver.simulated_annealing import SimulatedAnnealing


class SolverModelFactory:
    @staticmethod
    def create_model(cls, algorithm_type, *args, **kwargs):
        if algorithm_type == "genetic_algorithm":
            return GeneticAlgorithm(*args, **kwargs)

        elif algorithm_type == "simulated_annealing":
            return SimulatedAnnealing(*args, **kwargs)

        elif algorithm_type == "hill_climbing":
            return SimulatedAnnealing(proba=0, *args, **kwargs)