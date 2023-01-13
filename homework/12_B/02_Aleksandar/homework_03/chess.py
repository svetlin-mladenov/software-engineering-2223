from termcolor import *


class Rook():
    def __init__(self, color):
        self.color = color
        if self.color == "Black" or self.color == "black":
            self.symbol = "♜"
        else:
            self.symbol = "♖"


class Knight():
    def __init__(self, color):
        self.color = color
        if self.color == "Black" or self.color == "black":
            self.symbol = "♞"
        else:
            self.symbol = "♘"


class Bishop():
    def __init__(self, color):
        self.color = color
        if self.color == "Black" or self.color == "black":
            self.symbol = "♝"
        else:
            self.symbol = "♗"


class Queen():
    def __init__(self, color):
        self.color = color
        if self.color == "Black" or self.color == "black":
            self.symbol = "♛"
        else:
            self.symbol = "♕"


class King():
    def __init__(self, color):
        self.color = color
        if self.color == "Black" or self.color == "black":
            self.symbol = "♚"
        else:
            self.symbol = "♔"


class Pawn():
    def __init__(self, color):
        self.color = color
        if self.color == "Black" or self.color == "black":
            self.symbol = "♟"
        else:
            self.symbol = "♙"


board = [[None for i in range(8)] for j in range(8)]


# Structure of Black Pieces and then for cycle for placing them on board
BlackPieces = [Rook("black").symbol, Knight("black").symbol, Bishop("black").symbol, Queen(
    "black").symbol, King("black").symbol, Bishop("black").symbol, Knight("black").symbol, Rook("black").symbol]

for i in range(8):
    board[0][i] = BlackPieces[i]
    board[1][i] = Pawn("black").symbol

# Structure of White Pieces and then for cycle for placing them on board
WhitePieces = [Rook("white").symbol, Knight("white").symbol, Bishop("white").symbol, Queen(
    "white").symbol, King("white").symbol, Bishop("white").symbol, Knight("white").symbol, Rook("white").symbol]

for i in range(8):
    board[7][i] = WhitePieces[i]
    board[6][i] = Pawn("white").symbol

chess_row = 8
for i, row in enumerate(board):
    print()
    print(chess_row, end=" ")
    for pos, j in enumerate(row):
        if i % 2 == 0:
            if type(j) is str:
                j += " "
            if pos % 2 == 0:
                cprint(j or "  ", 'yellow', attrs=['reverse'], end="")
            else:
                cprint(j or "  ", 'white', attrs=['reverse'], end="")
        else:
            if type(j) is str:
                j += " "
            if pos % 2 == 0:
                cprint(j or "  ", 'white', attrs=['reverse'], end="")
            else:
                cprint(j or "  ", 'yellow', attrs=['reverse'], end="")
    if i == 7:
        print()
        print(' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', sep=" ")
    chess_row -= 1

print("After fen parser: ")


def parse_fen(fen_string):
    rows = fen_string.split("/")
    board = [[None for i in range(8)] for j in range(8)]
    for r, row in enumerate(rows):
        c = 0
        for i in row:
            if i.isnumeric():
                c += int(i)
            else:
                if i == 'p':
                    board[r][c] = Pawn("black").symbol
                elif i == 'P':
                    board[r][c] = Pawn("white").symbol
                elif i == 'r':
                    board[r][c] = Rook("black").symbol
                elif i == 'R':
                    board[r][c] = Rook("white").symbol
                elif i == 'n':
                    board[r][c] = Knight("black").symbol
                elif i == 'N':
                    board[r][c] = Knight("white").symbol
                elif i == 'b':
                    board[r][c] = Bishop("black").symbol
                elif i == 'B':
                    board[r][c] = Bishop("white").symbol
                elif i == 'q':
                    board[r][c] = Queen("black").symbol
                elif i == 'Q':
                    board[r][c] = Queen("white").symbol
                elif i == 'k':
                    board[r][c] = King("black").symbol
                elif i == 'K':
                    board[r][c] = King("white").symbol
                c += 1
    return board


fen_string = "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K"
board = parse_fen(fen_string)

chess_row = 8
for i, row in enumerate(board):
    print()
    print(chess_row, end=" ")
    for pos, j in enumerate(row):
        if i % 2 == 0:
            if type(j) is str:
                j += " "
            if pos % 2 == 0:
                cprint(j or "  ", 'yellow', attrs=['reverse'], end="")
            else:
                cprint(j or "  ", 'white', attrs=['reverse'], end="")
        else:
            if type(j) is str:
                j += " "
            if pos % 2 == 0:
                cprint(j or "  ", 'white', attrs=['reverse'], end="")
            else:
                cprint(j or "  ", 'yellow', attrs=['reverse'], end="")
    if i == 7:
        print()
        print(' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', sep=" ")
    chess_row -= 1
