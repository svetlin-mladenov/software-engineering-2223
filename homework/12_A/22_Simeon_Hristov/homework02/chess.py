from termcolor import colored
from enum import Enum
from dataclasses import dataclass, field


class Chess_pieces(Enum):
    WHITE_KING = "♔ "
    WHITE_QUEEN = "♕ "
    WHITE_ROOK = "♖ "
    WHITE_BISHOP = "♗ "
    WHITE_KNIGHT = "♘ "
    WHITE_PAWN = "♙ "
    BLACK_KING = "♚ "
    BLACK_QUEEN = "♛ "
    BLACK_ROOK = "♜ "
    BLACK_BISHOP = "♝ "
    BLACK_KNIGHT = "♞ "
    BLACK_PAWN = "♟ "


@dataclass
class Chessboard():
    board: list = field(default_factory=list)

    def print_position(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if ((i % 2) == (j % 2)):
                    print(colored(self.board[i][j],
                                  None,  "on_white"), end="")
                else:
                    print(self.board[i][j], end="")
            print()


example = Chessboard(
    [
        [Chess_pieces.BLACK_ROOK.value, Chess_pieces.BLACK_KNIGHT.value, Chess_pieces.BLACK_BISHOP.value,
         Chess_pieces.BLACK_QUEEN.value, Chess_pieces.BLACK_KING.value, Chess_pieces.BLACK_BISHOP.value,
         Chess_pieces.BLACK_KNIGHT.value, Chess_pieces.BLACK_ROOK.value],
        [Chess_pieces.BLACK_PAWN.value for i in range(8)],
        ["  " for i in range(8)],
        ["  " for i in range(8)],
        ["  " for i in range(8)],
        ["  " for i in range(8)],
        [Chess_pieces.WHITE_PAWN.value for i in range(8)],
        [Chess_pieces.WHITE_ROOK.value, Chess_pieces.WHITE_KNIGHT.value, Chess_pieces.WHITE_BISHOP.value,
         Chess_pieces.WHITE_QUEEN.value, Chess_pieces.WHITE_KING.value, Chess_pieces.WHITE_BISHOP.value,
         Chess_pieces.WHITE_KNIGHT.value, Chess_pieces.WHITE_ROOK.value]
    ]
)
example.print_position()
