import string
from dataclasses import dataclass
from termcolor import *


@dataclass
class ChessFigure:
    color: str
    symbol: str

    def __str__(self) -> str:
        return self.symbol


class ChessBoard:

    def __init__(self, fen: str = None):
        self.board = [[None for i in range(8)] for j in range(8)]

        if fen:
            self.loadPosition(fen)

    def loadPosition(self, fen: str) -> None:
        fen_parts = fen.split(" ")
        position_parts = fen_parts[0].split("/")
        for i, row in enumerate(position_parts):
            col = 0
            for char in row:
                if char.isdigit():
                    col += int(char)
                else:
                    self.board[i][col] = self.getFigure(char)
                    col += 1

    def getFigure(self, char: str) -> ChessFigure:
        figures = {
            "p": ChessFigure("black", "♟ "),
            "r": ChessFigure("black", "♜ "),
            "n": ChessFigure("black", "♞ "),
            "b": ChessFigure("black", "♝ "),
            "q": ChessFigure("black", "♛ "),
            "k": ChessFigure("black", "♚ "),
            "P": ChessFigure("white", "♙ "),
            "R": ChessFigure("white", "♖ "),
            "N": ChessFigure("white", "♘ "),
            "B": ChessFigure("white", "♗ "),
            "Q": ChessFigure("white", "♕ "),
            "K": ChessFigure("white", "♔ "),
        }
        return figures[char]

    def printPosition(self) -> None:
        def printLetters() -> None:
            print("\t  ", end="")
            for i in string.ascii_uppercase[:8]:
                print(f"{i} ", end="")
            print("")
        
        def printBoard() -> None:
            for col, row in enumerate(self.board):
                print(f"\t{col + 1} ", end="")
                for j, figure in enumerate(row):
                    if (col % 2 == 0 and j % 2 == 0) or (col % 2 != 0 and j % 2 != 0):
                        cprint(figure or "  ", attrs=["reverse"], end="")

                    else:
                        print(figure or "  ", end="")

                print(f" {col + 1} ")
                

        print("\n\n\n")
        printLetters()
        printBoard()
        printLetters()
        print("\n\n\n")
    
def main() -> None:
    fen = "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25"
    chess_board = ChessBoard(fen)
    chess_board.printPosition()

if __name__ == "__main__":
    main()
    
