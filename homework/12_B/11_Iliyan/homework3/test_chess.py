from ChessPieces import King, Queen, Rook, Bishop, Knight, Pawn
from ChessBoard import ChessBoard, EnumChessPiece

##################################################
# Testing pieces colour_name constructors
##################################################

def test_piece_name():
  assert King(EnumChessPiece.WHITE_KING).name     == "King"
  assert Queen(EnumChessPiece.BLACK_QUEEN).name   == "Queen"
  assert Rook(EnumChessPiece.WHITE_ROOK).name     == "Rook"
  assert Bishop(EnumChessPiece.BLACK_BISHOP).name == "Bishop"
  assert Knight(EnumChessPiece.WHITE_KNIGHT).name == "Knight"
  assert Pawn(EnumChessPiece.BLACK_PAWN).name     == "Pawn"

def test_piece_colour():
  assert King(EnumChessPiece.WHITE_KING).colour     == "White"
  assert Queen(EnumChessPiece.BLACK_QUEEN).colour   == "Black"
  assert Rook(EnumChessPiece.WHITE_ROOK).colour     == "White"
  assert Bishop(EnumChessPiece.BLACK_BISHOP).colour == "Black"
  assert Knight(EnumChessPiece.WHITE_KNIGHT).colour == "White"
  assert Pawn(EnumChessPiece.BLACK_PAWN).colour     == "Black"

def test_piece_value():
  assert King(EnumChessPiece.WHITE_KING).value     == None
  assert Queen(EnumChessPiece.BLACK_QUEEN).value   == 9
  assert Rook(EnumChessPiece.WHITE_ROOK).value     == 5
  assert Bishop(EnumChessPiece.BLACK_BISHOP).value == 3
  assert Knight(EnumChessPiece.WHITE_KNIGHT).value == 3
  assert Pawn(EnumChessPiece.BLACK_PAWN).value     == 1

def test_piece_display_icon():
  assert King(EnumChessPiece.BLACK_KING).display_icon     == '\u2654'
  assert King(EnumChessPiece.WHITE_KING).display_icon     == '\u265A'

  assert Queen(EnumChessPiece.BLACK_QUEEN).display_icon   == '\u2655'
  assert Queen(EnumChessPiece.WHITE_QUEEN).display_icon   == '\u265B'

  assert Rook(EnumChessPiece.BLACK_ROOK).display_icon     == '\u2656'
  assert Rook(EnumChessPiece.WHITE_ROOK).display_icon     == '\u265C'

  assert Bishop(EnumChessPiece.BLACK_BISHOP).display_icon == '\u2657'
  assert Bishop(EnumChessPiece.WHITE_BISHOP).display_icon == '\u265D'

  assert Knight(EnumChessPiece.BLACK_KNIGHT).display_icon == '\u2658'
  assert Knight(EnumChessPiece.WHITE_KNIGHT).display_icon == '\u265E'

  assert Pawn(EnumChessPiece.BLACK_PAWN).display_icon     == '\u2659'
  assert Pawn(EnumChessPiece.WHITE_PAWN).display_icon     == '\u265F'

def test_piece_notation():
  assert King(EnumChessPiece.WHITE_KING).notation     == "K"
  assert Queen(EnumChessPiece.BLACK_QUEEN).notation   == "q"
  assert Rook(EnumChessPiece.WHITE_ROOK).notation     == "R"
  assert Bishop(EnumChessPiece.BLACK_BISHOP).notation == "b"
  assert Knight(EnumChessPiece.WHITE_KNIGHT).notation == "N"
  assert Knight(EnumChessPiece.BLACK_KNIGHT).notation == "n"
  assert Pawn(EnumChessPiece.BLACK_PAWN).notation     == "p"

##################################################
# Testing chesspieces notation constructor
##################################################

def test_piece_name_notation():
  assert King(notation='K').name   == "King"
  assert Queen(notation='q').name  == "Queen"
  assert Rook(notation='R').name   == "Rook"
  assert Bishop(notation='b').name == "Bishop"
  assert Knight(notation='N').name == "Knight"
  assert Pawn(notation='p').name   == "Pawn"

def test_piece_colour_notation():
  assert King(notation='K').colour   == "White"
  assert Queen(notation='q').colour  == "Black"
  assert Rook(notation='R').colour   == "White"
  assert Bishop(notation='b').colour == "Black"
  assert Knight(notation='N').colour == "White"
  assert Pawn(notation='p').colour   == "Black"

def test_piece_value_notation():
  assert King(notation='K').value   == None
  assert Queen(notation='q').value  == 9
  assert Rook(notation='R').value   == 5
  assert Bishop(notation='b').value == 3
  assert Knight(notation='N').value == 3
  assert Pawn(notation='p').value   == 1

def test_piece_display_icon_notation():
  assert King(notation='k').display_icon   == '\u2654'
  assert King(notation='K').display_icon   == '\u265A'

  assert Queen(notation='q').display_icon  == '\u2655'
  assert Queen(notation='Q').display_icon  == '\u265B'

  assert Rook(notation='r').display_icon   == '\u2656'
  assert Rook(notation='R').display_icon   == '\u265C'

  assert Bishop(notation='b').display_icon == '\u2657'
  assert Bishop(notation='B').display_icon == '\u265D'

  assert Knight(notation='n').display_icon == '\u2658'
  assert Knight(notation='N').display_icon == '\u265E'
  
  assert Pawn(notation='p').display_icon   == '\u2659'
  assert Pawn(notation='P').display_icon   == '\u265F'

def test_piece_notation_notation():
  assert King(notation='K').notation   == "K"
  assert Queen(notation='q').notation  == "q"
  assert Rook(notation='R').notation   == "R"
  assert Bishop(notation='b').notation == "b"
  assert Knight(notation='N').notation == "N"
  assert Pawn(notation='p').notation   == "p"

##################################################
# Testing chessboard constructor
##################################################

def test_chessboard():
  board = ChessBoard()
  
  starting_chess_board = [[Rook(EnumChessPiece.BLACK_ROOK), Knight(EnumChessPiece.BLACK_KNIGHT), Bishop(EnumChessPiece.BLACK_BISHOP), Queen(EnumChessPiece.BLACK_QUEEN), King(EnumChessPiece.BLACK_KING), Bishop(EnumChessPiece.BLACK_BISHOP), Knight(EnumChessPiece.BLACK_KNIGHT), Rook(EnumChessPiece.BLACK_ROOK)],
                          [Pawn(EnumChessPiece.BLACK_PAWN), Pawn(EnumChessPiece.BLACK_PAWN), Pawn(EnumChessPiece.BLACK_PAWN), Pawn(EnumChessPiece.BLACK_PAWN), Pawn(EnumChessPiece.BLACK_PAWN), Pawn(EnumChessPiece.BLACK_PAWN), Pawn(EnumChessPiece.BLACK_PAWN), Pawn(EnumChessPiece.BLACK_PAWN)],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [Pawn(EnumChessPiece.WHITE_PAWN), Pawn(EnumChessPiece.WHITE_PAWN), Pawn(EnumChessPiece.WHITE_PAWN), Pawn(EnumChessPiece.WHITE_PAWN), Pawn(EnumChessPiece.WHITE_PAWN), Pawn(EnumChessPiece.WHITE_PAWN), Pawn(EnumChessPiece.WHITE_PAWN), Pawn(EnumChessPiece.WHITE_PAWN)],
                          [Rook(EnumChessPiece.WHITE_ROOK), Knight(EnumChessPiece.WHITE_KNIGHT), Bishop(EnumChessPiece.WHITE_BISHOP), Queen(EnumChessPiece.WHITE_QUEEN), King(EnumChessPiece.WHITE_KING), Bishop(EnumChessPiece.WHITE_BISHOP), Knight(EnumChessPiece.WHITE_KNIGHT), Rook(EnumChessPiece.WHITE_ROOK)]]

  for i in range(len(board.board)):
    for j in range(len(board.board[i])):
      if(board.board[i][j] != None):
        assert (board.board[i][j].name == starting_chess_board[i][j].name and 
               board.board[i][j].colour == starting_chess_board[i][j].colour and
               board.board[i][j].value == starting_chess_board[i][j].value and
               board.board[i][j].display_icon == starting_chess_board[i][j].display_icon)
        
      else:
        assert board.board[i][j] == starting_chess_board[i][j]

def test_build_starting_display_board():
  board = ChessBoard()
  starting_display_board = \
"""
  ┌────┬────┬────┬────┬────┬────┬────┬────┐
8 │ ♖  │ ♘  │ ♗  │ ♕  │ ♔  │ ♗  │ ♘  │ ♖  │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
7 │ ♙  │ ♙  │ ♙  │ ♙  │ ♙  │ ♙  │ ♙  │ ♙  │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
6 │    │    │    │    │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
5 │    │    │    │    │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
4 │    │    │    │    │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
3 │    │    │    │    │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
2 │ ♟  │ ♟  │ ♟  │ ♟  │ ♟  │ ♟  │ ♟  │ ♟  │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
1 │ ♜  │ ♞  │ ♝  │ ♛  │ ♚  │ ♝  │ ♞  │ ♜  │
  └────┴────┴────┴────┴────┴────┴────┴────┘
    A    B    C    D    E    F    G    H
"""
  assert board.display_board == starting_display_board[1:len(starting_display_board)]


def test_build_FEN_display_board():
  board = ChessBoard()
  board.FENparser("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25")
  FEN_display_board = \
"""
  ┌────┬────┬────┬────┬────┬────┬────┬────┐
8 │ ♖  │    │    │    │    │    │ ♖  │ ♔  │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
7 │    │ ♙  │    │ ♕  │    │ ♙  │    │ ♙  │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
6 │ ♙  │    │    │    │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
5 │    │    │    │ ♞  │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
4 │    │    │    │ ♟  │ ♘  │ ♝  │    │ ♗  │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
3 │    │    │ ♟  │    │    │ ♛  │    │ ♟  │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
2 │ ♟  │ ♟  │    │    │    │ ♟  │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
1 │ ♜  │    │    │    │ ♜  │    │    │ ♚  │
  └────┴────┴────┴────┴────┴────┴────┴────┘
    A    B    C    D    E    F    G    H
"""
  print(board.display_board)
  assert board.display_board == FEN_display_board[1:len(FEN_display_board)]