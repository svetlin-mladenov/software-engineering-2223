from enum import Enum
from termcolor import cprint

class White(Enum):
     Pawn = " ♙ "
     Rook = " ♖ "
     Knight = " ♘ "
     Bishop = " ♗ "
     King = " ♔ "
     Queen = " ♕ "

class Black(Enum):
     Pawn = " ♟ "
     Rook = " ♜ "
     Knight = " ♞ "
     Bishop = " ♝ "
     King = " ♚ "
     Queen = " ♛ "

white_piece_symbols = {"P": White.Pawn.value, "R": White.Rook.value, "N": White.Knight.value, "B": White.Bishop.value, "K": White.King.value, "Q": White.Queen.value}
black_piece_symbols = {"p": Black.Pawn.value, "r": Black.Rook.value, "n": Black.Knight.value, "b": Black.Bishop.value, "k": Black.King.value, "q": Black.Queen.value}

class Chessboard:
    def __init__(self, fen):
        self.fen = fen
        self.board = self.parse_fen()

    def parse_fen(self):
        board = []
        rows = self.fen.split("/")
        for row in rows:
            board_row = []
            for ch in row:
                if ch.isdigit():
                    for i in range(int(ch)):
                        board_row.append(" ")
                else:
                    if ch.isupper():
                        board_row.append(white_piece_symbols[ch])
                    else:
                        board_row.append(black_piece_symbols[ch])
            board.append(board_row)
        return board

    def give_num(self, value):
        return " {} {}".format(value, "")
       

    def print_board(self):
        color = "white"
        for i, row in enumerate(self.board):
            cprint(self.give_num(8-i), "white", "on_grey", attrs=["bold"], end="")
            for j, square in enumerate(row):
                if square == " ":
                    if (8 - i) % 2 == 0:
                        if (j % 2)  == 0:
                            cprint("   ", color, "on_white",end="")
                        else:
                            cprint("   ", color,end="")
                    else:
                        if (j % 2)  == 0:
                            cprint("   ", color, end="")
                        else:
                            cprint("   ", color, "on_white",end="")
                else:
                    if (8 - i) % 2 == 0:
                        if (j % 2)  == 0:
                            cprint(square, color, "on_white",end="")
                        else:
                            cprint(square, color,end="")
                    else:
                        if (j % 2)  == 0:
                            cprint(square, color, end="")
                        else:
                            cprint(square, color, "on_white",end="")
                if color == "white":
                    color = "grey"
                else:
                    color = "white"
            print()
            if (i+1)%2 == 0:
                color = "white"
            else:
                color = "grey"


fen = "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K"
chessboard = Chessboard(fen)
chessboard.print_board()