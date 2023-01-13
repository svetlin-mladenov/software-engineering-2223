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

    board = [[None for i in range(8)] for j in range(8)]
    for i in range(8):
        board[1][i] = ChessFigure("black", "♟ ︎")
        board[6][i] = ChessFigure("white", "♙ ")

    board[0][0] = ChessFigure("black", "♜ ")
    board[0][1] = ChessFigure("black", "♞ ")
    board[0][2] = ChessFigure("black", "♝ ")
    board[0][3] = ChessFigure("black", "♛ ")
    board[0][4] = ChessFigure("black", "♚ ")
    board[0][5] = ChessFigure("black", "♝ ")
    board[0][6] = ChessFigure("black", "♞ ")
    board[0][7] = ChessFigure("black", "♜ ")

    board[7][0] = ChessFigure("white", "♖ ")
    board[7][1] = ChessFigure("white", "♘ ")
    board[7][2] = ChessFigure("white", "♗ ")
    board[7][3] = ChessFigure("white", "♕ ")
    board[7][4] = ChessFigure("white", "♔ ")
    board[7][5] = ChessFigure("white", "♗ ")
    board[7][6] = ChessFigure("white", "♘ ")
    board[7][7] = ChessFigure("white", "♖ ")

    
    
    
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

    chess_board = ChessBoard()
    chess_board.printPosition()


if __name__ == "__main__":
    main()
