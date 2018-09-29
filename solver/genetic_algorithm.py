from solver.base_solver import BaseSolver
from file_parser import FileParser
from chess_board import ChessBoard
from solver.parent import Parent
import random
import itertools
import copy
import math


class GeneticAlgorithm(BaseSolver):
    def __init__(self, population_count, mutation_prob):
        super().__init__()
        self.population_count = population_count
        self.mutation_prob = mutation_prob
        self.population = []
        self.new_parent_position = []
        self.select_parent = []

    def generate(self):
        for i in range(self.population_count):
            orders = FileParser.parse_data("unit_test/testfile.txt")
            board = ChessBoard.load_board(orders)
            parent = Parent(board)
            self.population.append(parent)
            if i == self.population_count - 1:
                parent.reset_id()

    @staticmethod
    def get_tiles(board):
        arr_tiles = []
        for i in range(board.min_row, board.max_row):
            for j in range(board.min_col, board.max_col):
                tiles = board.get_tile_status((i, j))
                if tiles:
                    arr_tiles.append(j)
        return arr_tiles

    def find_score(self):
        for parent in self.population:
            parent.score = self.evaluator.evaluate(parent.chess_board)

    def fitness(self):
        sum_of_score = 0
        self.fitness_positivy()

        for parent in self.population:
            sum_of_score += parent.score

        for parent in self.population:
            parent.fitness_score = parent.score / sum_of_score

        self.fitness_percetager()

    def fitness_positivy(self):
        parent_score = []
        for parent in self.population:
            parent_score.append(parent.score)

        minimum_score = min(parent_score)

        if minimum_score < 0:
            for parent in self.population:
                parent.score = parent.score + abs(minimum_score) + 1

    def fitness_percetager(self):
        for parent in self.population:
            parent.fitness_score = int(parent.fitness_score * 100)

    def weighted_random(self):
        weighted_value = []
        for parent in self.population:
            weighted_value.append([parent.id] * parent.fitness_score)

        weighted_value = list(itertools.chain(*weighted_value))

        for _ in range(self.population_count):
            choice = random.choice(weighted_value)
            self.select_parent.append(choice)

    def selection_and_crossover_and_mutation(self, index):
        len_position = len(self.population[0].position)
        split_point = random.randint(1, len_position-1)

        list_position_1 = copy.deepcopy((self.find_parent(self.select_parent[index])).position)
        list_position_2 = list_position_1[split_point:len_position]
        list_position_1 = list_position_1[:split_point]

        list_position_3 = copy.deepcopy((self.find_parent(self.select_parent[index+1])).position)
        list_position_4 = list_position_3[split_point:len_position]
        list_position_3 = list_position_3[:split_point]

        list_position_2 += list_position_3
        list_position_4 += list_position_1

        merged_parent = list(set(list_position_1 + list_position_3))
        unpicked_position_list_2 = [item for item in merged_parent if item not in list_position_2]
        unpicked_position_list_4 = [item for item in merged_parent if item not in list_position_4]
        list_position_2 = self.fix_child_list_maker(list_position_2, unpicked_position_list_2)
        list_position_4 = self.fix_child_list_maker(list_position_4, unpicked_position_list_4)

        self.new_parent_position.append(list_position_2)
        self.new_parent_position.append(list_position_4)

    def selection_and_crossover_and_mutation_iteration(self):
        selection_crossover_mutation_iteration = int(self.population_count)
        for index in range(0, selection_crossover_mutation_iteration, 2):
            self.selection_and_crossover_and_mutation(index)

    def parent_list_of_chess_piece_position_generator(self):
        for parent in self.population:
            for chess_piece in parent.chess_board.pieces:
                parent.position.append(chess_piece.position)

    def find_parent(self, p_id):
        for parent in self.population:
            if p_id == parent.id:
                return parent

    @staticmethod
    def fix_child_list_maker(list_position, unpicked_number):
        fix_child_list = []
        j = 0
        for position in list_position:
            if position not in fix_child_list:
                fix_child_list.append(position)
            else:
                fix_child_list.append(unpicked_number[j])
                j += 1

        return fix_child_list

    def mutation(self, list_position):
        mutation_probability = [0] * 25 + [1] * 75
        choice = random.choice(mutation_probability)
        if choice == 1:
            point = list_position[0]
            while point in list_position:
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                point = (x, y)
            index = random.randint(0, len(self.population[0].position))
            list_position[index] = point

    def natural_selection(self, accepted_parent_percentage):
        self.population = sorted(self.population)
        for parent in self.population:
            print(parent.position)
            print(parent.evaluator.evaluate(parent.chess_board))
        self.population_count = math.ceil(self.population_count * accepted_parent_percentage / 100)
        self.population = self.population[0:self.population_count]

        print("GA Result")
        for parent in self.population:
            print(parent.position)

    def copy_parent(self):
        new_parent = []
        for parent in self.population:
            deep_copied = copy.deepcopy(parent)
            new_parent.append(deep_copied)

        i = 0
        for parent in new_parent:
            parent.position = self.new_parent_position[i]
            i += 1

        self.population = self.population + new_parent
        self.population_count = self.population_count * 2

    def assigning_parent_position_to_chessboard(self):
        i = 0
        for parent in self.population:
            j = 0
            for chess_piece in parent.chess_board.pieces:
                from_position = chess_piece.position
                #print(from_position)
                chess_piece.move(self.new_parent_position[i][j])
                #print(self.new_parent_position[i][])
                parent.chess_board.update_chess_piece(chess_piece, from_position)
                j += 1
            i += 1

    def next_step(self):
        self.find_score()
        self.fitness()
        self.weighted_random()
        self.parent_list_of_chess_piece_position_generator()
        for parent in self.population:
            print(parent.position)
            print(parent.chess_board)
        self.selection_and_crossover_and_mutation_iteration()
        self.copy_parent()
        self.natural_selection(50)
        self.assigning_parent_position_to_chessboard()
        for parent in self.population:
            print(parent.position)
            print(parent.chess_board)
