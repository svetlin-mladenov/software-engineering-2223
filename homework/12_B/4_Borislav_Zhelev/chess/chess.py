from enum import Enum
from termcolor import cprint, colored

all_pieces = [["♟", "♜", "♝", "♞", "♛", "♚", " "],["♙","♖","♗","♘","♕","♔", " "]]

class Letters(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8

class Pieces(Enum):
    PAWN = 0
    ROOK = 1
    BISHOP = 2
    KNIGHT = 3
    QUEEN = 4
    KING = 5
    NONE = 6

class Colors(Enum):
    BLACK = 0
    WHITE = 1

class Chess_pos:

    def __init__(self, piece:Pieces, piece_color:Colors, x:Letters, y:int) -> None:
        self.piece = piece
        self.piece_color = piece_color
        self.x = x
        self.y = y
        self.color = Colors((self.x.value + self.y)%2)#a1 -> (1+1)%2 = 0 = black


    def is_valid_x(self) -> bool:
        if type(self.x) == Letters:
            return True
        else:
            return False

    def is_valid_y(self) -> bool:
        if type(self.y) == int:
            if self.y >= 1 and self.y <= 8:
                return True
            else:
                return False
        else:
            return False

    def is_valid_piece(self) -> bool:
        if type(self.piece) == Pieces:
            return True
        else:
            return False

    def is_valid_piece_color(self) -> bool:
        if type(self.piece_color) == Colors:
            return True
        else:
            return False

    def is_valid(self) -> bool:
        if self.is_valid_x() and self.is_valid_y() and self.is_valid_piece() and self.is_valid_piece_color():
            return True
        else:
            return False

    def my_print(self) -> None:
        if self.is_valid():
            if self.color.value == 0:#black
                print(all_pieces[self.piece_color.value][self.piece.value], "", end=' ')
            else:
                cprint((str(all_pieces[self.piece_color.value][self.piece.value])+" "),  None, "on_white",  end=' ')
        else:
            print("invalid position")

a1 = Chess_pos(Pieces.ROOK, Colors.WHITE, Letters.A, 1)
a2 = Chess_pos(Pieces.KNIGHT, Colors.WHITE, Letters.A, 2)
a3 = Chess_pos(Pieces.BISHOP, Colors.WHITE, Letters.A, 3)
a4 = Chess_pos(Pieces.QUEEN, Colors.WHITE, Letters.A, 4)
a5 = Chess_pos(Pieces.KING, Colors.WHITE, Letters.A, 5)
a6 = Chess_pos(Pieces.BISHOP, Colors.WHITE, Letters.A, 6)
a7 = Chess_pos(Pieces.KNIGHT, Colors.WHITE, Letters.A, 7)
a8 = Chess_pos(Pieces.ROOK, Colors.WHITE, Letters.A, 8)
b1 = Chess_pos(Pieces.PAWN, Colors.WHITE, Letters.B, 1)
b2 = Chess_pos(Pieces.PAWN, Colors.WHITE, Letters.B, 2)
b3 = Chess_pos(Pieces.PAWN, Colors.WHITE, Letters.B, 3)
b4 = Chess_pos(Pieces.PAWN, Colors.WHITE, Letters.B, 4)
b5 = Chess_pos(Pieces.PAWN, Colors.WHITE, Letters.B, 5)
b6 = Chess_pos(Pieces.PAWN, Colors.WHITE, Letters.B, 6)
b7 = Chess_pos(Pieces.PAWN, Colors.WHITE, Letters.B, 7)
b8 = Chess_pos(Pieces.PAWN, Colors.WHITE, Letters.B, 8)
c1 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.C, 1)
c2 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.C, 2)
c3 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.C, 3)
c4 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.C, 4)
c5 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.C, 5)
c6 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.C, 6)
c7 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.C, 7)
c8 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.C, 8)
d1 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.D, 1)
d2 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.D, 2)
d3 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.D, 3)
d4 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.D, 4)
d5 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.D, 5)
d6 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.D, 6)
d7 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.D, 7)
d8 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.D, 8)
e1 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.E, 1)
e2 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.E, 2)
e3 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.E, 3)
e4 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.E, 4)
e5 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.E, 5)
e6 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.E, 6)
e7 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.E, 7)
e8 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.E, 8)
f1 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.F, 1)
f2 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.F, 2)
f3 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.F, 3)
f4 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.F, 4)
f5 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.F, 5)
f6 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.F, 6)
f7 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.F, 7)
f8 = Chess_pos(Pieces.NONE, Colors.WHITE, Letters.F, 8)
g1 = Chess_pos(Pieces.PAWN, Colors.BLACK, Letters.G, 1)
g2 = Chess_pos(Pieces.PAWN, Colors.BLACK, Letters.G, 2)
g3 = Chess_pos(Pieces.PAWN, Colors.BLACK, Letters.G, 3)
g4 = Chess_pos(Pieces.PAWN, Colors.BLACK, Letters.G, 4)
g5 = Chess_pos(Pieces.PAWN, Colors.BLACK, Letters.G, 5)
g6 = Chess_pos(Pieces.PAWN, Colors.BLACK, Letters.G, 6)
g7 = Chess_pos(Pieces.PAWN, Colors.BLACK, Letters.G, 7)
g8 = Chess_pos(Pieces.PAWN, Colors.BLACK, Letters.G, 8)
h1 = Chess_pos(Pieces.ROOK, Colors.BLACK, Letters.H, 1)
h2 = Chess_pos(Pieces.KNIGHT, Colors.BLACK, Letters.H, 2)
h3 = Chess_pos(Pieces.BISHOP, Colors.BLACK, Letters.H, 3)
h4 = Chess_pos(Pieces.KING, Colors.BLACK, Letters.H, 4)
h5 = Chess_pos(Pieces.QUEEN, Colors.BLACK, Letters.H, 5)
h6 = Chess_pos(Pieces.BISHOP, Colors.BLACK, Letters.H, 6)
h7 = Chess_pos(Pieces.KNIGHT, Colors.BLACK, Letters.H, 7)
h8 = Chess_pos(Pieces.ROOK, Colors.BLACK, Letters.H, 8)

#an array of all chess positions below
chess_board = [a1, a2, a3, a4, a5, a6, a7, a8, b1, b2, b3, b4, b5, b6, b7, b8, c1, c2, c3, c4, c5, c6, c7, c8, d1, d2, d3, d4, d5, d6, d7, d8, e1, e2, e3, e4, e5, e6, e7, e8, f1, f2, f3, f4, f5, f6, f7, f8, g1, g2, g3, g4, g5, g6, g7, g8, h1, h2, h3, h4, h5, h6, h7, h8,]
for i in range(64):
    chess_board[i].my_print()
    if (i + 1) % 8 == 0:
        print()#new line