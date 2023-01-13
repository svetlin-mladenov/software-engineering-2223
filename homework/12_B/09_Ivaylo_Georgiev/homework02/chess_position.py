from enum import Enum
from termcolor import *
from colorama import init
from dataclasses import dataclass

@dataclass
class WhitePieces(Enum):
    pawn = '♙ '
    knight = '♘ '
    bishop = '♗ '
    king = '♔ '
    rook = '♖ '
    queen = '♕ '

@dataclass
class BlackPieces(Enum):
    pawn = '♟ '
    knight = '♞ '
    bishop = '♝ '
    king = '♚ '
    rook = '♜ '
    queen = '♛ '

class ChessBoard():
    board = [['  ' for i in range(8)] for j in range(8)]

    def __init__(self) -> None:
        order_of_last_row= ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
        for i in range(8):
            self.board[0][i] = BlackPieces[order_of_last_row[i]].value
            self.board[7][i] = WhitePieces[order_of_last_row[i]].value

            self.board[1][i] = BlackPieces.pawn.value
            self.board[6][i] = WhitePieces.pawn.value


    def PrintBoard(self):
        main_color = 'white'

        for i in range(8): 
            print(f"{8-i} ", end=" ")

            for j in range(8):
                if main_color == 'black':
                    cprint(f"{self.board[i][j]}", end="")
                    main_color = 'white'
                else:
                    cprint(f"{self.board[i][j]}", None, 'on_white', end="")
                    main_color = 'black'
            print()

            if(main_color == 'black'):
                main_color = 'white'
            else:
                main_color = 'black'

        print("    A B C D E F G H")

if __name__ == "__main__":
    NewBoard = ChessBoard()
    NewBoard.PrintBoard()