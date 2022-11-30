from dataclasses import dataclass


@dataclass
class ChessPiece:
    emoji: str

    def print(self):
        print(self.emoji, end="")

class ChessBoard:
    def __init__(self):
        self.board = [
            [ChessPiece("♜"), ChessPiece("♞"), ChessPiece("♝"), ChessPiece("♛"), ChessPiece("♚"), ChessPiece("♝"), ChessPiece("♞"), ChessPiece("♜")],
            [ChessPiece("♟") for _ in range(8)],
            [ChessPiece(" ") for _ in range(8)],
            [ChessPiece(" ") for _ in range(8)],
            [ChessPiece(" ") for _ in range(8)],
            [ChessPiece(" ") for _ in range(8)],
            [ChessPiece("♙") for _ in range(8)],
            [ChessPiece("♖"), ChessPiece("♘"), ChessPiece("♗"), ChessPiece("♕"), ChessPiece("♔"), ChessPiece("♗"), ChessPiece("♘"), ChessPiece("♖")],
        ]

    def print(self):
        for i, row in enumerate(self.board):
            for j, piece in enumerate(row):
                print(f"\033[{37-(i%2==j%2)*7};{40+(i%2==j%2)*7}m ", end="")
                piece.print()
                print(" \033[0m", end="")
            print()


if __name__ == "__main__":
    board = ChessBoard()
    board.print()
