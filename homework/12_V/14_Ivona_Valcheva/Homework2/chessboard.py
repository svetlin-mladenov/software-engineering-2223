import piece
import sys
from termcolor import colored

class Chessboard:
    def __init__(self):
        self.board = []

        for i in range(8):
            self.board.append([None] * 8)

        for i in range(8):
            self.board[1][i] = colored(piece.Pawn(0).name, "red")

        for i in range(8):
            self.board[6][i] = colored(piece.Pawn(1).name, "blue")

        self.board[0][0] = colored(piece.Rook(0).name, "red")
        self.board[0][1] = colored(piece.Knight(0).name, "red")
        self.board[0][2] = colored(piece.Bishop(0).name, "red")
        self.board[0][3] = colored(piece.Queen(0).name, "red")
        self.board[0][4] = colored(piece.King(0).name, "red")
        self.board[0][5] = colored(piece.Bishop(0).name, "red")
        self.board[0][6] = colored(piece.Knight(0).name, "red")
        self.board[0][7] = colored(piece.Rook(0).name, "red")
            
            
        self.board[7][0] = colored(piece.Rook(1).name, "blue")
        self.board[7][1] = colored(piece.Knight(1).name, "blue")
        self.board[7][2] = colored(piece.Bishop(1).name, "blue")
        self.board[7][3] = colored(piece.Queen(1).name, "blue")
        self.board[7][4] = colored(piece.King(1).name, "blue")
        self.board[7][5] = colored(piece.Bishop(1).name, "blue")
        self.board[7][6] = colored(piece.Knight(1).name, "blue")
        self.board[7][7] = colored(piece.Rook(1).name, "blue")        
            
    def print_board(self):
        buffer = str()
        for i in range(17):
            buffer += "- "
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