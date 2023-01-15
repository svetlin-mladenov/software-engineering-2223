import string
from termcolor import *

class Piece:
    def __init__(self, color, symbol):
        self.color = color
        self.symbol = symbol

    def __str__(self):
        return self.symbol

class Board:
    def __init__(self, fen):
        self.board = [[None for j in range(8)] for i in range(8)]
        ranks = fen.split(" ")[0].split("/")
        for i in range(8):
            for j, c in enumerate(ranks[i]):
                if c.isnumeric():
                    for k in range(int(c)):
                        self.board[i][j+k] = None
                else:
                    if c.isupper():
                        color = "white"
                    else:
                        color = "black"
                    symbol = "♟ " if c.lower() == "p" else "♞ " if c.lower() == "n" else "♝ " if c.lower() == "b" else "♛ " if c.lower() == "q" else "♚ " if c.lower() == "k" else "♜ "
                    self.board[i][j] = Piece(color, symbol)

    def print_board(self):
        print("  A B C D E F G H")
        for i in range(8):
            print(8-i, end=" ")
            for j in range(8):
                color = ["red", "on_white"] if (i+j)%2 == 0 else ["white", "on_red"]
                if self.board[i][j] is None:
                    cprint("  ", color[0], color[1], end = "")
                else:
                    cprint(self.board[i][j], color[0], color[1], end = "")
            print(" " + str(8-i))

fen = "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25"
board = Board(fen)
board.print_board()
