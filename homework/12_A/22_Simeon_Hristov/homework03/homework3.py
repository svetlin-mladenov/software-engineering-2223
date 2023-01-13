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
class FEN_position():
    FEN_position : str = field(default_factory=str)
    
    def read_position(self):
        board = []
        row = []
        for letter in self.FEN_position:
            match letter:
                case 'r':
                    row.append(Chess_pieces.BLACK_ROOK.value)
                case 'n':
                    row.append(Chess_pieces.BLACK_KNIGHT.value)
                case 'b':
                    row.append(Chess_pieces.BLACK_BISHOP.value)
                case 'q':
                    row.append(Chess_pieces.BLACK_QUEEN.value)
                case 'k':
                    row.append(Chess_pieces.BLACK_KING.value)
                case 'p':
                    row.append(Chess_pieces.BLACK_PAWN.value) 
                case 'R':
                    row.append(Chess_pieces.WHITE_ROOK.value)
                case 'N':
                    row.append(Chess_pieces.WHITE_KNIGHT.value)
                case 'B':
                    row.append(Chess_pieces.WHITE_BISHOP.value)
                case 'Q':
                    row.append(Chess_pieces.WHITE_QUEEN.value)
                case 'K':
                    row.append(Chess_pieces.WHITE_KING.value)
                case 'P':
                    row.append(Chess_pieces.WHITE_PAWN.value)
                case '/':
                    board.append(row)
                    row = []
                case _:
                    for i in range(int(letter)):
                        row.append("  ")
        board.append(row)
        return board

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

    


example = FEN_position("1q4Q1/1q4Q1/1q4Q1/qqq2QQQ/qqqkKQQQ/8/8/8").read_position()
chessboard_example = Chessboard(example)
chessboard_example.print_position()