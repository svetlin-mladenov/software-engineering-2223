class Board:
    def __init__(self) :
        self.board = [[None for j in range(8)] for i in range(8)]
        for i in range(8):
            self.board[6][i] = Piece("♟ ︎")
            self.board[1][i] = Piece("♙ ")
        self.board[0][0] = Piece("♖ ")
        self.board[0][1] = Piece("♘ ")
        self.board[0][2] = Piece("♗ ")
        self.board[0][3] = Piece("♕ ")
        self.board[0][4] = Piece("♔ ")
        self.board[0][5] = Piece("♗ ")
        self.board[0][6] = Piece("♘ ")
        self.board[0][7] = Piece("♖ ")
        self.board[7][0] = Piece("♜ ")
        self.board[7][1] = Piece("♞ ")
        self.board[7][2] = Piece("♝ ")
        self.board[7][3] = Piece("♛ ")
        self.board[7][4] = Piece("♚ ")
        self.board[7][5] = Piece("♝ ")
        self.board[7][6] = Piece("♞ ")
        self.board[7][7] = Piece("♜ ")

    def printLayout(self):
        for i in range(0, 8):
            for j in range(0, 8):
                if self.board[i][j] == None:
                    print("  ", end="")
                else:
                    print(self.board[i][j], end="")
                if j == 7:
                    print("\n", end="")

class Piece:
    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return self.symbol

chessBoard = Board()
chessBoard.printLayout()
