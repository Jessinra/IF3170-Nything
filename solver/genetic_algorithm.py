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

    def find_position(self):
        for parent in self.population:
            tiles = self.get_tiles(parent.chess_board)
            parent.position = tiles

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

        for i in range(self.population_count):
            choice = random.choice(weighted_value)
            self.select_parent.append(choice)

        # for parent in self.child_factory:
        #     print(parent.fitness_score)
        #
        # print(self.select_parent)

    def selection(self):
        # for i in range(0, int(self.parent/2)):
        len_position = len(self.population[0].position)
        split_point = random.randint(1, len_position-1)

        l1 = copy.deepcopy((self.find_parent(self.select_parent[0])).position)
        l2 = l1[:split_point]
        print(split_point)
        print(l1)
        l1 = l1[split_point:len_position]
        print(l1)
        print(l2)
        l3 = copy.deepcopy((self.find_parent(self.select_parent[1])).position)
        l4 = l3[:split_point]
        print(split_point)
        print(l3)
        l3 = l3[split_point:len_position]
        print(l3)
        print(l4)

        l2 = l2 + l3
        l4 = l4 + l1

        print('\n')
        print(l2)
        print(l4)



    def find_parent(self, id):
        for parent in self.population:
            if id == parent.id:
                return parent

    def next_step(self):
        pass
