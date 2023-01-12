from dataclasses import dataclass
from typing import List


@dataclass
class ChessPiece:
    emoji: str

    def print(self):
        print(self.emoji, end="")

class ChessBoard:
    # def __init__(self):
    #     self.board = [
    #         [ChessPiece("♜"), ChessPiece("♞"), ChessPiece("♝"), ChessPiece("♛"), ChessPiece("♚"), ChessPiece("♝"), ChessPiece("♞"), ChessPiece("♜")],
    #         [ChessPiece("♟") for _ in range(8)],
    #         [ChessPiece(" ") for _ in range(8)],
    #         [ChessPiece(" ") for _ in range(8)],
    #         [ChessPiece(" ") for _ in range(8)],
    #         [ChessPiece(" ") for _ in range(8)],
    #         [ChessPiece("♙") for _ in range(8)],
    #         [ChessPiece("♖"), ChessPiece("♘"), ChessPiece("♗"), ChessPiece("♕"), ChessPiece("♔"), ChessPiece("♗"), ChessPiece("♘"), ChessPiece("♖")],
    #     ]

    def print(self):
        for i, row in enumerate(self.board):
            for j, piece in enumerate(row):
                print(f"\033[{37-(i%2==j%2)*7};{40+(i%2==j%2)*7}m ", end="")
                piece.print()
                print(" \033[0m", end="")
            print()

    def __init__(self):
      
        self.board = self.parse_fen("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25")

    def parse_fen(self, fen: str) -> List[List[ChessPiece]]:
        """Parses a FEN string and returns a 2D list representing the chess board."""
        rows = fen.split(" ")[0].split("/")
        board = []
        for row in rows:
            new_row = []
            for char in row:
                if char.isdigit():
                    new_row.extend([ChessPiece(" ") for _ in range(int(char))])
                else:
                    new_row.append(ChessPiece(char))
            board.append(new_row)
        return board


if __name__ == "__main__":
    board = ChessBoard()
    board.print()
    