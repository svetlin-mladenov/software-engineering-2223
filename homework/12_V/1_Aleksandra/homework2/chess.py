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

    def FEN_to_Board(self, fen):
        self.clear_board()
        i = -1
        for row in fen.split('/'):
            i += 1
            j = -1
            for c in row:
                j += 1
                if c == ' ':
                    break
                elif c in '12345678':
                    j += int(c) - 1
                elif c == 'p':
                    self.board[i][j] = figure.Pawn(False)
                elif c == 'P':
                    self.board[i][j] = figure.Pawn(True)
                elif c == 'k':
                    self.board[i][j] = figure.King(False)
                elif c == 'K':
                    self.board[i][j] = figure.King(True)
                elif c == 'q':
                    self.board[i][j] = figure.Queen(False)
                elif c == 'Q':
                    self.board[i][j] = figure.Queen(True)
                elif c == 'r':
                    self.board[i][j] = figure.Rook(False)
                elif c == 'R':
                    self.board[i][j] = figure.Rook(True)
                elif c == 'n':
                    self.board[i][j] = figure.Knight(False)
                elif c == 'N':
                    self.board[i][j] = figure.Knight(True)
                elif c == 'b':
                    self.board[i][j] = figure.Bishop(False)
                elif c == 'B':
                    self.board[i][j] = figure.Bishop(True)

    def clear_board(self):
        for i in range(8):
            for j in range(8):
                self.board[i][j] = None


os.system('color')
Game = Chess()
print("Starting position")
Game.print_board()
print("FEN position")
Game.FEN_to_Board("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25")
Game.print_board()
