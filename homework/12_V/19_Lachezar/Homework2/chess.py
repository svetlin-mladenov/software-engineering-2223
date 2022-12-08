from dataclasses import dataclass
from termcolor import colored
from math import floor
from chess_piece import Piece, PieceType, PieceColor


@dataclass
class Chess:
    pieces = \
        [Piece(PieceType.ROOK, PieceColor.BLACK),
         Piece(PieceType.KNIGHT, PieceColor.BLACK),
         Piece(PieceType.BISHOP, PieceColor.BLACK),
         Piece(PieceType.QUEEN, PieceColor.BLACK),
         Piece(PieceType.KING, PieceColor.BLACK),
         Piece(PieceType.BISHOP, PieceColor.BLACK),
         Piece(PieceType.KNIGHT, PieceColor.BLACK),
         Piece(PieceType.ROOK, PieceColor.BLACK)] + \
        ([Piece(PieceType.PAWN, PieceColor.BLACK)] * 8) + \
        ([None] * 32) + \
        ([Piece(PieceType.PAWN, PieceColor.WHITE)] * 8) + \
        [Piece(PieceType.ROOK, PieceColor.WHITE),
            Piece(PieceType.KNIGHT, PieceColor.WHITE),
            Piece(PieceType.BISHOP, PieceColor.WHITE),
            Piece(PieceType.QUEEN, PieceColor.WHITE),
            Piece(PieceType.KING, PieceColor.WHITE),
            Piece(PieceType.BISHOP, PieceColor.WHITE),
            Piece(PieceType.KNIGHT, PieceColor.WHITE),
            Piece(PieceType.ROOK, PieceColor.WHITE)]

    def get_color_value(self, is_white: bool, should_invert: bool):
        return PieceColor.WHITE if (is_white and not should_invert) or (not is_white and should_invert) else PieceColor.BLACK

    def print(self):
        for (index, _) in enumerate(self.pieces):
            end = chr(9) if ((index+1) % 8) != 0 else '\n'
            background_color = self.get_color_value(
                ((index) % 2) != 0, floor((index) / 8) % 2 == 0)

            color_value = self.pieces[index].get_color_value(
                background_color) if self.pieces[index] is not None else colored("*", "magenta", "on_grey" if background_color ==
                                                                                 PieceColor.BLACK else "on_white")

            print(color_value, end=end)


chess = Chess()
chess.print()
