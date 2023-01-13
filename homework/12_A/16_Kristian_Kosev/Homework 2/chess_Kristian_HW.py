from termcolor import colored


class Piece:
    def __init__(self, emoji):
        self.emoji = emoji

    def __str__(self):
        return self.emoji


class Chessboard:
    def __init__(self) :
        self.chessboard = [[None for j in range(8)] for i in range(8)]
        for i in range(8):
            self.chessboard[6][i] = Piece(" ♟ ")
            self.chessboard[1][i] = Piece(" ♙ ")
            self.chessboard[0][0] = Piece(" ♖ ")
            self.chessboard[0][1] = Piece(" ♘ ")
            self.chessboard[0][2] = Piece(" ♗ ")
            self.chessboard[0][3] = Piece(" ♕ ")
            self.chessboard[0][4] = Piece(" ♔ ")
            self.chessboard[0][5] = Piece(" ♗ ")
            self.chessboard[0][6] = Piece(" ♘ ")
            self.chessboard[0][7] = Piece(" ♖ ")
            self.chessboard[7][0] = Piece(" ♜ ")
            self.chessboard[7][1] = Piece(" ♞ ")
            self.chessboard[7][2] = Piece(" ♝ ")
            self.chessboard[7][3] = Piece(" ♛ ")
            self.chessboard[7][4] = Piece(" ♚ ")
            self.chessboard[7][5] = Piece(" ♝ ")
            self.chessboard[7][6] = Piece(" ♞ ")
            self.chessboard[7][7] = Piece(" ♜ ")

            def printLayout(self):
        for i in range(0, 8):
            for j in range(0, 8):
                if self.chessboard[i][j] == None:
                    print(colored("   ", on_color= "on_white" if ((i + j) % 2) == 1 else "on_grey"), end="")
                else:
                    print(colored(self.chessboard[i][j], on_color= "on_white" if ((i + j) % 2) == 1 else "on_grey"), end="")
                if j == 7:
                    print()

class Piece:
    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return self.symbol

chessboard = Chessboard()
chessboard.printLayout()