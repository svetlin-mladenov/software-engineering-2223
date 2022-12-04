
Домашно N2:
Svetlin Mladenov
•
24.11
100 точки
Краен срок: Днес
Create a data structure that represents a chess
position. Use it to represent the starting position of a chess game.
Print the position to screen. A position in chess is a board with a
particular configuration of the pieces on it.

Notes:
You may use termcolor to print colors.
When submitting the PR please add a screenshot of the position printed.
You can also use emojis to print the figures on the board.

termcolor · PyPI
https://pypi.org/project/termcolor/
Коментари за курса
Вашата работа
Предадени

chess.py
Текст

Chess_starting_possitions.jpg
Изображение
Частни коментари
from string import ascii_uppercase

width = 8
height = 8

files = "0" + ascii_uppercase[:width]
ranks = range(0, height + 1)


boardmatrix = [["  " for x in range(1, height + 1)]
               for y in range(1, width + 1)]


def reset(setting):
    global boardmatrix
    if setting == "empty":
        boardmatrix = [["  " for x in range(1, height + 1)]
                       for x in range(1, width + 1)]


    else:
        print("Something failed.")



class piece:
    # Summons piece of given color and position
    def __init__(self, color, piece, position):

        # color
        if color == "w":
            self.color = "white"
        elif color == "b":
            self.color = "black"
        else:
            self.color = "none"

        # piece
        if piece == "p":
            self.piece = "pawn"
            self.short = color + "P"
        elif piece == "n":
            self.piece = "knight"
            self.short = color + "N"
        elif piece == "b":
            self.piece = "bishop"
            self.short = color + "B"
        elif piece == "r":
            self.piece = "rook"
            self.short = color + "R"
            self.canCastle = True
        elif piece == "q":
            self.piece = "queen"
            self.short = color + "Q"
        elif piece == "k":
            self.piece = "king"
            self.short = color + "K"
            self.canCastle = True

        self.position = position.upper()
        file = files.index(((self.position[0]).upper()))
        rank = self.position[1:]
        boardmatrix[int(file) - 1][int(rank) - 1] = self.short


wApawn = piece("w", "p", "a2")
wBpawn = piece("w", "p", "b2")
wCpawn = piece("w", "p", "c2")
wDpawn = piece("w", "p", "d2")
wEpawn = piece("w", "p", "e2")
wFpawn = piece("w", "p", "f2")
wGpawn = piece("w", "p", "g2")
wHpawn = piece("w", "p", "h2")

bApawn = piece("b", "p", "a7")
bBpawn = piece("b", "p", "b7")
bCpawn = piece("b", "p", "c7")
bDpawn = piece("b", "p", "d7")
bEpawn = piece("b", "p", "e7")
bFpawn = piece("b", "p", "f7")
bGpawn = piece("b", "p", "g7")
bHpawn = piece("b", "p", "h7")


wQrook = piece("w", "r", "a1")
wQknight = piece("w", "n", "b1")
wBbishop = piece("w", "b", "c1")
wQueen = piece("w", "q", "d1")
wKing = piece("w", "k", "e1")
wWbishop = piece("w", "b", "f1")
wKknight = piece("w", "n", "g1")
wKrook = piece("w", "r", "h1")

bQrook = piece("b", "r", "a8")
bQknight = piece("b", "n", "b8")
bBbishop = piece("b", "b", "c8")
bQueen = piece("b", "q", "d8")
bKing = piece("b", "k", "e8")
bWbishop = piece("b", "b", "f8")
bKknight = piece("b", "n", "g8")
bKrook = piece("b", "r", "h8")

print("Chess board")
print("")

for line in boardmatrix:
    print(line)
