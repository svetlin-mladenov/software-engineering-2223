from termcolor import cprint
from colorama import init
from dataclasses import dataclass

pieces = {
    'R': '♖ ',
    'N': '♘ ',
    'B': '♗ ',
    'Q': '♕ ',
    'K': '♔ ',
    'P': '♙ ',
    'r': '♜ ',
    'n': '♞ ',
    'b': '♝ ',
    'q': '♛ ',
    'k': '♚ ',
    'p': '♟ '
}


class Board():
    def __init__(self):
        self.board = [['  ' for i in range(8)] for j in range(8)]

    def parse_fen(self, string):
        row, column = 0, 0

        i = 0
        while (string[i] != ' '):
            if (string[i].isnumeric()):
                column += int(string[i])
                i += 1

            elif (string[i] == '/'):
                row += 1
                column = 0
                i += 1

            else:
                slot = pieces[string[i]]
                self.board[row][column] = slot
                column += 1
                i += 1

    def board_print(self):
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
    NewBoard = Board()
    NewBoard.parse_fen("r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K w - - 0 25")
    NewBoard.board_print()