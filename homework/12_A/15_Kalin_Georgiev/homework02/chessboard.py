from enum import Enum
from termcolor import cprint

class White(Enum):
     Pawn = " ♙ "
     Rook = " ♖ "
     Knight = " ♘ "
     Bishop = " ♗ "
     King = " ♔ "
     Queen = " ♕ "

class Black(Enum):
     Pawn = " ♟ "
     Rook = " ♜ "
     Knight = " ♞ "
     Bishop = " ♝ "
     King = " ♚ "
     Queen = " ♛ "
     
class Numbers(Enum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
     

class Chessboard:
    
    def give_num(self, value):
        return " {} {}".format(value, "")
    
    def __init__(self):
        self.board = [
                        [[0, self.give_num(Numbers.one.value)], [1, Black.Rook.value], [0, Black.Knight.value], [1, Black.Bishop.value], [0, Black.Queen.value], [1, Black.King.value], [0, Black.Bishop.value], [1, Black.Knight.value], [0, Black.Rook.value], [0, self.give_num(Numbers.one.value)]],
                        [[0, self.give_num(Numbers.two.value)], [0, Black.Pawn.value], [1, Black.Pawn.value], [0, Black.Pawn.value], [1, Black.Pawn.value], [0, Black.Pawn.value], [1, Black.Pawn.value], [0, Black.Pawn.value], [1, Black.Pawn.value], [0, self.give_num(Numbers.two.value)]],
                        [[0, self.give_num(Numbers.three.value)], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [0, self.give_num(Numbers.three.value)]],
                        [[0, self.give_num(Numbers.four.value)], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, self.give_num(Numbers.four.value)]],
                        [[0, self.give_num(Numbers.five.value)], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [0, self.give_num(Numbers.five.value)]],
                        [[0, self.give_num(Numbers.six.value)], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, "   "], [1, "   "], [0, self.give_num(Numbers.six.value)]],
                        [[0, self.give_num(Numbers.seven.value)], [1, White.Pawn.value], [0, White.Pawn.value], [1, White.Pawn.value], [0, White.Pawn.value], [1, White.Pawn.value], [0, White.Pawn.value], [1, White.Pawn.value], [0, White.Pawn.value], [0, self.give_num(Numbers.seven.value)]],
                        [[0, self.give_num(Numbers.eight.value)], [0, White.Rook.value], [1, White.Knight.value], [0, White.Bishop.value], [1, White.King.value], [0, White.Queen.value], [1, White.Bishop.value], [0, White.Knight.value], [1, White.Rook.value], [0, self.give_num(Numbers.eight.value)]]]

    def print_chessboard_layout(self):
        for i in range(0, 8):
            for j in range(0, 10):
                if self.board[i][j][0] == 0:
                    print(self.board[i][j][1], end = "")
                else:
                    cprint(self.board[i][j][1], None, "on_white", end = "")
                if j == 9:
                    print("\n", end = "")

chessboard = Chessboard()
print("    A  B  C  D  E  F  G  H")
chessboard.print_chessboard_layout()
print("    A  B  C  D  E  F  G  H")