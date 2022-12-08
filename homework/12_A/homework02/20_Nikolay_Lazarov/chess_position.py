from chess_classes import *

position1 = ChessPosition()

position1.new_position()

Queen = ChessFigure (Color.BLACK,Figure.QUEEN,1,"h")
King = ChessFigure(Color.WHITE,Figure.KING,3,"a")
Queen2 = ChessFigure (Color.WHITE,Figure.QUEEN,3,"h")
Rook = ChessFigure(Color.BLACK,Figure.ROOK,1,"a")
Rook2 = ChessFigure(Color.WHITE,Figure.ROOK,2,"a")

position1.add_figure(Queen2)
position1.add_figure(Queen)
position1.add_figure(King)
position1.add_figure(Rook)
position1.add_figure(Rook2)

for i in range (0,8,2):
    position1.add_figure(ChessFigure(Color.BLACK,Figure.PAWN,i,"g"))

for i in range (0,8,3):
    position1.add_figure(ChessFigure(Color.WHITE,Figure.PAWN,i,"b"))


position1.print_position()
