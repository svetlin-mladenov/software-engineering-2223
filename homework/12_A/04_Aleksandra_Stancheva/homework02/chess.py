import sys
from termcolor import colored, cprint


class ChessBoard:
    def __init__(self):
        self.chess_board = [[[0, " ♜ "], [1, " ♞ "], [0, " ♝ "], [1, " ♛ "], [0, " ♚ "], [1, " ♝ "], [0, " ♞ "], [1, " ♜ "]], 
                            [[1, " ♟ "], [0, " ♟ "], [1, " ♟ "], [0, " ♟ "], [1, " ♟ "], [0, " ♟ "], [1, " ♟ "], [0, " ♟ "]],
                            [[0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "]],
                            [[1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "]],
                            [[0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "]],
                            [[1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "]],
                            [[0, " ♙ "], [1, " ♙ "], [0, " ♙ "], [1, " ♙ "], [0, " ♙ "], [1, " ♙ "], [0, " ♙ "], [1, " ♙ "]],
                            [[1, " ♖ "], [0, " ♘ "], [1, " ♗ "], [0, " ♕ "], [1, " ♔ "], [0, " ♗ "], [1, " ♘ "], [0, " ♖ "]]]

    def print_chess_board(self):   
        for i in range (0, 8):
            for y in range (0, 8):
                if self.chess_board[i][y][0] == 0:
                    cprint(self.chess_board[i][y][1], "grey", "on_white", end = "")
                else:
                    cprint(self.chess_board[i][y][1], "grey", "on_grey", end = "")
                if y == 7:
                    print("\n", end = "")
                

if __name__ == "__main__":
    my_board = ChessBoard()
    my_board.print_chess_board()
