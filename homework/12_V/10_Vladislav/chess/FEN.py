from board import Chessboard
from termcolor import colored

def parse_fen_to_matrix(fen_string):
    rows = fen_string.split(" ")[0].split("/")
    matrix = []
    for row in rows:
        matrix_row = []
        for char in row:
            if char.isalpha():
                if char.islower():
                    matrix_row.append(colored(char.upper(), "white", "on_grey"))
                else:
                    matrix_row.append(colored(char.upper(), "grey", "on_white"))
            else:
                matrix_row.extend([" " for i in range(int(char))])
        matrix.append(matrix_row)
    return matrix



fen_string = "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25"
matrix = parse_fen_to_matrix(fen_string)
Chessboard(matrix).print_board()