from solver.genetic_algorithm import GeneticAlgorithm
from solver.simulated_annealing import SimulatedAnnealing
from solver.full_scan_hill_climbing import FullScanHillClimbing
from solver.stochastic_hill_climbing import StochasticHillClimbing


class SolverModelFactory:
    @staticmethod
    def create_model(algorithm_type, *args, **kwargs):

        if algorithm_type == "genetic_algorithm":
            return GeneticAlgorithm(*args, **kwargs)

        elif algorithm_type == "simulated_annealing":
            return SimulatedAnnealing(*args, **kwargs)

        elif algorithm_type == "full_scan_hill_climbing":
            return FullScanHillClimbing(*args, **kwargs)

        elif algorithm_type == "stochastic_hill_climbing":
            return StochasticHillClimbing(*args, **kwargs)
