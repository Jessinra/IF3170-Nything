from Genetic_algorithm import GeneticAlgorithm
from Simulated_annealing import SimulatedAnnealing
from Hill_claimbing import HillClaimbing

class SolverModelFactory:

    @staticmethod
    def create_model(algorithm_type, *args, **kwargs):

        if algorithm_type == "genetic_algorithm":
            return GeneticAlgorithm(*args, **kwargs)

        elif algorithm_type == "simulated_annealing":
            return SimulatedAnnealing(*args, **kwargs)

        elif algorithm_type == "hill_claimbing":
            return SimulatedAnnealing(proba=0, *args, **kwargs)
