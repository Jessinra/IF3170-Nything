from solver.base_solver import BaseSolver
from file_parser import FileParser
from chess_board import ChessBoard
from solver.parent import Parent
import random
import itertools
import copy

class GeneticAlgorithm(BaseSolver):
    def __init__(self, population_count, mutation_prob, fraction):
        super().__init__()
        self.population_count = population_count
        self.mutation_prob = mutation_prob
        self.fraction = fraction
        self.population = []
        self.select_parent = []

    def generate(self):
        for i in range(self.population_count):
            board = ChessBoard()
            board = FileParser.load(board, "something.txt")
            parent = Parent(board)
            self.population.append(parent)
            if i == self.population_count-1:
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
            parent.fitness_score = parent.score/sum_of_score

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

        # for parent in self.child_factory:
        #     print(parent.fitness_score)
        #
        print(self.select_parent)

    def selection_and_crossover(self):
        for i in range(0, self.population_count, 2):
            len_position = len(self.population[0].position)
            split_point = random.randint(1, len_position-1)

            list_position_1 = copy.deepcopy((self.find_parent(self.select_parent[i])).position)
            list_position_2 = list_position_1[:split_point]
            print(split_point)
            print(list_position_1)
            list_position_1 = list_position_1[split_point:len_position]
            print(list_position_1)
            print(list_position_2)

            list_position_3 = copy.deepcopy((self.find_parent(self.select_parent[i+1])).position)
            list_position_4 = list_position_3[:split_point]
            print(split_point)
            print(list_position_3)
            list_position_3 = list_position_3[split_point:len_position]
            print(list_position_3)
            print(list_position_4)

            list_position_2.append(list_position_3)
            list_position_4.append(list_position_1)

            print('\n')
            print(list_position_2)
            print(list_position_4)
            print('\n')
            print('Iterasi ke' + str(i))
            print('\n')

    def parent_list_of_chess_piece_position_generator(self):
        for parent in self.population:
            for chess_piece in parent.chess_board.pieces:
                parent.position.append(chess_piece.position)
            #print(parent.position)

    def find_parent(self, id):
        for parent in self.population:
            if id == parent.id:
                return parent

    def next_step(self):
        pass
