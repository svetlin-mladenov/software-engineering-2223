from enum import Enum, auto


class ChessPieceType(Enum):
    PAWN = auto()
    ROOK = auto()
    KNIGHT = auto()
    BISHOP = auto()
    QUEEN = auto()
    KING = auto()

    EMPTY = auto()


class ChessPieceGroup(Enum):
    ANIMALS = auto()
    PLANTS = auto()
    CREATURES = auto()
    BIRDS = auto()
    FARM = auto()
