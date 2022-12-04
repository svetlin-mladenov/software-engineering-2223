from dataclasses import dataclass
from enum import Enum
from termcolor import colored


class PieceType(Enum):
    KING = "KING"
    QUEEN = "QUEEN"
    BISHOP = "BISHOP"
    KNIGHT = "KNIGHT"
    ROOK = "ROOK"
    PAWN = "PAWN"


class PieceColor(Enum):
    WHITE = "WHITE"
    BLACK = "BLACK"


@dataclass
class Piece:
    type: PieceType
    color: PieceColor

    def type_to_string(self) -> str:
        switcher = {
            PieceType.KING: "K",
            PieceType.QUEEN: "Q",
            PieceType.BISHOP: "B",
            PieceType.KNIGHT: "KN",
            PieceType.ROOK: "R",
            PieceType.PAWN: "P"
        }

        return switcher.get(self.type)

    def get_color_value(self, background_color: PieceColor) -> str:
        switcher = {
            PieceColor.BLACK: "grey",
            PieceColor.WHITE: "white"
        }

        return colored(self.type_to_string(), switcher.get(self.color), "on_grey" if background_color == PieceColor.BLACK else "on_white")
