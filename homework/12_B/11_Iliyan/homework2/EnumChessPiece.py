from enum import Enum

class EnumChessPiece(Enum):
  # Unicode character/display_value, value of chesspiece
  WHITE_KING   = '\u265A', None
  WHITE_QUEEN  = '\u265B', 9
  WHITE_ROOK   = '\u265C', 5
  WHITE_BISHOP = '\u265D', 3
  WHITE_KNIGHT = '\u265E', 3
  WHITE_PAWN   = '\u265F', 1
  BLACK_KING   = '\u2654', None
  BLACK_QUEEN  = '\u2655', 9
  BLACK_ROOK   = '\u2656', 5
  BLACK_BISHOP = '\u2657', 3
  BLACK_KNIGHT = '\u2658', 3
  BLACK_PAWN   = '\u2659', 1