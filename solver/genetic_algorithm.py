from solver.base_solver import BaseSolver
from file_parser import FileParser
from chess_board import ChessBoard
from solver.parent import Individuals
import random
import itertools
import copy
import math
import numpy


class GeneticAlgorithm(BaseSolver):
    def __init__(self, population_count, max_population, mutation_probability, population_survival_rate):
        super().__init__()
        self.population_count = population_count
        self.max_population = max_population
        self.mutation_probability = mutation_probability
        self.population_survival_rate = population_survival_rate    # keep best n-% every iteration
        self.population = []
        self.new_children = []
        self.crossovered_pieces_position = []
        self.selected_parents_id = []

    def generate_population(self, orders):

        for _ in range(self.population_count):
            individual = self.create_individual(orders)
            self.population.append(individual)

    def create_individual(self, orders):
        chess_board = ChessBoard.load_board(orders)
        return Individuals(chess_board)

    def set_score_for_each_individual(self):
        for individual in self.population:
            individual.set_score()

    def set_fitness_score_for_each_individual(self):
        self.shifting_all_individual_score_to_positive()
        
        sum_of_score = 0
        for individual in self.population:
            sum_of_score += individual.score

        for individual in self.population:

            try:
                individual.fitness_score = individual.score / sum_of_score
            except:
                individual.fitness_score = 0

    def shifting_all_individual_score_to_positive(self):
        individual_scores = []
        for individual in self.population:
            individual_scores.append(individual.score)

        minimum_score = min(individual_scores)

        if minimum_score < 0:
            for individual in self.population:
                individual.score += abs(minimum_score) + 1

    def fitness_to_percent_for_each_individual(self):
        for individual in self.population:
            individual.convert_fitness_score_to_percent()

    def select_parents_with_weighted_random(self):   
        population_id = [i for i in range(1, self.population_count + 1)]
        individual_weight = [individual.fitness_score for individual in self.population]
        parent_size = int(self.population_count // 2 * 2 )

        try:
            self.select_parent_id_weighted_random(population_id, parent_size, individual_weight)
        except:
            self.select_parent_id_default_random(population_id, parent_size)

    def select_parent_id_weighted_random(self, population_id, parent_size, individual_weight):
        self.selected_parents_id = numpy.random.choice(
            a=population_id,
            size=parent_size,
            p=individual_weight
        )

    def select_parent_id_default_random(self, population_id, parent_size):
        self.selected_parents_id = random.choices(population_id, k=parent_size)

    # please refactor this
    def selection_and_crossover_and_mutation(self, index):
        split_point = self.get_split_point()

        parent_01 = self.find_individual_by_id(self.selected_parents_id[index])
        parent_02 = self.find_individual_by_id(self.selected_parents_id[index+1])
        child_01, child_02 = self.crossover_parents(parent_01, parent_02, split_point)

        available_positions = list(set(parent_01.pieces_position + parent_02.pieces_position))
        child_01_unused_positions = self.get_unused_positions(available_positions, child_01)
        child_02_unused_positions = self.get_unused_positions(available_positions, child_02)

        child_01 = self.change_duplicate_positions(child_01, child_01_unused_positions)
        child_02 = self.change_duplicate_positions(child_02, child_02_unused_positions)

        self.crossovered_pieces_position.append(child_01)
        self.crossovered_pieces_position.append(child_02)

    @staticmethod
    def get_unused_positions(available_positions, child):
        return [p for p in available_positions if p not in child]


    def crossover_parents(self, parent_01, parent_02, split_point):
        
        parent_01_pieces_position = parent_01.deepcopy_pieces_position()
        parent_02_pieces_position = parent_02.deepcopy_pieces_position()
        
        parent_01_gen_front = parent_01_pieces_position[:split_point]
        parent_01_gen_back = parent_01_pieces_position[split_point:]
        parent_02_gen_front = parent_02_pieces_position[:split_point]
        parent_02_gen_back = parent_02_pieces_position[split_point:]

        child_01 = parent_01_gen_front + parent_02_gen_back
        child_02 = parent_02_gen_front + parent_01_gen_back

        return child_01, child_02

    

    def get_split_point(self):

        # Get sample of individual to get piece_position length
        len_position = len(self.population[0].pieces_position)  
        split_point = random.randint(1, len_position - 2)
        return split_point

    def selection_and_crossover_and_mutation_iteration(self):

        # (skip iteration by 2) e.g. individual 0 will be matched with individual 1, 2nd with 3rd, and so on...
        # Also atempt to skip remaining individual if it's odd number
        for index in range(0, len(self.selected_parents_id), 2):
            self.selection_and_crossover_and_mutation(index)

    def generate_pieces_position_for_each_individual(self):
        for individual in self.population:
            individual.generate_pieces_position()

    def find_individual_by_id(self, individual_id):
        for individual in self.population:
            if individual_id == individual.id:
                return individual

    @staticmethod
    def change_duplicate_positions(position_list, unpicked_numbers):
        filtered_position = []
        i = 0
        for position in position_list:
            if position not in filtered_position:
                filtered_position.append(position)
            else:
                if i < len(unpicked_numbers):
                    filtered_position.append(unpicked_numbers[i])
                    i += 1

        return filtered_position

    def try_to_mutate_individual(self, individuals):
        if self.is_mutation_occurring():
            individuals.mutate_pieces_position()

    def is_mutation_occurring(self):
        random_number = random.random() # random float 0 to 1
        return random_number < self.mutation_probability

    def natural_selection(self):
        self.population = sorted(self.population, reverse=True)

        self.remove_exceeding_individuals()            
        self.get_survival_individual_count()
        self.remove_individual_without_partner()

        self.population = self.population[:self.population_count]



    def remove_exceeding_individuals(self):
        if self.population_count > self.max_population:
            self.population_count = self.max_population

    def get_survival_individual_count(self):
        self.population_count = math.ceil(self.population_count * self.population_survival_rate)

    def remove_individual_without_partner(self):
        if self.population_count % 2 == 1:
            self.population_count -= 1

    # Please rename this
    def create_crossovered_individuals(self):

        self.new_children = self.create_children()
        self.configure_pieces_for_each_child()
        self.add_children_to_population()

    def add_children_to_population(self):
        self.population = self.population + self.new_children
        self.population_count = self.population_count + len(self.new_children)
        self.new_children = []

    def create_children(self):

        amount = int(self.population_count // 2 * 2)
        return copy.deepcopy(self.population[:amount])

    def configure_pieces_for_each_child(self):
        for i in range(0, len(self.new_children)):
            child = self.new_children[i]
            child.pieces_position = self.crossovered_pieces_position[i]
            child.place_chess_piece_according_to_pieces_positions()
            self.try_to_mutate_individual(child)

    def reassign_individuals_id(self):
        Individuals.reset_individual_count()
        for individual in self.population:
            individual.set_id()

    def teardown(self):
        self.new_children = []
        self.crossovered_pieces_position = []
        self.selected_parents_id = []

    def next_step(self):

        self.set_score_for_each_individual()
        self.set_fitness_score_for_each_individual()
        self.generate_pieces_position_for_each_individual()


        self.select_parents_with_weighted_random()
        self.selection_and_crossover_and_mutation_iteration()
        self.create_crossovered_individuals()
        self.natural_selection()
        self.reassign_individuals_id()
        self.teardown()

        # print()
        # print(self.population_count)
        # print("best", max([x.score for x in self.population]))
        # print("top 4")
        # for x in self.population:
        #     print(x.pieces_position)