from ChessPieces import King, Queen, Rook, Bishop, Knight, Pawn
from ChessBoard import ChessBoard, EnumChessPiece

import sys
import pytest

##################################################
# Testing pieces invalid cases
##################################################

def test_invalid_piece_position_given_in_constructor():
  with pytest.raises(Exception):
    King(EnumChessPiece.BLACK_KING, "z1")
  with pytest.raises(Exception):
    Queen(EnumChessPiece.WHITE_QUEEN, "c10")
  with pytest.raises(Exception):
    Rook(EnumChessPiece.BLACK_ROOK, "11")
  with pytest.raises(Exception):
    Bishop(EnumChessPiece.WHITE_BISHOP, "aa")
  with pytest.raises(Exception):
    Knight(EnumChessPiece.BLACK_KNIGHT, "rar")
  with pytest.raises(Exception):
    Pawn(EnumChessPiece.WHITE_PAWN, "88")

##################################################
# Testing pieces constructors
##################################################

def test_piece_name():
  assert King(EnumChessPiece.WHITE_KING, "a1").name     == "King"
  assert Queen(EnumChessPiece.BLACK_QUEEN, "c1").name   == "Queen"
  assert Rook(EnumChessPiece.WHITE_ROOK, "h8").name     == "Rook"
  assert Bishop(EnumChessPiece.BLACK_BISHOP, "b3").name == "Bishop"
  assert Knight(EnumChessPiece.WHITE_KNIGHT, "e4").name == "Knight"
  assert Pawn(EnumChessPiece.BLACK_PAWN, "e5").name     == "Pawn"

def test_piece_colour():
  assert King(EnumChessPiece.WHITE_KING, "a1").colour     == "White"
  assert Queen(EnumChessPiece.BLACK_QUEEN, "c1").colour   == "Black"
  assert Rook(EnumChessPiece.WHITE_ROOK, "h8").colour     == "White"
  assert Bishop(EnumChessPiece.BLACK_BISHOP, "b3").colour == "Black"
  assert Knight(EnumChessPiece.WHITE_KNIGHT, "e4").colour == "White"
  assert Pawn(EnumChessPiece.BLACK_PAWN, "e5").colour     == "Black"

def test_piece_position():
  assert King(EnumChessPiece.WHITE_KING, "a1").position     == "a1"
  assert Queen(EnumChessPiece.BLACK_QUEEN, "c1").position   == "c1"
  assert Rook(EnumChessPiece.WHITE_ROOK, "h8").position     == "h8"
  assert Bishop(EnumChessPiece.BLACK_BISHOP, "b3").position == "b3"
  assert Knight(EnumChessPiece.WHITE_KNIGHT, "e4").position == "e4"
  assert Pawn(EnumChessPiece.BLACK_PAWN, "e5").position     == "e5"

def test_piece_value():
  assert King(EnumChessPiece.WHITE_KING, "a1").value     == None
  assert Queen(EnumChessPiece.BLACK_QUEEN, "c1").value   == 9
  assert Rook(EnumChessPiece.WHITE_ROOK, "h8").value     == 5
  assert Bishop(EnumChessPiece.BLACK_BISHOP, "b3").value == 3
  assert Knight(EnumChessPiece.WHITE_KNIGHT, "e4").value == 3
  assert Pawn(EnumChessPiece.BLACK_PAWN, "e5").value     == 1

def test_piece_display_icon():
  assert King(EnumChessPiece.BLACK_KING, "a1").display_icon     == '\u2654'
  assert King(EnumChessPiece.WHITE_KING, "a1").display_icon     == '\u265A'

  assert Queen(EnumChessPiece.BLACK_QUEEN, "c1").display_icon   == '\u2655'
  assert Queen(EnumChessPiece.WHITE_QUEEN, "c1").display_icon   == '\u265B'

  assert Rook(EnumChessPiece.BLACK_ROOK, "h8").display_icon     == '\u2656'
  assert Rook(EnumChessPiece.WHITE_ROOK, "h8").display_icon     == '\u265C'

  assert Bishop(EnumChessPiece.BLACK_BISHOP, "b3").display_icon == '\u2657'
  assert Bishop(EnumChessPiece.WHITE_BISHOP, "b3").display_icon == '\u265D'

  assert Knight(EnumChessPiece.BLACK_KNIGHT, "e4").display_icon == '\u2658'
  assert Knight(EnumChessPiece.WHITE_KNIGHT, "e4").display_icon == '\u265E'

  assert Pawn(EnumChessPiece.BLACK_PAWN, "e5").display_icon     == '\u2659'
  assert Pawn(EnumChessPiece.WHITE_PAWN, "e5").display_icon     == '\u265F'

def test_piece_notation():
  assert King(EnumChessPiece.WHITE_KING, "a1").notation     == "Ka1"
  assert Queen(EnumChessPiece.BLACK_QUEEN, "c1").notation   == "Qc1"
  assert Rook(EnumChessPiece.WHITE_ROOK, "h8").notation     == "Rh8"
  assert Bishop(EnumChessPiece.BLACK_BISHOP, "b3").notation == "Bb3"
  assert Knight(EnumChessPiece.WHITE_KNIGHT, "e4").notation == "Ne4"
  assert Pawn(EnumChessPiece.BLACK_PAWN, "e5").notation     == "e5"

##################################################
# Testing chessboard constructor
##################################################

def test_chessboard():
  board = ChessBoard()
  
  starting_chess_board = [[Rook(EnumChessPiece.BLACK_ROOK, "a8"), Knight(EnumChessPiece.BLACK_KNIGHT, "b8"), Bishop(EnumChessPiece.BLACK_BISHOP, "c8"), Queen(EnumChessPiece.BLACK_QUEEN, "d8"), King(EnumChessPiece.BLACK_KING, "e8"), Bishop(EnumChessPiece.BLACK_BISHOP, "f8"), Knight(EnumChessPiece.BLACK_KNIGHT, "g8"), Rook(EnumChessPiece.BLACK_ROOK, "h8")],
                          [Pawn(EnumChessPiece.BLACK_PAWN, "a7"), Pawn(EnumChessPiece.BLACK_PAWN, "b7"), Pawn(EnumChessPiece.BLACK_PAWN, "c7"), Pawn(EnumChessPiece.BLACK_PAWN, "d7"), Pawn(EnumChessPiece.BLACK_PAWN, "e7"), Pawn(EnumChessPiece.BLACK_PAWN, "f7"), Pawn(EnumChessPiece.BLACK_PAWN, "g7"), Pawn(EnumChessPiece.BLACK_PAWN, "h7")],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [Pawn(EnumChessPiece.WHITE_PAWN, "a2"), Pawn(EnumChessPiece.WHITE_PAWN, "b2"), Pawn(EnumChessPiece.WHITE_PAWN, "c2"), Pawn(EnumChessPiece.WHITE_PAWN, "d2"), Pawn(EnumChessPiece.WHITE_PAWN, "e2"), Pawn(EnumChessPiece.WHITE_PAWN, "f2"), Pawn(EnumChessPiece.WHITE_PAWN, "g2"), Pawn(EnumChessPiece.WHITE_PAWN, "h2")],
                          [Rook(EnumChessPiece.WHITE_ROOK, "a1"), Knight(EnumChessPiece.WHITE_KNIGHT, "b1"), Bishop(EnumChessPiece.WHITE_BISHOP, "c1"), Queen(EnumChessPiece.WHITE_QUEEN, "d1"), King(EnumChessPiece.WHITE_KING, "e1"), Bishop(EnumChessPiece.WHITE_BISHOP, "f1"), Knight(EnumChessPiece.WHITE_KNIGHT, "g1"), Rook(EnumChessPiece.WHITE_ROOK, "h1")]]

  for i in range(len(board.board)):
    for j in range(len(board.board[i])):
      if(board.board[i][j] != None):
        assert (board.board[i][j].name == starting_chess_board[i][j].name and 
               board.board[i][j].colour == starting_chess_board[i][j].colour and
               board.board[i][j].position == starting_chess_board[i][j].position and # Also tests matrix_to_pos dictionary
               board.board[i][j].value == starting_chess_board[i][j].value and
               board.board[i][j].display_icon == starting_chess_board[i][j].display_icon)
        
      else:
        assert board.board[i][j] == starting_chess_board[i][j]

def test_build_blank_display_board():
  board = ChessBoard()
  board_border = \
"""
  ┌────┬────┬────┬────┬────┬────┬────┬────┐
8 │    │    │    │    │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
7 │    │    │    │    │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
6 │    │    │    │    │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
5 │    │    │    │    │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
4 │    │    │    │    │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
3 │    │    │    │    │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
2 │    │    │    │    │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
1 │    │    │    │    │    │    │    │    │
  └────┴────┴────┴────┴────┴────┴────┴────┘
    A    B    C    D    E    F    G    H
"""
  assert board.display_board == board_border[1:len(board_border)]

def test_build_starting_display_board():
  board = ChessBoard()
  board.update_display_board()
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