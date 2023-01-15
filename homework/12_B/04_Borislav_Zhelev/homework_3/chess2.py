from enum import Enum
from termcolor import cprint, colored

class Letters(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8

class Pieces(Enum):
    PAWN = 0
    ROOK = 1
    BISHOP = 2
    KNIGHT = 3
    QUEEN = 4
    KING = 5
    NONE = 6

class Colors(Enum):
    BLACK = 0
    WHITE = 1

all_pieces = [["♟", "♜", "♝", "♞", "♛", "♚", " "],["♙","♖","♗","♘","♕","♔", " "]]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
str_pieces = {'p':Pieces.PAWN, 'n':Pieces.KNIGHT, 'b':Pieces.BISHOP, 'r':Pieces.ROOK, 'q':Pieces.QUEEN, 'k':Pieces.KING}

class Chess_pos:
    def __init__(self, piece:Pieces, piece_color:Colors, x:Letters, y:int) -> None:
        self.piece = piece
        self.piece_color = piece_color
        self.x = x
        self.y = y
        self.color = Colors((self.x.value + self.y)%2)#a1 -> (1+1)%2 = 0 = black

    def modify_self(self, new_piece:str) -> None:
        if new_piece.islower():
            self.piece_color = Colors.BLACK
        else:
            self.piece_color = Colors.WHITE

        new_piece = new_piece.lower()#transforms letter to lowercase
        self.piece = str_pieces.get(new_piece)

    def is_valid_x(self) -> bool:
        if type(self.x) == Letters:
            return True
        else:
            return False

    def is_valid_y(self) -> bool:
        if type(self.y) == int:
            if self.y >= 1 and self.y <= 8:
                return True
            else:
                return False
        else:
            return False

    def is_valid_piece(self) -> bool:
        if type(self.piece) == Pieces:
            return True
        else:
            return False

    def is_valid_piece_color(self) -> bool:
        if type(self.piece_color) == Colors:
            return True
        else:
            return False

    def is_valid(self) -> bool:
        if self.is_valid_x() and self.is_valid_y() and self.is_valid_piece() and self.is_valid_piece_color():
            return True
        else:
            return False

    def my_print(self) -> None:
        if self.is_valid():
            if self.color.value == 0:#black
                print(all_pieces[self.piece_color.value][self.piece.value], "", end=' ')
            else:
                cprint((str(all_pieces[self.piece_color.value][self.piece.value])+" "),  None, "on_white",  end=' ')
        else:
            print("invalid position")

sp = "r5rk/1p1q1p1p/p7/3N4/3PnB1b/2P2Q1P/PP3P2/R3R2K b - - 0 25"#input string
cb = []

def load_pos(starting_pos:str, chess_board:list)->None:
    for i in range(1,9):
        for j in range(1,9):
            chess_board.append(Chess_pos(Pieces.NONE, Colors.WHITE, Letters(i), j))#initializing default values for all spaces on the board

    i = 0 #iterator for the string
    x = 0 #goes from 0 - 7 depending on the row
    y = 0 #goes from 0 - 7 depending on the colmn
    while True:
        while True:
            if starting_pos[i] == ' ':
                return
            if starting_pos[i] == '/':
                break
            if starting_pos[i] not in numbers:#if the pos is a piece, it is assigned to the square on the board
                chess_board[x*8 + y].modify_self(starting_pos[i])
                y = y + 1
            else:#if it is a number, we skip by this amount of spaces on the board
                y = y + ord(starting_pos[i]) - ord('0')
            i = i + 1
        y = 0
        i = i + 1
        x = x + 1



load_pos(sp, cb)
for i in range(64):
    cb[i].my_print()
    if (i + 1) % 8 == 0:
        print()#new line