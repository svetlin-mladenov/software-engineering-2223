from enum import Enum

class Columns(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8

class Names(Enum):
    PAWN = 0
    ROOK = 1
    BISHOP = 2
    KNIGHT = 3
    QUEEN = 4
    KING = 5
    EMPTY = 6

class Colors(Enum):
   BLACK = 0
   WHITE = 1
   EMPTY = 3


class Position:
    def __init__(self, name:Names, color:Colors, c:Columns, r:int,image):
        self.name = name
        self.c = c
        self.r = r
        self.color = color
        self.image = image


a1 = Position(Names.ROOK, Colors.WHITE, Columns.A, 1,"♖")
b1= Position(Names.KNIGHT, Colors.WHITE, Columns.B, 1, "♘")
c1 = Position(Names.BISHOP, Colors.WHITE, Columns.C, 1, "♗")
d1 = Position(Names.QUEEN, Colors.WHITE, Columns.D, 1, "♕")
e1 = Position(Names.KING, Colors.WHITE, Columns.E, 1, "♔")
f1 = Position(Names.BISHOP, Colors.WHITE, Columns.F, 1,"♗")
g1 = Position(Names.KNIGHT, Colors.WHITE, Columns.G, 1, "♘")
h1 = Position(Names.ROOK, Colors.WHITE, Columns.H, 1,"♖")


a8 = Position(Names.ROOK, Colors.BLACK, Columns.A, 8,"♜")
b8 = Position(Names.KNIGHT, Colors.BLACK, Columns.B, 8,"♞")
c8 = Position(Names.BISHOP, Colors.BLACK, Columns.C, 8,"♝")
d8 = Position(Names.KING, Colors.BLACK, Columns.D, 8,"♚")
e8 = Position(Names.QUEEN, Colors.BLACK, Columns.E, 8,"♛")
f8 = Position(Names.BISHOP, Colors.BLACK, Columns.F, 8,"♝")
g8 = Position(Names.KNIGHT, Colors.BLACK, Columns.G, 8,"♞")
h8 = Position(Names.ROOK, Colors.BLACK, Columns.H, 8,"♜")

a2 = Position(Names.PAWN, Colors.WHITE, Columns.A, 2,"♙")
b2 = Position(Names.PAWN, Colors.WHITE, Columns.B, 2,"♙")
c2 = Position(Names.PAWN, Colors.WHITE, Columns.C, 2,"♙")
d2 = Position(Names.PAWN, Colors.WHITE, Columns.D, 2,"♙")
e2 = Position(Names.PAWN, Colors.WHITE, Columns.E, 2,"♙")
f2 = Position(Names.PAWN, Colors.WHITE, Columns.F, 2,"♙")
g2 = Position(Names.PAWN, Colors.WHITE, Columns.G, 2,"♙")
h2 = Position(Names.PAWN, Colors.WHITE, Columns.H, 2,"♙")

a7 = Position(Names.PAWN, Colors.BLACK, Columns.A, 1,"♟")
b7 = Position(Names.PAWN, Colors.BLACK, Columns.B, 2,"♟")
c7 = Position(Names.PAWN, Colors.BLACK, Columns.C, 3,"♟")
d7 = Position(Names.PAWN, Colors.BLACK, Columns.D, 4,"♟")
e7 = Position(Names.PAWN, Colors.BLACK, Columns.E, 5,"♟")
f7 = Position(Names.PAWN, Colors.BLACK, Columns.F, 6,"♟")
g7 = Position(Names.PAWN, Colors.BLACK, Columns.G, 7,"♟")
h7 = Position(Names.PAWN, Colors.BLACK, Columns.H, 8,"♟")

a3 = Position(Names.EMPTY, Colors.EMPTY, Columns.A, 3,".")
b3 = Position(Names.EMPTY, Colors.EMPTY, Columns.B, 3,".")
c3 = Position(Names.EMPTY, Colors.EMPTY, Columns.C, 3,".")
d3 = Position(Names.EMPTY, Colors.EMPTY, Columns.D, 3,".")
e3 = Position(Names.EMPTY, Colors.EMPTY, Columns.E, 3,".")
f3 = Position(Names.EMPTY, Colors.EMPTY, Columns.F, 3,".")
g3 = Position(Names.EMPTY, Colors.EMPTY, Columns.G, 3,".")
h3 = Position(Names.EMPTY, Colors.EMPTY, Columns.H, 3,".")

a4 = Position(Names.EMPTY, Colors.EMPTY, Columns.A, 4,".")
b4 = Position(Names.EMPTY, Colors.EMPTY, Columns.B, 4,".")
c4 = Position(Names.EMPTY, Colors.EMPTY, Columns.C, 4,".")
d4 = Position(Names.EMPTY, Colors.EMPTY, Columns.D, 4,".")
e4 = Position(Names.EMPTY, Colors.EMPTY, Columns.E, 4,".")
f4 = Position(Names.EMPTY, Colors.EMPTY, Columns.F, 4,".")
g4 = Position(Names.EMPTY, Colors.EMPTY, Columns.G, 4,".")
h4 = Position(Names.EMPTY, Colors.EMPTY, Columns.H, 4,".")

a5 = Position(Names.EMPTY, Colors.EMPTY, Columns.A, 5,".")
b5 = Position(Names.EMPTY, Colors.EMPTY, Columns.B, 5,".")
c5 = Position(Names.EMPTY, Colors.EMPTY, Columns.C, 5,".")
d5 = Position(Names.EMPTY, Colors.EMPTY, Columns.D, 5,".")
e5 = Position(Names.EMPTY, Colors.EMPTY, Columns.E, 5,".")
f5 = Position(Names.EMPTY, Colors.EMPTY, Columns.F, 5,".")
g5 = Position(Names.EMPTY, Colors.EMPTY, Columns.G, 5,".")
h5 = Position(Names.EMPTY, Colors.EMPTY, Columns.H, 5,".")

a6 = Position(Names.EMPTY, Colors.EMPTY, Columns.A, 6,".")
b6 = Position(Names.EMPTY, Colors.EMPTY, Columns.B, 6,".")
c6 = Position(Names.EMPTY, Colors.EMPTY, Columns.C, 6,".")
d6 = Position(Names.EMPTY, Colors.EMPTY, Columns.D, 6,".")
e6 = Position(Names.EMPTY, Colors.EMPTY, Columns.E, 6,".")
f6 = Position(Names.EMPTY, Colors.EMPTY, Columns.F, 6,".")
g6 = Position(Names.EMPTY, Colors.EMPTY, Columns.G, 6,".")
h6 = Position(Names.EMPTY, Colors.EMPTY, Columns.H, 6,".")

board = [[a1, a2, a3, a4, a5, a6, a7, a8], [b1, b2, b3, b4, b5, b6, b7, b8], 
[c1, c2, c3, c4, c5, c6, c7, c8],[d1, d2, d3, d4, d5, d6, d7, d8]
, [e1, e2, e3, e4, e5, e6, e7, e8], [f1, f2, f3, f4, f5, f6, f7, f8], 
[g1, g2, g3, g4, g5, g6, g7, g8], [h1, h2, h3, h4, h5, h6, h7, h8]]    


for i in range (8):
   print("\n")
   for j in range (8):
      print(board[j][i].image, end=" ")

print(str(g1.name) + "-->" + g1.image)
