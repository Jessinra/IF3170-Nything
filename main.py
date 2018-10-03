from tqdm import tqdm
import os
from time import sleep

from solver.factory import SolverModelFactory
from file_parser import FileParser
from chess_board import ChessBoard
from solver.threshold_generator import BoltzmannGenerator, ConstantGenerator

board_data = ""
iter_count = ""
solver = None
generator = None

def logo():
    print('''77777777777777777777777777777777777777777777777777777777777777777777777777777777777''')
    print('''`7MN.   `7MF'`YMM'   `MM'MMP""MM""YMM `7MMF'  `7MMF'`7MMF'`7MN.   `7MF' .g8"""bgd  ''')
    print('''  MMN.    M    VMA   ,V  P'   MM   `7   MM      MM    MM    MMN.    M .dP'     `M  ''')
    print('''  M YMb   M     VMA ,V        MM        MM      MM    MM    M YMb   M dM'       `  ''')
    print('''  M  `MN. M      VMMP         MM        MMmmmmmmMM    MM    M  `MN. M MM           ''')
    print('''  M   `MM.M       MM          MM        MM      MM    MM    M   `MM.M MM.    `7MMF' ''')
    print('''  M     YMM       MM          MM        MM      MM    MM    M     YMM `Mb.     MM  ''')
    print('''.JML.    YM     .JMML.      .JMML.    .JMML.  .JMML..JMML..JML.    YM   `"bmmmdPY''')
    print('''77777777777777777777777777777777777777777777777777777777777777777777777777777777777''')
    print()


def author():
    print("13516041 Felix Septianus")
    print("13516112 Jessin Donnyson")
    print("13516014 Renjira")
    print("13516101 Kelvin Kristian")
    print("13516119 Gabriel Bentara Raphael")
    print("===================================================================================")


def menu():
    print("Choose the algorithm :")
    print("1. Full Scan Hill Climbing")
    print("2. Stochastic Hill Climbing")
    print("3. Simulated Annealing")
    print("4. Genetic Algorithm")


def prepare_algo():
    cmd = prompt()
    if cmd == "1":
        prepare_full_hill()
        execute()
    elif cmd == "2":
        prepare_stoc_hill()
        execute()
    elif cmd == "3":
        prepare_sim_ann()
        execute()
    elif cmd == "4":
        prepare_ga()
        execute()
    else:
        print("Invalid choice, choose again")
        menu()
        prepare_algo()


def basic_prepare():
    global board_data, iter_count
    print("Board filename : ")
    filename = prompt()
    print("Iteration count : ")
    iter_count = prompt()
    board_data = FileParser.parse_data(filename)


def prepare_full_hill():
    global solver, board_data
    basic_prepare()
    board = ChessBoard.load_board(board_data)
    solver = SolverModelFactory.create_model("full_scan_hill_climbing", board)


def prepare_stoc_hill():
    global solver, board_data
    basic_prepare()
    board = ChessBoard.load_board(board_data)
    solver = SolverModelFactory.create_model("stochastic_hill_climbing", board)


def prepare_sim_ann():
    global solver, board_data
    basic_prepare()
    prepare_generator()
    board = ChessBoard.load_board(board_data)
    solver = SolverModelFactory.create_model("simulated_annealing", board, generator)


def prepare_generator():
    global generator
    print("Choose the temperature generator")
    print("1. Constant Generator")
    print("2. Boltzmann Generator")
    choice = prompt()
    print("Initial temperature (suggested 15) :")
    temp = prompt()
    if choice == "1":
        generator = ConstantGenerator(float(temp))
    else:
        print("Input Ratio (suggested 1.0006) :")
        step = prompt()
        generator = BoltzmannGenerator(float(temp), float(step))


def prepare_ga():
    global solver, board_data
    basic_prepare()
    print("Population count : ")
    population = prompt()
    print("Mutation probability : ")
    mutation_prob = prompt()
    solver = SolverModelFactory.create_model("genetic_algorithm", int(population), float(mutation_prob))
    solver.generate_population(board_data)


def execute():
    for i in tqdm(range(int(iter_count))):
        solver.next_step()

    if "population" in vars(solver):
        board = max(solver.population).chess_board
    else:
        board = solver.chess_board
    print()
    print(board)
    print("Jumlah serangan (sama warna, beda warna, total)")
    print(solver.evaluator.evaluate(board))
    print("Jumlah bidak menyerang (sama warna, beda warna)")
    print(solver.evaluator.evaluate_chess_count(board))

def prompt():
    cmd = input(">>> ")
    return cmd


if __name__ == "__main__":
    logo()
    author()
    menu()
    prepare_algo()

