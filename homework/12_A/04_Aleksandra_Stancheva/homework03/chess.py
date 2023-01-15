import sys
from termcolor import colored, cprint


class ChessBoard:
    fen_map = {
        "p": "♟",
        "r": "♜",
        "n": "♞",
        "b": "♝",
        "q": "♛",
        "k": "♚",
        "P": "♙",
        "R": "♖",
        "N": "♘",
        "B": "♗",
        "Q": "♕",
        "K": "♔"
    }

    def __init__(self, fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self.chess_board = [[] for _ in range(8)]

        for row_number, row in enumerate(fen.split()[0].split("/")):
            column = 0
            for symbol in row:
                if symbol.isdigit():
                    for _ in range(int(symbol)):
                        self.chess_board[row_number].append([(row_number + column) % 2, "   "])
                        column += 1
                else:
                    self.chess_board[row_number].append([(row_number + column) % 2, f" {self.fen_map[symbol]} "])
                    column += 1

    def print_chess_board(self):   
        for i in range (0, 8):
            for y in range (0, 8):
                if self.chess_board[i][y][0] == 0:
                    cprint(self.chess_board[i][y][1], "grey", "on_white", end = "")
                else:
                    cprint(self.chess_board[i][y][1], "grey", "on_grey", end = "")
                if y == 7:
                    print("\n", end = "")
                

if __name__ == "__main__":
    my_board = ChessBoard("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25")
    my_board.print_chess_board()