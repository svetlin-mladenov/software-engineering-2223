from termcolor import cprint

class ChessPosition:
    def __init__(self):
        self.board = [[" " for _ in range(8)] for _ in range(8)]

    def start(self):
        self.board[7][7] = "♖"
        self.board[7][0] = "♖"
        self.board[7][6] = "♘"
        self.board[7][1] = "♘"
        self.board[7][5] = "♗"
        self.board[7][2] = "♗"
        self.board[7][4] = "♔"
        self.board[7][3] = "♕"
        for i in range(8):
            self.board[6][i] = "♙"

        for i in range(8):
            self.board[1][i] = "♟"
        self.board[0][7] = "♜"
        self.board[0][0] = "♜"
        self.board[0][6] = "♞"
        self.board[0][1] = "♞"
        self.board[0][5] = "♝"
        self.board[0][2] = "♝"
        self.board[0][4] = "♚"
        self.board[0][3] = "♛"

    def print(self):
        for x in range(8):
            for y in range(8):
                print(self.board[x][y], end = "") if (x + y) % 2 else cprint(self.board[x][y], "grey", "on_white", end = "")
            print()

che_p = ChessPosition()
che_p.start()
che_p.print()
