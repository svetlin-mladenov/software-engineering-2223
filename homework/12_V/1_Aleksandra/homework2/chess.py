import figure
import os


class Chess:
    def __init__(self):
        self.board = []
        for i in range(8):
            self.board.append([None] * 8)
        self.board[7][0] = figure.Rook(True)
        self.board[7][1] = figure.Knight(True)
        self.board[7][2] = figure.Bishop(True)
        self.board[7][3] = figure.Queen(True)
        self.board[7][4] = figure.King(True)
        self.board[7][5] = figure.Bishop(True)
        self.board[7][6] = figure.Knight(True)
        self.board[7][7] = figure.Rook(True)

        for i in range(8):
            self.board[6][i] = figure.Pawn(True)

        self.board[0][0] = figure.Rook(False)
        self.board[0][1] = figure.Knight(False)
        self.board[0][2] = figure.Bishop(False)
        self.board[0][3] = figure.Queen(False)
        self.board[0][4] = figure.King(False)
        self.board[0][5] = figure.Bishop(False)
        self.board[0][6] = figure.Knight(False)
        self.board[0][7] = figure.Rook(False)

        for i in range(8):
            self.board[1][i] = figure.Pawn(False)

    def print_board(self):
        buffer = ""
        for i in range(33):
            buffer += "-"
        print(buffer)
        for i in range(len(self.board)):
            tmp_str = "|"
            for j in self.board[i]:
                if j is None:
                    tmp_str += "   |"
                else:
                    tmp_str += (" " + str(j) + " |")
            print(tmp_str)
        buffer = ""
        for i in range(33):
            buffer += "-"
        print(buffer)


os.system('color')
Game = Chess()
Game.print_board()