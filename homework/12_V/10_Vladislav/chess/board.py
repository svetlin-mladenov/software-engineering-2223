import sys
from termcolor import colored

class Chessboard:
    def __init__(self, board):
        self.board = board    

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