import string
from termcolor import *


class ChessPiece:

    def __init__(self, color, symbol) -> None:
        self.color = color
        self.symbol = symbol
    
    def __str__(self) -> str:
        return self.symbol


class ChessBoard:

    def __init__(self) -> None:
        self.board = [[None for i in range(8)] for j in range(8)]
        for i in range(8):
            self.board[1][i] = ChessPiece("black", "♟ ︎")
            self.board[6][i] = ChessPiece("white", "♙ ")

        self.board[0][0] = ChessPiece("black", "♜ ")
        self.board[0][1] = ChessPiece("black", "♞ ")
        self.board[0][2] = ChessPiece("black", "♝ ")
        self.board[0][3] = ChessPiece("black", "♛ ")
        self.board[0][4] = ChessPiece("black", "♚ ")
        self.board[0][5] = ChessPiece("black", "♝ ")
        self.board[0][6] = ChessPiece("black", "♞ ")
        self.board[0][7] = ChessPiece("black", "♜ ")

        self.board[7][0] = ChessPiece("white", "♖ ")
        self.board[7][1] = ChessPiece("white", "♘ ")
        self.board[7][2] = ChessPiece("white", "♗ ")
        self.board[7][3] = ChessPiece("white", "♕ ")
        self.board[7][4] = ChessPiece("white", "♔ ")
        self.board[7][5] = ChessPiece("white", "♗ ")
        self.board[7][6] = ChessPiece("white", "♘ ")
        self.board[7][7] = ChessPiece("white", "♖ ")

    def print_position(self) -> None:
        """ Print the current chess position """
        for i, row in enumerate(self.board):
            print(f"{i + 1} ", end="")
            for j, piece in enumerate(row):
                if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
                    cprint(piece or "  ", attrs=["reverse"], end="")

                else:
                    print(piece or "  ", end="")

            print("")
        
        print("  ", end="")
        for i in string.ascii_uppercase[:len(self.board)]:
            print(f"{i} ", end="")

        print("")


def main() -> None:

    chess_board = ChessBoard()
    chess_board.print_position()


if __name__ == "__main__":
    main()
