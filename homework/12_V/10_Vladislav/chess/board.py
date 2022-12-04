import sys
from termcolor import colored

class Chessboard:
    def __init__(self):
        self.board = []

        for i in range(8):
            self.board.append([None] * 8)

        for i in range(8):
            self.board[1][i] = colored("P", "white", "on_grey")

        for i in range(8):
            self.board[6][i] = colored("P", "grey", "on_white")

        self.board[0][0] = colored("R", "white", "on_grey")
        self.board[0][1] = colored("N", "white", "on_grey")
        self.board[0][2] = colored("B", "white", "on_grey")
        self.board[0][3] = colored("Q", "white", "on_grey")
        self.board[0][4] = colored("K", "white", "on_grey")
        self.board[0][5] = colored("B", "white", "on_grey")
        self.board[0][6] = colored("N", "white", "on_grey")
        self.board[0][7] = colored("R", "white", "on_grey")


        self.board[7][0] = colored("R", "grey", "on_white")
        self.board[7][1] = colored("N", "grey", "on_white")
        self.board[7][2] = colored("B", "grey", "on_white")
        self.board[7][3] = colored("Q", "grey", "on_white")
        self.board[7][4] = colored("K", "grey", "on_white")
        self.board[7][5] = colored("B", "grey", "on_white")
        self.board[7][6] = colored("N", "grey", "on_white")
        self.board[7][7] = colored("R", "grey", "on_white")        

    def print_board(self):
        buffer = str()
        for i in range(33):
            buffer += "-"
        print(buffer)       

        for row in range(len(self.board)):
            res = "|"
            for col in self.board[row]:
                if col is None:
                    res += "   |"
                else:
                    res += (" " + str(col) + " |")

            print(res)
            print(buffer)