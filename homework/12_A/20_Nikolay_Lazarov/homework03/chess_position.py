from chess_classes import *


string = "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25"
# string = "r5rk/1p1q1p1p/p7"


positions = string.split(" ")
ranks = positions[0].split("/")
print(positions[0])
print(ranks)

position1 = ChessPosition()

position1.new_position()

row = 7
col = "a"

for rows in ranks:
    for cell in rows:
        if cell.isnumeric():
            col = chr( ord(col) + int(cell))
            # print (cell)
            continue
         
        (figure,color) = get_figure(cell)
        position1.add_figure(ChessFigure(color,figure,row,col))
        print( (figure,color),row,col)
        col =chr(ord(col)+1)
    print("new")    
    row -= 1
    col = "a"

# for i in positions[0]:
#     (figure, color) = get_figure(i)
#     position1.add_figure(figure, color,)

# Queen = ChessFigure (Color.BLACK,Figure.QUEEN,1,"h")
# King = ChessFigure(Color.WHITE,Figure.KING,3,"a")
# Queen2 = ChessFigure (Color.WHITE,Figure.QUEEN,3,"h")
# Rook = ChessFigure(Color.BLACK,Figure.ROOK,1,"a")
# Rook2 = ChessFigure(Color.WHITE,Figure.ROOK,2,"a")

# position1.add_figure(Queen2)
# position1.add_figure(Queen)
# position1.add_figure(King)
# position1.add_figure(Rook)
# position1.add_figure(Rook2)

# for i in range (0,8,2):
#     position1.add_figure(ChessFigure(Color.BLACK,Figure.PAWN,i,"g"))

# for i in range (0,8,3):
#     position1.add_figure(ChessFigure(Color.WHITE,Figure.PAWN,i,"b"))


position1.print_position()
