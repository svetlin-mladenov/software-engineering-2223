from termcolor import cprint

class White:
     Pawn = " ♙ "
     Rook = ' ♖ '
     Knight = ' ♘ '
     Bishop = ' ♗ '
     King = ' ♔ '
     Queen = ' ♕ '

class Black:
     Pawn = ' ♟ '
     Rook = ' ♜ '
     Knight = ' ♞ '
     Bishop = ' ♝ '
     King = ' ♚ '
     Queen = ' ♛ '

class Board:
    def __init__(self):
        self.board = [[[1, Black.Rook], [0, Black.Knight], [1, Black.Bishop], [0, Black.Queen], [1, Black.King], [0, Black.Bishop], [1, Black.Knight], [0, Black.Rook]],
                      [[0, Black.Pawn], [1, Black.Pawn], [0, Black.Pawn], [1, Black.Pawn], [0, Black.Pawn], [1, Black.Pawn], [0, Black.Pawn], [1, Black.Pawn]],
                      [[1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "]],
                      [[0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "]],
                      [[1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "]],
                      [[0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "]],
                      [[1, White.Pawn], [0, White.Pawn], [1, White.Pawn], [0, White.Pawn], [1, White.Pawn], [0, White.Pawn], [1, White.Pawn], [0, White.Pawn]],
                      [[0, White.Rook], [1, White.Knight], [0, White.Bishop], [1, White.King], [0, White.Queen], [1, White.Bishop], [0, White.Knight], [1, White.Rook]]]

    def print_board(self):
        for i in range(0, 8):
            for j in range(0, 8):
                if self.board[i][j][0] == 1:
                    cprint(self.board[i][j][1], "red", "on_white", end = "")
                else:
                    cprint(self.board[i][j][1], "white", "on_red", end = "")
                if j == 7:
                    print("\n", end = "")

board = Board()
board.print_board()