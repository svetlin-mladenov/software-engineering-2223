import sys
sys.path.append('Homework2')

from piece import *
from chessboard import *

def parse_fen(fen_string, chessboard):
    """
    Parse a FEN string and create a Chessboard object
    """
    fen_parts = fen_string.split(" ")
    board_string = fen_parts[0]
    board_rows = board_string.split("/")
    chessboard.clear_board()
    for row in range(8):
        col = 0
        for char in board_rows[row]:
            if char.isnumeric():
                col += int(char)
            elif char == 'p':
                chessboard.board[row][col] = Pawn("red")
                col += 1
            elif char == 'P':
                chessboard.board[row][col] = Pawn("blue")
                col += 1
            elif char == 'r':
                chessboard.board[row][col] = Rook("red")
                col += 1
            elif char == 'R':
                chessboard.board[row][col] = Rook("blue")
                col += 1
            elif char == 'n':
                chessboard.board[row][col] = Knight("red")
                col += 1
            elif char == 'N':
                chessboard.board[row][col] = Knight("blue")
                col += 1
            elif char == 'b':
                chessboard.board[row][col] = Bishop("red")
                col += 1
            elif char == 'B':
                chessboard.board[row][col] = Bishop("blue")
                col += 1
            elif char == 'q':
                chessboard.board[row][col] = Queen("red")
                col += 1
            elif char == 'Q':
                chessboard.board[row][col] = Queen("blue")
                col += 1
            elif char == 'k':
                chessboard.board[row][col] = King("red")
                col += 1
            elif char == 'K':
                chessboard.board[row][col] = King("blue")
                col += 1
    return chessboard

game = Chessboard()
print("Starting position")
game.print_board()

# Example usage
print("FEN position")
fen_string = "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25"
parse_fen(fen_string, game)
game.print_board()

