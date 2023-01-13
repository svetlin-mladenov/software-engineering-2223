import string
from termcolor import *


class Piece:
    def __init__(self, color, symbol):
        self.color = color
        self.symbol = symbol

    def __str__(self):
        return self.symbol


class Board:
    def __init__(self) :
        self.board = [[None for j in range(8)] for i in range(8)]
        for i in range(8):
            self.board[1][i] = Piece("black", "♟ ︎")
            self.board[6][i] = Piece("white", "♙ ")

        self.board[0][0] = Piece("black", "♜ ")
        self.board[0][1] = Piece("black", "♞ ")
        self.board[0][2] = Piece("black", "♝ ")
        self.board[0][3] = Piece("black", "♛ ")
        self.board[0][4] = Piece("black", "♚ ")
        self.board[0][5] = Piece("black", "♝ ")
        self.board[0][6] = Piece("black", "♞ ")
        self.board[0][7] = Piece("black", "♜ ")
        self.board[7][0] = Piece("white", "♖ ")
        self.board[7][1] = Piece("white", "♘ ")
        self.board[7][2] = Piece("white", "♗ ")
        self.board[7][3] = Piece("white", "♕ ")
        self.board[7][4] = Piece("white", "♔ ")
        self.board[7][5] = Piece("white", "♗ ")
        self.board[7][6] = Piece("white", "♘ ")
        self.board[7][7] = Piece("white", "♖ ")


        def print_board(self):
                for i in range(0, 8):
                    for j in range(0, 8):
                        if self.board[i][j] == None:
                            cprint("  ", "red", "on_white", end = "")
                        else:
                            cprint(self.board[i][j], "white", "on_red", end = "")
                        if j == 7:
                            print("\n", end = "")


board = Board()
board.print_board()
